menu = ["ბორში", "თევზი", "ფრანცუზული სენდვიჩი", "სალათი", "სუპი"]


choose = []

print("მენიუ:")
for index, item in enumerate(menu, start=1):
    print(f"{index}. {item}")


while True:
    choice = input("გთხოვთ აირჩიოთ პროდუქტის ნომერი (თუმცა 'დასრულება' რომ შეწყვეტოთ): ")

    if choice.lower() == 'დასრულება':
        break


        choice_index = int(choice) - 1
        if 0 <= choice_index < len(menu):
            choose.append(menu[choice_index])
            print(f"{menu[choice_index]} დაემატა სიაში.")
        else:
            print("შეცდომა: გთხოვთ აირჩიოთ სწორი ნომერი.")

        print("შეცდომა: გთხოვთ შეიყვანოთ ნომერი.")


print("თქვენი არჩეული საკვებია:", choose)

small_pets=("rabbit","hamster","sea pig")
big_pets=("dog","bear","lion")
print(small_pets+big_pets)