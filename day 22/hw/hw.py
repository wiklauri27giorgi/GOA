#შექმენი სია 10 წიგნის სახელით
book_list = [
    "tom soieris tavgadasavali",
    "kukaracha",
    "10000 kilometri wyal qvesh",
    "dzagli",
    "magdanas lurja",
    "xazarula",
    "deda",
    "boshebi",
    "didro",
    "patara princi"
]


favorite_book = "kukaracha"


try:
    index = book_list.index(favorite_book)
    print(f"The index of '{favorite_book}' is {index}.")
except ValueError:
    print(f"'{favorite_book}' is not in the list.")



cities_to_visit = [
    "Tokyo",
    "Paris",
    "New York",
    "Sydney",
    "Barcelona"
]


cities_to_visit.reverse()

print(cities_to_visit)

numbers = [1,2,3,4,5]
for number in numbers:
   result=number*2
   print(result)


fruits = ["apple", "banana", "orange"]


print(fruits)


 
numbers = [10, 20, 30, 40]


print(numbers[0])




cities = ["New York", "Paris", "Tokyo", "Sydney", "Barcelona"]


list_length = len(cities)


print("Number of elements in the list:", list_length)