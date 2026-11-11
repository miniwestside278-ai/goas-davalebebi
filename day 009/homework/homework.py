# 1. კომენტარის სახით, თქვენი სიტყვებით ახსენით როგორ მუშაობს if else-ი
# if-else პირობითი ოპერატორი გამოიყენება პროგრამაში გადაწყვეტილებების მისაღებად. 
# 'if' ამოწმებს მოცემულ პირობას: თუ ის ჭეშმარიტია (True), სრულდება 'if' ბლოკში 
# მოცემული კოდი. წინააღმდეგ შემთხვევაში, თუ პირობა მცდარია (False), მუშაობა 
# გადადის და სრულდება 'else' ბლოკში არსებული კოდი.


# 2. მომხმარებელს შემოაყვანინეთ რიცხვი და შეამოწმეთ ეს რიცხვი ლუწია თუ კენტი
number = int(input("enter your number: "))

if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


# 3. მომხმარებელს შემოაყვანინეთ სრული გადასახადი და თუ ეს რიცხვი 100-ზე მეტია მიეცით 10%-იანი ფასდაკლება
total_amount = int(input("enter your number: "))

if total_amount > 100:
    discounted_price = total_amount * 0.9  # 10%-იანი ფასდაკლება (თანხის 90%)
    print(f"got 10% discount! new discount: {discounted_price}")
else:
    print("No discount!")


# 4. მომხმარებელს შემოაყვანინეთ ტემპერატურა და შეამოწმეთ, თუ ტემპერატურა 25-ზე მეტია
temperature = float(input("enter your number: "))

if temperature > 25:
    print("It's hot outside!")
else:
    print("It's not hot outside!")


# 5. მომხმარებელს შემოაყვანინეთ ორი რიცხვი და შეადარეთ რომელი უფრო მეტია
num1 = int(input("enter your number : "))
num2 = int(input("enter your number : "))

if num1 > num2:
    print(f"first number is more ({num1}) then second .")
else:
    print(f"second number is more ({num2}) then first.")
