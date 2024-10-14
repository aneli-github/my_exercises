def string_int(txt):
    # here type(txt) could be used as well, but isinstance is faster
    if isinstance(txt, str) and txt.isnumeric():
        return int(txt)
    else:
        raise ValueError("Input must be numeric string.")


if __name__ == "__main__":
    # txt = "234"
    txt = "rewer"
    print(string_int(txt))
