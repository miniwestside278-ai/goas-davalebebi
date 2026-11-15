# davaleba 1.
# 1. and, or, not
# and: True მხოლოდ მაშინ, როცა ორივე პირობა True-ა
# or: True, თუ ერთი მაინც True-ა
# not: აბრუნებს მნიშვნელობას საპირისპიროდ
# პრიორიტეტი: not -> and -> or


# davaleba 2.

user=input("enter ur username :")
pasw=int(input("enter your password :"))

if user=="admin" and pasw=="admin123":
     print("login successful")
else:
     print("login unsuccesful")


# davaleba 3.

day=input("enter your week day :")

if day=="saturday" or day=="sunday":
       print("its the weekend")

else:
      print("its working day")


# davaleba 4.

paym=int(input("enter ur number :"))

if paym>=100 or paym<=500:
      print("you received 10% discount")

else:
      print("no discount available")



# davaleba 5.


temp=int(input("enter your temperature"))

if temp<0 or temp>35:
      print("extreame temperature!")

else:
      print("temperature is normal!")



# davaleba 6.

number = int(input("Enter a number: "))

if number % 3 == 0 or number % 5 == 0:
    print("Special number!")
else:
    print("Regular number!")

# davaleba 7.

# A. False
# B. True
# C. False
# D. True
# E. False