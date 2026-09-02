from math import floor

def translate_days_to_age(all_days):
    years = floor(all_days/365)
    months = floor((all_days - years*365)/30)
    days = all_days - years*365 - months*30
    age = {
    'years': years,
    'months': months,
    'days': days
    }
    return age

print("Введите ваш возраст в днях:")
age_in_days = int(input())

print(translate_days_to_age(age_in_days))