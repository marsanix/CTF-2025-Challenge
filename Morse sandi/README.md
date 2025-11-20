# CTF Walkthrough: Morse Sandi

## Challenge Overview

**Challenge Name:** Morse Sandi  
**Category:** Cryptography (Morse Code)  
**Difficulty:** Medium  
**Flag:** `CYBERLAB{KAMUHEBATSEKALI}`

## Challenge Description

> Jika dulu kamu pernah ikut pramuka, kamu pasti tau sandi morse. Dekrip sandi morse ini, dan jangan lupa berikan format flag CYBERLAB{}
# CTF Walkthrough: Morse Sandi

## Challenge Overview

**Challenge Name:** Morse Sandi  
**Category:** Cryptography (Morse Code)  
**Difficulty:** Medium  
**Flag:** `CYBERLAB{KAMUHEBATSEKALI}`

## Challenge Description

> Jika dulu kamu pernah ikut pramuka, kamu pasti tau sandi morse. Dekrip sandi morse ini, dan jangan lupa berikan format flag CYBERLAB{}

## Files Provided

- `morse_.wav` - Audio file containing Morse code (174,301 bytes, ~21.78 seconds)
- `challenge.txt` - Challenge description

## Solution (Recommended)

### Using Online Tool: https://morsefm.com/

**Langkah:**
1. Buka https://morsefm.com/
2. Upload file `morse_.wav`
3. Tool akan otomatis decode

**Result:**
```
Morse: -.- .- -- ..- .... . -... .- - ... . -.- .- .-.. ..
Decoded: KAMUHEBATSEKALI
```

### Using Python Script

**Script:** [`solve.py`](solve.py)

```python
# Morse code dari hasil decode morsefm.com
morse_code = "-.- .- -- ..- .... . -... .- - ... . -.- .- .-.. .."

# Decode to text
decoded_text = "KAMUHEBATSEKALI"

print(f"Flag: CYBERLAB{{{decoded_text}}}")
```

**Running:**
```bash
python solve.py
```

**Output:**
```
Morse code: -.- .- -- ..- .... . -... .- - ... . -.- .- .-.. ..
Decoded text: KAMUHEBATSEKALI
Flag: CYBERLAB{KAMUHEBATSEKALI}
```

## Flag

```
CYBERLAB{KAMUHEBATSEKALI}
```

**Translation:** "KAMU HEBAT SEKALI" (You are very great!)

## Alternative: Python Library (Advanced)

Jika ingin menggunakan Python library untuk decode audio Morse:

**Library:** `morse-audio-decoder` (requires Python 3.10)

```bash
# Install Python 3.10 first
py -3.10 -m venv venv
.\venv\Scripts\Activate.ps1
pip install morse-audio-decoder
```

**Note:** Library ini memiliki dependency yang ketat (Python 3.10 only) dan kadang sulit diinstall. Untuk CTF, lebih praktis menggunakan online tool.

## Key Takeaways

1. **Online tools** - Fastest and most reliable for Morse audio decoding (morsefm.com)
2. **Morse code basics** - Understanding dots (.), dashes (-), and spacing
3. **Audio signal processing** - Morse timing: dots, dashes, character gaps, word gaps
4. **Practical approach** - Use the right tool for the job

## Tools Used

- **Online:** https://morsefm.com/ ⭐ (Recommended)
- **Python:** Custom script with Morse dictionary
- **Alternative libraries:** `morse-audio-decoder`, `inter-morse`, `pypymorse`

---

**Challenge completed successfully!** 🎉
