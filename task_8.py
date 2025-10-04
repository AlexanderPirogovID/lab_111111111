def shift_letter(ch, shift=3):
    if ch.isalpha():
        start = ord('A') if ch.isupper() else ord('a')
        return chr((ord(ch) - start + shift) % 26 + start)
    else:
        return ch

def caesar_cipher(text, shift=3):
    return ''.join(shift_letter(ch, shift) for ch in text)

s = "Hello, World!"
print(caesar_cipher(s))