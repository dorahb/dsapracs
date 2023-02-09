name = input("What is your name?:  ")
print("hello", name)

hrs = input("How many hours do you work per week?: ")
rate = input("How much are you paid per hour?: ")

hf = float(hrs)
rf = float(rate)

if hf > 40 :
  # print("Overtime due:", )
  reg = hf * rf
  otp = (hf - 40.0)*(rf*0.5)
  # print(reg,otp)
  pay= reg+otp

  
else:
  # print("Regular")
  pay = hf * rf

print("Your total pay is", pay)



