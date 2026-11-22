# # davaleba 1.

age=int(input("enter your age :"))

if age<18:
    print("you are minor")

elif age<=64:
    print("you are an adult")

else:
   print("you are senior")

# davaleba 2.

num1=int(input("enter your number :"))
num2=int(input("enter your number :"))

if num1>num2:
  print("num1>num2")

elif num1<num2:
   print("num2>num1")

elif num1==num2:
   print("num1==num2")


# davaleba 3.

num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
operacia=input("enter your operacia (+, -, *, /): ")

if operacia == "+":
    print("result:", num1 + num2)

elif operacia =="-":
    print("result:", num1-num2)

elif operacia=="*":
    print("result:",num1*num2)

elif operacia=="/":
    print("result:",num1/num2)

else:
    print("unknown operacia")

# davaleba 4.


temp = float(input("enter temp: "))
weather = input("enter weather (sunny, rainy, snowy): ")

if temp> 25 and weather == "sunny":
    print("Perfect weather for a walk!")
elif weather == "rainy" or weather == "snowy":
    print("Bad weather for a walk!")
else:
    print("Normal weather!")


# davaleba 5.

user = input("enter user: ")
passw = input("enter pass: ")
age = int(input("enter age: "))

if user == "admin" or passw == "Adm1n_123":
    print("Access denied!")
elif age >= 18:
    print("Full access granted!")
else:
    print("Limited access!")