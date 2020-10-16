from datetime import date

# Exercise 9

today = date.today()
born = date(2000,5,16)

timeTranscurred = (today.year-born.year) * 12 + today.month - born.month
print(f"The number of months transcurred since {born} is: {timeTranscurred}")