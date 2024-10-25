def print_hello():
    print("გამარჯობა, მეგობრებო!")

print_hello()



def birthday(name):
    print(name + "დაბადებისდღეს გილოცავ")

birthday("guga")

def fav_color():
    print("წითელი")
fav_color()


def print_numbers():
    for i in range(1,101):
        print(i)
print_numbers()


def len_text(text):
    length = len(text)
    print(length)

len_text("გამარჯობა!")



def multiplication(six ,seven):
    print(six * seven)
multiplication(6,7)


def friends():
    friends_list = ["luka", "კოკა", " guga", "idk", "ნიკა"]
    for i in friends_list:
        print(i)
friends()