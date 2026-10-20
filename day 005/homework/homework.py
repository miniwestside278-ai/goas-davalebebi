#1.მომხმარებელს შემოაყვანინეთ: სახელი, გვარი და ასაკი. შეინახეთ ცვლადებში და დაპრინტეთ: "Hello, my name is [სახელი] [გვარი] and i am [ასაკი] years old"

name=input("name")
last_name=input("last_name")
age=input("my age")

print(f"Hello, my name is {name} {last_name} and i am {age} years old")

#2. მომხმარებელს შემოაყვანინეთ რამდენიმე პროდუქტის ფასები, შეინახეთ ცვლადებში, შექმენით ერთი ცვლადი total და გამოთვალეთ სულ რამდენი იქნება პროდუქტების ღირებულება საბოლოოდ დაპრინტეთ: "Total: [ჯამი]"

price1 = float(input("შეიყვანეთ პირველი პროდუქტის ფასი: "))
price2 = float(input("შეიყვანეთ მეორე პროდუქტის ფასი: "))
price3 = float(input("შეიყვანეთ მესამე პროდუქტის ფასი: "))

total = price1 + price2 + price3
print(f"Total: {total}")


#3. მომხმარებელს შემოაყვანინეთ ასაკი და წლების რაოდენობა, გამოთვალეთ თუ რამდენი წლის იქნება ის მომავალში და დაპრინტეთ: "In [წლები] years you will be [ჯამი] years old"

age = int(input("შეიყვანეთ თქვენი ასაკი: "))
years = int(input("შეიყვანეთ წლების რაოდენობა: "))

total_age = age + years
print(f"In {years} years you will be {total_age} years old")


#4. მომხმარებელს შემოაყვანინეთ გავლილი მანძილი კილომეტრებში და დახარჯული დრო და გამოთვალეთ საშვალო სიჩქარე: მანძილი / დრო

distance = int(input("შეიყვანეთ გავლილი მანძილი (კმ): "))
time = int(input("შეიყვანეთ დახარჯული დრო (სათი): "))

speed = distance / time
print(f"საშუალო სიჩქარე: {speed} კმ/სთ")

#5. მანქანა 100 კილომეტრზე 8 ლიტრ ბენზინს მოიხმარს, მომხმარებელს შემოაყვანინეთ გასავლელი მანძილი კილომეტრებში და გამოთვალეთ რამდენი ლიტრი საწვავი დასჭირდება მანქანას: (მანძილი x 8) / 100 

distance = int(input("შეიყვანეთ გასავლელი მანძილი (კმ): "))

fuel = (distance * 8) / 100
print(f"საჭირო საწვავის რაოდენობა: {fuel} ლიტრი")


#6. საწვავის ხარჯისა და ღირებულების გამოთვლა

distance = float(input("შეიყვანეთ გასავლელი მანძილი (კმ): "))
consumption = float(input("შეიყვანეთ საწვავის ხარჯი ყოველ 100კმ-ზე: "))
price_per_liter = float(input("შეიყვანეთ ერთი ლიტრი საწვავის ფასი ლარებში: "))

fuel = (distance * consumption) / 100
total_cost = fuel * price_per_liter

print(f"A. დახარჯული საწვავი: {fuel} ლიტრი")
print(f"B. საწვავის ღირებულება: {total_cost}₾")

#7. კვირის ხელფასის გამოთვლა

hourly_wage = float(input("შეიყვანეთ საათობრივი ანაზღაურება ლარებში: "))
hours_worked = float(input("შეიყვანეთ კვირის განმავლობაში ნამუშევარი საათების რაოდენობა: "))

weekly_salary = hourly_wage * hours_worked
print(f"ერთი კვირის ხელფასი: {weekly_salary}₾")


#8. თანხის განაწილება ადამიანებზე

total_amount = float(input("შეიყვანეთ თანხის რაოდენობა ლარებში: "))
people_count = int(input("შეიყვანეთ ადამიანების რაოდენობა: "))

per_person = total_amount // people_count
remainder = total_amount % people_count

print(f"თითოეულ ადამიანს შეხვდება: {per_person}₾")
print(f"ნაშთი (რაც დარჩება): {remainder}₾")

#9. ფასდაკლებისა და საბოლოო ფასის გამოთვლა

original_price = float(input("შეიყვანეთ პროდუქტების საწყისი ფასი: "))
discount_percent = float(input("შეიყვანეთ ფასდაკლების პროცენტი: "))

discount_amount = (original_price * discount_percent) / 100
final_price = original_price - discount_amount

print(f"ფასდაკლების თანხა: {discount_amount}₾")
print(f"საბოლოო ფასი: {final_price}₾")

#10. წიგნის წასაკითხად საჭირო დღეების გამოთვლა

total_pages = int(input("შეიყვანეთ წიგნის გვერდების რაოდენობა: "))
pages_per_day = int(input("შეიყვანეთ რამდენ გვერდს კითხულობს ერთ დღეში: "))

# ვიყენებთ კალმოვან გაყოფას, რათა მივიღოთ მთლიანი დღეების რაოდენობა
days_needed = total_pages // pages_per_day
if total_pages % pages_per_day != 0:
    days_needed += 1  # თუ ნაშთი დარჩა, დამატებითი 1 დღეც დასჭირდება

print(f"წიგნის წასაკითხად დასჭირდება: {days_needed} დღე")

