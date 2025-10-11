prodlist = {
    "chlib":60,
    "jablko":20,
    "banan":30,
    "grusha":10
}

def convert(num):
    return f"ціна: {num:.2f} грн"

def list(*produkt):
    produkts = {}
    for item in produkt:
        produkts[item] = item in prodlist
    return produkts

def shop(check, option):
    if not check:
        return "В списку немає продуктів"
    for item in check:
        if item not in prodlist:
            return "Певних товарів немає в магазині"
    total = 0
    for item in check:
        total += prodlist[item]
    if option == "price":
        return "Загальна " + convert(total)
    elif option == "buy":
        return "Ваші покупки " + ", ".join(check) + " " + convert(total)
    else:
        return "Ви вказали не правильні дані"



def main():
    num = float(input())
    print(convert(num))
    print(list("chlib", "jablko", "Jay", "banan", "yogurt"))
    a=0
    while True:
        if(a==0):
            check = input().split()
            option = input()
            print(shop(check, option))
            print("------------------")
            print("Якщо хочете вийти введіть - stop. Інакше вводьте нові продукти")
            check = input().split()
            if check == "stop":
                break
            option = input()
            print(shop(check, option))
            a+=1
        else:
            print("Якщо хочете вийти введіть - stop. Інакше вводьте нові продукти")
            check = input().split()
            if check == "stop":
                break
            option = input()
            print(shop(check, option))



if __name__ == '__main__':
    main()