import unicodedata
def Unicode_Con(char):
    unicode_code = f"U+{ord(char):04X}"
    character_name = unicodedata.name(char)
    return (f"The Unicode code point of '{char}' is {unicode_code}\nThe character name of '{char}' is '{character_name}'")
def Convert(unicode):
    unicode_code = int(unicode[2::],16)
    symbol = chr(unicode_code)
    return (f"The symbol for Unicode U+{unicode_code:04X} is '{symbol}'")
def encode(name):
    decimal=[]
    for x in name:
        decimal+=[hex(ord(x))[2::]]
    hexa=" ".join(decimal)
    return f"Encoded y-name is ({hexa}) in ASCII!"