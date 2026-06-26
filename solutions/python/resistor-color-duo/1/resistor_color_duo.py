COLOR_LIST=["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    return int("".join(str(COLOR_LIST.index(colors[c])) for c in range(2)))