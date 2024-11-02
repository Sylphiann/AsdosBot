VOCAB_GET = { "a" : "aga", "i" : "igi", "u" : "ugu", "e" : "ege", "o" : "ogo" }

def getG (ch: str) -> str:
    if ch in VOCAB_GET:
        return VOCAB_GET[ch]
    return ch

def turnToG (text: str) -> str:
    """ Translate a String into the G language """
    res = []
    for char in text:
        res.append(getG(char))
    return "".join(res)

if __name__ == "__main__":
    print(turnToG("halo bumi"))