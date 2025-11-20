# path: c:\Users\infin\Documents\LABS\POLTEK\MyKisahCrypto\MyKisahCrypto\solve_my_kisah_crypto.py
import os, re, struct, zlib, base64, binascii

ROOT = r"c:\Users\infin\Documents\LABS\POLTEK\MyKisahCrypto\MyKisahCrypto"
PNG_SIG = b"\x89PNG\r\n\x1a\n"

def find_flag_in_text(s):
    m = re.search(r"(CTF|CYBERLAB)\{[^}]+\}", s)
    return m.group(0) if m else None

def try_base64(s):
    try:
        return base64.b64decode(s, validate=True)
    except Exception:
        try:
            return base64.b64decode(s + "===")
        except Exception:
            return None

def try_hex(s):
    s2 = s.strip().replace(" ", "")
    if len(s2) % 2 == 0 and re.fullmatch(r"[0-9a-fA-F]+", s2 or ""):
        try:
            return binascii.unhexlify(s2)
        except Exception:
            return None
    return None

def caesar_all(s):
    out = []
    for k in range(26):
        t = []
        for ch in s:
            if 'a' <= ch <= 'z':
                t.append(chr((ord(ch)-97+k)%26+97))
            elif 'A' <= ch <= 'Z':
                t.append(chr((ord(ch)-65+k)%26+65))
            else:
                t.append(ch)
        out.append(("shift+"+str(k), "".join(t)))
    return out

def read_zip(path):
    # Minimal ZIP parser: list entries and read raw file payloads and comment
    data = open(path, "rb").read()
    # EOCD: PK\x05\x06
    idx = data.rfind(b"PK\x05\x06")
    comment = ""
    if idx != -1 and idx+22 <= len(data):
        try:
            # comment length is last 2 bytes of EOCD
            clen = struct.unpack("<H", data[idx+20:idx+22])[0]
            comment = data[idx+22:idx+22+clen].decode("latin1", errors="ignore")
        except Exception:
            pass
    files = []
    # naive scan for local headers PK\x03\x04
    i = 0
    while True:
        j = data.find(b"PK\x03\x04", i)
        if j == -1: break
        try:
            # parse local file header
            hdr = data[j+4:j+30]
            _, _, _, _, _, _, comp_size, uncomp_size, nlen, elen = struct.unpack("<HHHHHIIIHH", hdr)
            name = data[j+30:j+30+nlen].decode("latin1", errors="ignore")
            extra_off = j+30+nlen
            comp_off = extra_off+elen
            payload = data[comp_off:comp_off+comp_size]
            files.append((name, payload))
            i = comp_off+comp_size
        except Exception:
            i = j+4
    return comment, files

def parse_png_chunks(b):
    if not b.startswith(PNG_SIG): return {}
    out = {"text": [], "after_IEND": b[b.rfind(b"IEND")+8:] if b.rfind(b"IEND")!=-1 else b""}
    i = 8
    while i+8 <= len(b):
        try:
            length = struct.unpack(">I", b[i:i+4])[0]
            ctype = b[i+4:i+8]
            chunk = b[i+8:i+8+length]
            i = i+8+length+4  # skip CRC
            if ctype in (b"tEXt", b"iTXt", b"zTXt"):
                out["text"].append(chunk)
        except Exception:
            break
    return out

