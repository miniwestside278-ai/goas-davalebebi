#1. input_ არის შემავალი ინფორმაცია,იგი აძლევს საშუალებას მომხმარებელს შეიყვანოს ტერმინალში კონკრეტული მონაცემი.

#2. type casting_არის პროცესი,როდესაც ერთ მონაცემთა ტიპს ვაქცევთ სხვა ტიპად 

#3.stringi,integeri,floati,bool
#age=int("25")
#price=("10.5")
#text=str(100)
#print(5 > 3)   # გამოიტანს True (რადგან 5 მეტია 3-ზე - ჭეშმარიტია)
#print(10 == 2) # გამოიტანს False (რადგან 10 არ უდრის 2-ს - მცდარია)

#4. davaleba


#> (მეტია)

# < (ნაკლებია)

# == (უდრის)

# != (არ უდრის)

# >= (მეტია ან ტოლია)

# <= (ნაკლებია ან ტოლია)


#5. davaleba
num1=int(input("enter your number: "))
num2=int(input("enter your number: "))

print(num1>num2)
print(num1<num2)
print(num1==num2)
print(num1!=num2)
print(num1>=num2)
print(num1<=num2)


#6. davaleba

age=int(input("enter your age :"))

is_adult=age>=18
print("is he/she 18 or more :",is_adult)



#7. davaleba

speed = float(input("enter your speed (კმ/სთ): "))
distance = float(input("enter your distance (კმ): "))
given_time = float(input("enter your time (სთ): "))


actual_time = distance / speed

fits_in_time = actual_time <= given_time

print(f"to reach he/she will need: {actual_time} საათი")
print(f"will he/she fit in time?: {fits_in_time}")


#8. davaleba

price1=float(input("enter your number :"))
price2=float(input("enter your number :"))
price3=float(input("enter your number :"))

my_money=float(input("enter your money :"))

total_cost = price1 + price2 + price3

is_enough = my_money >= total_cost


print(f"total cost is: {total_cost}")
print(f"is money enough?: {is_enough}")


#9. davaleba

program_size=int(input("enter your number :"))
free_space=int(input("enter your number :"))

has_enough_space = free_space >= program_size

print(f"is free space enough?: {has_enough_space}")


#10. davaleba

math=float(input("enter your number :"))
history=float(input("enter your number :"))
physics=float(input("enter your number :"))

average_grade = (math + history + physics) / 3
exceeds_five = average_grade > 5

print(f"avereage grade is: {average_grade}")
print(f"exceeds five??: {exceeds_five}")

#ისეთი ნიშნები შევუყვანე იმის მერე აღარავის უნახავს მომხმარებელი.


#11. davaleba


# num1 = input("Enter first number: ")
# num2 = int(input("Enter second number: "))

# result = num1 + num2
# print(result)

#errori imitoa rom am kods aklia integeri an floati pirvel cvladshi.


# num1 = int(input("Enter first number: "))
# num2 = float(input("Enter second number: "))

# result = num1 - "5" * num2
# print(result)

#am kodshi result cvladshi 5 aris chasmuli brwyalebshi da errors amoagdebs.


#hours = input("Enter hours worked: ")
# rate = float(input("Enter hourly rate: "))
# bonus = input("Enter bonus: ")

# salary = hours * rate
# total = salary + bonus
# final_salary = total / "2"

# print(final_salary)

#pirvel da mesame cvladshi integeri an float aklia xolo final salary cvladshi 2 brwyalebshia.


#price = float(input("Enter product price: "))
# quantity = input("Enter quantity: ")
# discount = float(input("Enter discount percentage: "))

# subtotal = price + quantity
# discount_amount = subtotal * discount
# final_price = subtotal - "10"

# print(int(final_price))

#quantity cvladshi integeri an float aklia,final price cvladshi 10 brwyalebshia chasmuli,printshi kidev integeri ar wirdeba da zedmeti frchxilebia dasmuli


# num1 = int(input("Enter first number: "))
# num2 = input("Enter second number: ")
# num3 = float(input("Enter third number: "))

# total = num1 + num2
# average = total / num3
# remainder = average % "2"
# result = int(remainder + num1)

# print(result)

#remainder cvladshi 2 brwyalebshia chasmuli da result cvladshi integeri ar gvwirdeba.







#SWORI-------------------------------VERSIEBI




num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2
print(result)




num1 = int(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = num1 - 5 * num2
print(result)



hours = int(input("Enter hours worked: "))
rate = float(input("Enter hourly rate: "))
bonus = int(input("Enter bonus: "))

salary = hours * rate
total = salary + bonus
final_salary = total / 2

print(final_salary)


price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount = float(input("Enter discount percentage: "))

subtotal = price + quantity
discount_amount = subtotal * discount
final_price = subtotal - 10

print(final_price)



num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = float(input("Enter third number: "))

total = num1 + num2
average = total / num3
remainder = average % 2
result =(remainder + num1)

print(result)