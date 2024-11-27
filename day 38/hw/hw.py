# 1

def calculate_sum(a, b):
    return a + b

# 2

def is_even(n):

    return n% 2 == 0

# 3

def greet_user(n):
    print(f"გამარჯობა, {n}")

# 4

def calculate_user_inputs():
    s = int(input("Enter first num: "))
    o = int(input("Enter seccond num: "))
    print(f"Sum: {s + o}")

# 5

def check_stage(n):
    if n> 5:
        return "შენ გადახვედი მეორე ეტაპზე"
    else:
        return "შენ არ გადახვედი შემდეგ ეტაპზე"