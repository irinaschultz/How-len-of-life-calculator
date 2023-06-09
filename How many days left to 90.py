# 🚨 code below 👇
age = input("What is your current age? ")
# 🚨 the code above 👆

#Write code below this line 👇
age_as_int=int(age)
years_remaining=90-age_as_int
days_left=years_remaining*365
weeks_remaining=years_remaining*52
months_remaining=years_remaining*12
print(f"You have {days_left} days, {weeks_remaining} weeks, and {months_remaining} months left.")
