def sayhello():
    print("გამარჯობა!")


def sumtwonumbers(a, b):
    return a + b

def calculateage(birth_year):
    current_year = 2024
    return current_year - birth_year


def multiply(x, y):
    return x * y


def repeat_twice(word):
    return word * 2


if __name == "__main":

    say_hello()


    result_sum = sum_two_numbers(5, 7)
    print(f"ჯამი: {result_sum}")


    age = calculate_age(1990)
    print(f"თქვენი ასაკი: {age} წლის.")


    result_multiply = multiply(3, 4)
    print(f"ნამრავლი: {result_multiply}")


    repeated_word = repeat_twice("გამარჯობა")
    print(f"გამეორებული სიტყვა: {repeated_word}")