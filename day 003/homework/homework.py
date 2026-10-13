# 1.მომხმარებელს input-ის დახმარებით კითხეთ სახელი შეინახეთ ცვლადში და print-ის დახმარებით მიესალმეთ: "Hello, სახელი"

name = input("Enter your name: ")
print(f"Hello, {name}")


# 2.მომხმარებელს კითხეთ ასაკი შეინახეთ ცვლადში და გამოთვალეთ თუ რამდენი წლის იქნება ის 5 წლის შემდეგ

age=int(input("enter your age"))
future_age=age+5
print(f"in 5 years i will be {future_age} old")

# 3.მომხმარებელს შემოაყვინენთ დღეების რაოდენობა და გადააქციეთ საათებად

days = 25
hours = days * 24
print(f"{days} days equals {hours} hours")



# 4.მომხმარებელს კითხეთ ორი რიცხვი და შეინახეთ ცვლადებში: num1, num2 გამოთვალეთ მათი: ჯამი, სხვაობა, ნამრავლი და განაყოფი

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print(f"Sum: {addition}")
print(f"Difference: {subtraction}")
print(f"Product: {multiplication}")

if num2 != 0:
    division = num1 / num2
    print(f"Division: {division}")
else:
    print("Cannot divide by zero!")




    # 5.მომხმარებელს შემოაყვანინეთ 3 ან მეტი რიცხვი და გამოთვალეთ მათი საშვალო არითმეტიკული 


    
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))


average = (num1 + num2 + num3) / 3

print(f"The average is: {average}")