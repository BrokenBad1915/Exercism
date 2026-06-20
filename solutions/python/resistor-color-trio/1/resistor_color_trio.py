'''Calculating total resistance of resistors'''
COLORS=["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
def label(colors):
    prefix=""
    total_resistance=int("".join(str(COLORS.index(colors[c])) for c in range(2)))
    if len(colors)>=3:
        total_resistance=total_resistance*10**COLORS.index(colors[2])
        if total_resistance/1000>=1:
            if total_resistance/1000000>=1:
                if total_resistance/1000000000>=1:
                    total_resistance=int(total_resistance/1000000000)
                    prefix="giga"
                else:
                    total_resistance=int(total_resistance/1000000)
                    prefix="mega"
            else:
                total_resistance=int(total_resistance/1000)
                prefix="kilo"
        return f"{total_resistance} {prefix}ohms"