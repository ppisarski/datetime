import datetime


def monthrange(year, month):
    first_day = 1
    # get close to the end of the month, and add 4 days 'over'
    next_month = datetime.date(year, month, 28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month,
    # or the previous day of the first of next month
    last_day = (next_month - datetime.timedelta(days=next_month.day)).day
    return first_day, last_day


if __name__ == "__main__":
    for month in range(1, 13):
        print(month, monthrange(2012, month))
