import codecs

def rot13(message):
    list_chars = list()
    list_rot13 = list()
    for letter in message:
        for character in letter:
            if (ord(character) >= 65 and ord(character) <= 90) or (ord(character) >= 97 and ord(character) <= 122):
                code_ascii = ord(character)
                code_ascii = rotar13(code_ascii)
                list_chars.append(chr(code_ascii))
            else:
                list_chars.append(character)
                list_rot13.append("".join(list_chars))
    return codecs.encode(message,"rot13")
    #return "".join(list_chars)
    #ebqevtb
    #ebqevtb

def rotar13(c):

    if c >= 97 and c <= 122:
        if(c < 110):
            return c + 13
        else:
            for i in range(0,13):
                if(c + 1) > 122:
                    c = 97
                else:
                    c = c + 1
            return c


    if(c < 78):
        return c + 13
    else:
        for i in range(0,13):
            if(c + 1) > 90:
                c = 65
            else:
                c = c + 1
    return c


print(rot13("rodrigo"))
