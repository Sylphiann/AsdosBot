VOCAL_GET = { "a" : "aiden", "i" : "isfir", "u" : "usfur", "e" : "eiden", "o" : "osfor",
             "A" : "Aiden", "I" : "Isfir", "U" : "Usfur", "E" : "Eiden", "O" : "Osfor" }

def getVocal (ch: str) -> str:
    if ch in VOCAL_GET:
        return VOCAL_GET[ch]
    return ch

def raidenify (text: str):
    if len(text) == 0:
        return ""

    elif text[0] in VOCAL_GET:
        return getVocal(text[0]) + raidenify(text[1:])
    
    elif text.startswith("ng") and len(text) > 2:
        if text[2] not in VOCAL_GET:
            return "streng" + raidenify(text[2:])
    
    elif text[0].isalpha() and text[0] not in VOCAL_GET and len(text) > 1:
        if text[1] not in VOCAL_GET:
            return f"{text[0]}es" + raidenify(text[1:])

    return text[0] + raidenify(text[1:])

if __name__ == "__main__":
    print(raidenify("Tendang? tDen Bola'ka Kloban_g [YOO!]"))