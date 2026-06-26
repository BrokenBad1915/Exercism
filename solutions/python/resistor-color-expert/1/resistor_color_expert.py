COLORS=["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
TOLERANCE={"grey":0.05, "violet":0.1, "blue":0.25, "green":0.5, "brown":1, "red":2, "gold":5, "silver":10}
def resistor_label(colors):
    prefix=""
    if len(colors)>=3:
        total_resistance=int("".join(str(COLORS.index(colors[c])) for c in range(len(colors[-3::-1]))))
        total_resistance=total_resistance*10**COLORS.index(colors[-2])
        current_tolerance=TOLERANCE[colors[-1]]
        if total_resistance/1000>=1:
            if total_resistance/1000000>=1:
                if total_resistance/1000000000>=1:
                    total_resistance=float(total_resistance/1000000000)
                    prefix="giga"
                else:
                    total_resistance=float(total_resistance/1000000)
                    prefix="mega"
            else:
                total_resistance=float(total_resistance/1000)
                prefix="kilo"
        total_resistance=int(total_resistance) if total_resistance.is_integer() else total_resistance
        return f"{total_resistance} {prefix}ohms ±{current_tolerance}%"
    else:
        total_resistance=int("".join(str(COLORS.index(colors[c])) for c in range(len(colors))))
        return f"{total_resistance} {prefix}ohms"
