def is_number(chr: str):
    diff = ord(chr) - 48
    return diff >= 0 and diff <= 9