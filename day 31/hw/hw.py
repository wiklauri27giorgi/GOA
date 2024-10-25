num = int(input("შეიყვანეთ რიცხვი:"))

if num == 0:
    print("0-ის ტოლია")
elif num % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")

nums = [] 

for i in range(10):
    num = int(input(f"შეიქვანეთ რიცხვი"))


results = []


for num in nums:
    if num == 0:
        results.append(0)
    elif num % 2 == 0:
        results.append("ლუწია")
    else:
        results.append("კენტია")


print(results)
 
fruitlist = [
    "banana",
    "apple",
    "mango",
    "chery",
    "blueberry",
    "dragonfruit",
    "berry",
    "grape",
    "orange",
    "strawbery"
]

print(f"ეს არის ხლის სია {fruitlist}")


new = input("რომელი ხილი გსურთ დაამატოთ სიაში")
indexing = int(input(f"სად გსურთ რომ დაამატოთ {fruitlist} (0 - {len(fruitlist)})"))

fruitlist.insert(indexing, new)


print(f"ახალი სია {fruitlist}")

numbers = [34, 12, 89, 7, 56, 23, 45, 90, 3, 78]


numbers.remove(min(numbers))


numbers.insert(0, 100)  
numbers.append(100)      


numbers.sort()


print(numbers)
shopping_list = ["ბანანი", "ვაშლი", "მაიმუნი", "შაურმა"]

num_items = int(input("რამდენი ტელეფონის მოდელის დამატება გსურთ სიაში? "))

for i in range(num_items): 
    item = input("შეიტანეთ ტელეფონის მოდელი: ")
    shopping_list.append(item)

print("საყიდლების სია:", shopping_list)


movies = ["Inception", "The Matrix", "Interstellar", "The Godfather", "Pulp Fiction"]

while True:
    action = input("გთხოვთ აირჩიოთ: 'დამატება', 'წაშლა' ან 'quit': ").strip().lower()
    
    if action == "quit":
        break
    elif action == "დამატება":
        neWmovie = input("შეიტანეთ ახალი ფილმის სახელი: ")
        movies.append(neWmovie)
    elif action == "წაშლა":
        Mtr = input("შეიტანეთ ფილმის სახელი, რომელიც უნდა წაიშალოს: ")
        if Mtr in movies:
            movies.remove(Mtr)
        else:
            print("ეს ფილმი არ არის სიაში.")
    else:
        print("გთხოვთ აირჩიოთ 'დამატება', 'წაშლა' ან 'quit'.")

print("ფილმების საბოლოო სია:", movies)num = int(input("შეიყვანეთ რიცხვი:"))

if num == 0:
    print("0-ის ტოლია")
elif num % 2 == 0:
    print("ლუწია")
else:
    print("კენტია")

nums = [] 

for i in range(10):
    num = int(input(f"შეიქვანეთ რიცხვი"))


results = []


for num in nums:
    if num == 0:
        results.append(0)
    elif num % 2 == 0:
        results.append("ლუწია")
    else:
        results.append("კენტია")


print(results)
 
fruitlist = [
    "banana",
    "apple",
    "mango",
    "chery",
    "blueberry",
    "dragonfruit",
    "berry",
    "grape",
    "orange",
    "strawbery"
]

print(f"ეს არის ხლის სია {fruitlist}")


new = input("რომელი ხილი გსურთ დაამატოთ სიაში")
indexing = int(input(f"სად გსურთ რომ დაამატოთ {fruitlist} (0 - {len(fruitlist)})"))

fruitlist.insert(indexing, new)


print(f"ახალი სია {fruitlist}")

numbers = [34, 12, 89, 7, 56, 23, 45, 90, 3, 78]


numbers.remove(min(numbers))


numbers.insert(0, 100)  
numbers.append(100)      


numbers.sort()


print(numbers)
shopping_list = ["ბანანი", "ვაშლი", "მაიმუნი", "შაურმა"]

num_items = int(input("რამდენი ტელეფონის მოდელის დამატება გსურთ სიაში? "))

for i in range(num_items): 
    item = input("შეიტანეთ ტელეფონის მოდელი: ")
    shopping_list.append(item)

print("საყიდლების სია:", shopping_list)


movies = ["Inception", "The Matrix", "Interstellar", "The Godfather", "Pulp Fiction"]

while True:
    action = input("გთხოვთ აირჩიოთ: 'დამატება', 'წაშლა' ან 'quit': ").strip().lower()
    
    if action == "quit":
        break
    elif action == "დამატება":
        neWmovie = input("შეიტანეთ ახალი ფილმის სახელი: ")
        movies.append(neWmovie)
    elif action == "წაშლა":
        Mtr = input("შეიტანეთ ფილმის სახელი, რომელიც უნდა წაიშალოს: ")
        if Mtr in movies:
            movies.remove(Mtr)
        else:
            print("ეს ფილმი არ არის სიაში.")
    else:
        print("გთხოვთ აირჩიოთ 'დამატება', 'წაშლა' ან 'quit'.")

print("ფილმების საბოლოო სია:", movies)