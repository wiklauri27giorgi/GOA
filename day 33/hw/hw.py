სახელი= "ლუკა ნინო ნიკა ლიზი"

სახელი1= სახელი.split()

for სახელი in სახელი1:
    print("გამარჯობა +" " +name}")
    name="gamarjoba"
    name2="gagimarjos"
    name=name.replace("a","#")
    name=name2.replace("g","*")


saying = input("თქვენი საყვარელი ანდაზა რა არის? ")


words = saying.split()


longest_word = max(words, key=len)
shortest_word = min(words, key=len)


print(f"ყველაზე დიდი სიტყვა: {longest_word}")
print(f"ყველაზე პატარა სიტყვა: {shortest_word}")


text = "i love python == True"


text_no_spaces = text.replace(" ", "")

print(text_no_spaces)



name = " i love html but its not progrramming language"

name = name.strip()


text_no_spaces = "ilovepyton==True"


name = name.replace(text_no_spaces, "")


reversed_name = name[::-1]


print(reversed_name)

names = ["luka", "nika ", "salome", "giorgi", "sofo"]


capital_names = [name.upper() for name in names]


print(capital_names)