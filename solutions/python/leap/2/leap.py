'''Checking whether the given year is a leap year or not'''
is_leap=True
def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return is_leap
            else:
                return not(is_leap)
        else:
            return is_leap
    else:
        return not(is_leap)