def getG (ch: str) -> str:
    vocab = {
        "a" : "aga",
        "i" : "igi",
        "u" : "ugu",
        "e" : "ege",
        "o" : "ogo"
    }
    if ch in vocab:
        return vocab[ch]
    return ch

def turnToG (text: str) -> str:
    res = []
    for char in text:
        res.append(getG(char))
    return "".join(res)

def translateG (text: str) -> str:
    # TODO implement this
    pass

if __name__ == "__main__":
    print(turnToG("halo bumi"))