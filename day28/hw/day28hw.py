# მომხმარებელს შემოატანინეთ სიტყვა
word = input("შეიყვანეთ სიტყვა: ")

# დაბეჭდეთ სიტყვა სხვადასხვა ფორმატში
print("ყველა პატარა ასო:", word.lower())
print("ყველა დიდი ასო:", word.upper())
print("პირველი ასო დიდი, დანარჩენი პატარა:", word.capitalize())
# მომხმარებელს შემოატანინეთ სამი წინადადება
sentence1 = input("შეიყვანეთ პირველი წინადადება: ")
sentence2 = input("შეიყვანეთ მეორე წინადადება: ")
sentence3 = input("შეიყვანეთ მესამე წინადადება: ")

# თითოეულზე გამოიყენეთ სხვადასხვა სტრინგის მეთოდი
print("პირველი წინადადება პატარა ასოებით:", sentence1.lower())
print("მეორე წინადადება დიდი ასოებით:", sentence2.upper())
print("მესამე წინადადება პირველი ასო დიდი, დანარჩენი პატარა:", sentence3.capitalize())
# შეინახე შენი სახელი ცვლადში
my_name = "YourName"  # ჩაწერე შენი სახელი

# მომხმარებელს შეეკითხე თავისი სახელი
user_name = input("შეიყვანეთ თქვენი სახელი: ")

# შეადარე სახელები
if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names.")
    # შეინახე წინადადება ცვლადში
    sentence = input("შეიყვანეთ წინადადება: ")

    # მხოლოდ პირველი სიტყვა იყოს დიდი ასოთი, დანარჩენი პატარა
    formatted_sentence = sentence.capitalize()

    # დაბეჭდე შედეგი
    print("ფორმატირებული წინადადება:", formatted_sentence)
    # სტრინგის მეთოდები და მათი განმარტებები:

    # 1. lower() - აბრუნებს სტრინგს პატარა ასოებით.
    # მაგალითი:
    example = "HELLO"
    print(example.lower())  # შედეგი: "hello"

    # 2. upper() - აბრუნებს სტრინგს დიდი ასოებით.
    # მაგალითი:
    example = "hello"
    print(example.upper())  # შედეგი: "HELLO"

    # 3. capitalize() - სტრინგის პირველი ასო ხდება დიდი, დანარჩენი პატარა.
    # მაგალითი:
    example = "hello world"
    print(example.capitalize())  # შედეგი: "Hello world"

    # 4. title() - სტრინგის თითოეული სიტყვის პირველი ასო ხდება დიდი.
    # მაგალითი:
    example = "hello world"
    print(example.title())  # შედეგი: "Hello World"

    # 5. strip() - აშორებს სტრინგის დასაწყისსა და ბოლოში არსებულ ცარიელ ადგილებს ან მითითებულ სიმბოლოებს.
    # მაგალითი:
    example = "  hello  "
    print(example.strip())  # შედეგი: "hello"

    # 6. lstrip() - აშორებს სტრინგის დასაწყისში არსებულ ცარიელ ადგილებს ან მითითებულ სიმბოლოებს.
    # მაგალითი:
    example = "  hello"
    print(example.lstrip())  # შედეგი: "hello"

    # 7. rstrip() - აშორებს სტრინგის ბოლოში არსებულ ცარიელ ადგილებს ან მითითებულ სიმბოლოებს.
    # მაგალითი:
    example =