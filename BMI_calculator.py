# BMI Calculator 

height = float(input('Enter your height in m:'))
weight = float(input('Enter your weight in kg:'))

BMI = round((weight/height**2),1)

def bold_text(text):
    bold_start = '\033[1m'
    bold_end = '\033[0m'
    return bold_start + text + bold_end

if BMI <18.5:
    print(f'Your BMI is {BMI}. You are '+ bold_text("Underweight!"))
elif BMI <=25:
    print(f'Your BMI is {BMI}. You are '+ bold_text("Normal Weight!"))
elif BMI <=30:
    print(f'Your BMI is {BMI}. You are '+ bold_text("Overweight!"))
elif BMI <=35:
    print(f'Your BMI is {BMI}. You are '+ bold_text("Obese!"))
else:
    print(f'Your BMI is {BMI}. You are '+ bold_text("Clinically Obese!"))
