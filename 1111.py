from steganocryptopy.steganography import Steganography

Steganography.generate_key("")
secret = Steganography.encrypt("key.key","img.png", "secret.txt")
secret.save("secret4.png")
result = Steganography.decrypt("key.key", "secret4.png")
print(result)