# 1.```1. კომენტარის სახით ახსენით თუ როგორ მუშაობს, რა შედეგი გამოაქვს და რა სიმბოლობით შედგება გაკვეთილზე ნასწავლი მათემატიკური ოპერაცები

#1.მიმატება (+) ზრდის რიცხვებს
#print(10+5) #result=15

#2.გამოკლება (-) ამცირებს რიცხვებს
#print(10-5) #result=5

#3.გამრავლება (*) ამრავლებს რიცხვებს
#print(10*5)  result=50

#4.გაყოფა (/) ყოფს რიცხვებს
#print(10/5) result=2.5 (float) ათწილადთან

#5.მთელი ნაწილის გამოყოფა (//) ყოფს და ტოვებს მხოლოდ განაყოფის მთელ ნაწილს
#print(10//3) #result=3


#6.ნაშთიანი გაყოფა (%) აბრუნებს გაყოფის შემდეგ დარჩენილ ნაშთს
#print(10%3) #result=1 10 ში 3 3_ჯერ მოთავსდება მივიღებთ 9_ს და დარჩება 1 ნაშთი.

#7.ახარისხება (**)
#print(2**3) result=8 (2_ის კუბი)


#2.2. მომხმარებელს შემოაყვანინეთ რიცხვი და დაპრინტეთ მისი კვადრატი და კუბი
num=float(input("enter your number:"))
square=num**2
cube=num**3
print(square)
print(cube)



# 3.მომხმარებელს შემოაყვანინეთ ორი რიცხვი და შეასრულეთ ყველა მათემატიკური ოპერაცია

num1=int(input("enter first number (num1):"))
num2=int(input("enter second number(num2):"))

print(f"ჯამი(+){num1+num2}")
print(f"სხვაობა(-){num1-num2}")
print(f"გამრავლება(*){num1*num2}")
print(f"განაყოფი(/):{num1/num2}")
print(f"მთელი განაყოფი(//):{num1//num2}")
print(f"ნაშთი(%):{num1%num2}")
print(f"ახარისხება(**):{num1**num2}")



#4. მაღაზიაში არის გარკვეული რაოდენობის კანფეტი, ერთ ყუთში 12 კანფეტი ეტევა
#მომხმარებელს შემოაყვანინეთ კანფეტების რაოდენობა და გამოთვალეთ:
#A. სულ რამდენი ყუთი გაივსება
#B. რამდენი კანფეტი დარჩება


total_candies=int(input("enter total candies"))
full_boxes=total_candies//12
remaining_candies = total_candies % 12
print(f"A. full boxes: {full_boxes}")
print(f"B. full boxes: {remaining_candies}")


#5. მომხმარებელს შემოაყვანინეთ წუთების რაოდენობა და გამოთვალეთ:

#A. რამდენი სრული საათია

#B. რამდენი წუთი დარჩა

#მაგალითად: 135წთ --> 2 სრული საათი და 15 წუთი

total_minutes=int(input("enter total_minutes"))

hours=total_minutes//60
minutes=total_minutes%60

print(f"{total_minutes}წთ {hours} საათი და {minutes} წუთი")