def png_pixels_lsb(b):
    # Attempt to reconstruct pixels then take LSBs to text
    try:
        # IHDR
        p = 8
        if b[p:p+4] != b"\x00\x00\x00\x0d": return None
        ctype = b[p+4:p+8]
        if ctype != b"IHDR": return None
        w,h,bit_depth,color_type = struct.unpack(">IIBB", b[p+8:p+8+9])[:4]
        # collect IDAT
        idats = []
        p = 8
        while p+8 <= len(b):
            ln = struct.unpack(">I", b[p:p+4])[0]
            ct = b[p+4:p+8]
            if ct == b"IDAT":
                idats.append(b[p+8:p+8+ln])
            p = p+8+ln+4
        raw = zlib.decompress(b"".join(idats))
        # bytes per pixel
        bpp = {0:1,2:3,6:4}.get(color_type, 4)
        stride = w*bpp
        out = []
        i = 0
        prev = bytearray(stride)
        def paeth(a,b,c):
            p = a + b - c
            pa = abs(p - a); pb = abs(p - b); pc = abs(p - c)
            return a if pa <= pb and pa <= pc else (b if pb <= pc else c)
        while i < len(raw):
            f = raw[i]; i += 1
            line = bytearray(raw[i:i+stride]); i += stride
            if f == 1:
                for x in range(stride):
                    left = line[x-bpp] if x >= bpp else 0
                    line[x] = (line[x] + left) & 0xFF
            elif f == 2:
                for x in range(stride):
                    up = prev[x]
                    line[x] = (line[x] + up) & 0xFF
            elif f == 3:
                for x in range(stride):
                    left = line[x-bpp] if x >= bpp else 0
                    up = prev[x]
                    line[x] = (line[x] + ((left+up)//2)) & 0xFF
            elif f == 4:
                for x in range(stride):
                    left = line[x-bpp] if x >= bpp else 0
                    up = prev[x]
                    upleft = prev[x-bpp] if x >= bpp else 0
                    line[x] = (line[x] + paeth(left, up, upleft)) & 0xFF
            out.extend(line); prev = line
        bits = [(b & 1) for b in out]
        ba = bytearray()
        for k in range(0, len(bits), 8):
            byte = 0
            for bit in bits[k:k+8]:
                byte = (byte<<1)|bit
            ba.append(byte)
        return ba.decode("utf-8", errors="ignore")
    except Exception:
        return None

def pipeline_decode(txt):
    # try base64 then hex then caesar in various orders
    tried = set()
    queue = [txt]
    while queue:
        s = queue.pop(0)
        if s in tried: continue
        tried.add(s)
        fl = find_flag_in_text(s)
        if fl: return fl
        for cand in [try_base64(s), try_hex(s)]:
            if cand:
                try:
                    ns = cand.decode("utf-8")
                except Exception:
                    ns = cand.decode("latin1", errors="ignore")
                queue.append(ns)
        for name, cs in caesar_all(s):
            fl = find_flag_in_text(cs)
            if fl: return fl
    return None

def main():
    zips = [os.path.join(ROOT, f) for f in os.listdir(ROOT) if f.lower().endswith(".zip")]
    found = None
    for zp in zips:
        comment, files = read_zip(zp)
        if comment:
            f = find_flag_in_text(comment)
            if f: print("FLAG in zip comment:", f); return
            f = pipeline_decode(comment)
            if f: print("FLAG via decoded zip comment:", f); return
        for name, payload in files:
            if name.endswith(".png"):
                chunks = parse_png_chunks(payload)
                for t in chunks["text"]:
                    try:
                        s = t.decode("latin1", errors="ignore")
                    except Exception:
                        s = ""
                    f = find_flag_in_text(s) or pipeline_decode(s)
                    if f: print(f"FLAG from PNG text chunk {name}:", f); return
                # appended data after IEND
                if chunks.get("after_IEND"):
                    s = chunks["after_IEND"].decode("latin1", errors="ignore")
                    f = find_flag_in_text(s) or pipeline_decode(s)
                    if f: print(f"FLAG from PNG appended data {name}:", f); return
                # LSB try
                lsbt = png_pixels_lsb(payload)
                if lsbt:
                    f = find_flag_in_text(lsbt) or pipeline_decode(lsbt)
                    if f: print(f"FLAG from PNG LSB {name}:", f); return
            else:
                # non-PNG payload: scan as text
                s = payload.decode("latin1", errors="ignore")
                f = find_flag_in_text(s) or pipeline_decode(s)
                if f: print(f"FLAG from {name} in {os.path.basename(zp)}:", f); return
    print("Flag belum ditemukan. Coba jalankan ulang setelah menambah heuristik atau periksa manual artefak yang dihasilkan.")

if __name__ == "__main__":
    main()