def is_number(chr: str):
    diff = chr - '0'
    return diff >= 0 and diff <= 9