def line_up(name, number):
    unit="th"
    if number%10==1 and number%100!=11:
        unit="st"
    elif number%10==2 and number%100!=12:
        unit="nd"
    elif number%10==3 and number%100!=13:
        unit="rd"
    return f"{name}, you are the {number}{unit} customer we serve today. Thank you!"