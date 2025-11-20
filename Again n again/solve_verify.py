import base64
import binascii

def solve():
    encoded = "Vm0weE5GbFdWWGhUV0d4VlYwZG9WRll3Wkc5V1ZteHlXa1pPVjFadGVGcFpNRlpyVm1zeFYyTkljRmRpVkZab1ZrZHplRll5VGtkYVJtaG9UVmhDZVZkV1VrZFRNVnBYVjI1S2FWSnNjSEJXTUZWM1pVWmFjVk5xVW1oTlZYQjVWR3hhYjFWR1duVlJia0pYVFVkU1QxcFZXbXRXTVZaeVUyMTRVMkpXU2twV2JHUXdZekZXZEZOcmFGWmlSa3BoVm01d1JtUXhVblJsUjNSWFRWWmFlVmRyWkc5VWJGcHlZMFZ3VjJGcmJ6QlZla1pYVmpGa2NsWnNTbGRTTTAwMQ=="
    
    count = 0
    while True:
        try:
            decoded = base64.b64decode(encoded).decode('utf-8')
            print(f"Round {count+1}: {decoded[:50]}...")
            encoded = decoded
            count += 1
            if "CYBERLAB" in encoded:
                print(f"Flag found: {encoded}")
                break
        except (binascii.Error, UnicodeDecodeError):
            print("Decoding stopped.")
            break

if __name__ == "__main__":
    solve()
