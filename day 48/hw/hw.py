def rndmun(lst):
    for i in range(len(lst)):
        lst[i] = (i % 50) + 1  
    return lst

lst = [None, None, None]
print(rndmun(lst))

# 2 

def choose_random_animal(anml):
    num = 0  
    print(f"თქვენი საყვარელი ცხოველი არის: {anml[num]}")

anml = ["მაიმუნი", "ლიომი", "გველი-მგელი", "დათვი"]
choose_random_animal(anml)

# 3 

def rdnsymbl(text):
    smbl = ['#', '*', '%']
    smbl = smbl[0]  
    nm = 5  
    return f"{smbl}{nm}{smbl}{text}"

txt = "hi"
print(rdnsymbl(txt))

# 4

def trnflstelmnt(lst):
    for i in lst:
        print(f"მიმდინარე ელემენტი: {i}")

lst = [1, 2, 3, 4]
trnflstelmnt(lst)

# 5
def rndmsprt():
    sprts = []
    for i in range(3):  
        sprt = input(f"მიუთითეთ {i+1} საყვარელი სპორტი: ")
        sprts.append(sprt)

    num = 0 
    print(f"თქვენი საყვარელი სპორტი არის: {sprt[num]}")

rndmsprt()
