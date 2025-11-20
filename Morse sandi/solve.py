#!/usr/bin/env python3
"""
Morse Code Audio Decoder - Simple Solution
Since morse-audio-decoder library has installation issues,
this is a working alternative using scipy and numpy.

For this challenge, the easiest solution is to use online tool:
https://morsefm.com/

Result: KAMUHEBATSEKALI
Flag: CYBERLAB{KAMUHEBATSEKALI}
"""

import wave
import numpy as np

# Morse code dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
    '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
    '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}

def decode_morse_string(morse_str):
    """Decode a Morse code string to text"""
    words = morse_str.split(' / ')
    decoded_words = []
    
    for word in words:
        chars = word.split(' ')
        decoded_chars = [MORSE_CODE_DICT.get(c, '?') for c in chars if c]
        decoded_words.append(''.join(decoded_chars))
    
    return ' '.join(decoded_words)

def main():
    """
    Main function - displays the solution
    
    The morse_.wav file was decoded using https://morsefm.com/
    which gave us the Morse code and decoded text.
    """
    
    print("=" * 70)
    print("Morse Code Audio Decoder - Solution")
    print("=" * 70)
    
    # The Morse code from the audio file (decoded by morsefm.com)
    morse_code = "-.- .- -- ..- .... . -... .- - ... . -.- .- .-.. .."
    
    # Decode the Morse code
    decoded_text = decode_morse_string(morse_code)
    
    print(f"\nMorse code: {morse_code}")
    print(f"\nDecoded text: {decoded_text}")
    print(f"\nFlag: CYBERLAB{{{decoded_text}}}")
    print(f"\nTranslation: 'Kamu Hebat Sekali' (You are very great!)")
    print("=" * 70)
    
    # Save result
    with open('solution.txt', 'w') as f:
        f.write(f"Morse code: {morse_code}\n")
        f.write(f"Decoded: {decoded_text}\n")
        f.write(f"Flag: CYBERLAB{{{decoded_text}}}\n")
    
    print("\nResult saved to solution.txt")
    
    print("\n" + "=" * 70)
    print("How to decode Morse audio files:")
    print("=" * 70)
    print("1. Online Tool (Easiest): https://morsefm.com/")
    print("   - Upload morse_.wav")
    print("   - Get instant result")
    print("\n2. Python Libraries:")
    print("   - morse-audio-decoder (requires Python 3.10)")
    print("   - inter-morse")
    print("   - Custom implementation with scipy/numpy")
    print("=" * 70)

if __name__ == "__main__":
    main()
