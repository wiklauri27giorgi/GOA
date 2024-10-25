product_list = [
    {"name": "ბანანი", "price": 1.00},
    {"name": "საცხოვრებელი ქათამი", "price": 3.50},
    {"name": "რძე", "price": 0.80},
    {"name": "პური", "price": 1.20},
    {"name": "ფუძის ცხიმი", "price": 2.00}
]


product_list.reverse()
print("ატრიალებული სია:", product_list)


reversed_list = product_list[::-1]
print("ატრიალებული სია (slicing):", reversed_list)



def decrees_calc(a, b):

    result = a - b
    print("ერთმნიშვნელოვნება:", result)


decrees_calc(10, 5)
decrees_calc(20, 8) 
decrees_calc(15, 3)