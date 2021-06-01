def initials(phrase):
    words = phrase.split()
    character = ''.join(word[0] for word in words)
    return character.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS