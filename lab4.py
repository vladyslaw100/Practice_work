prodlist = {
    "chlib":60,
    "jablko":20,
    "banan":30,
    "grusha":10
}

def convert(num):
    return f"ціна: {num:.2f} грн"


def prodcheck(*products):
    res = {}
    for prod in products:
        if prod in prodlist: res[prod] = True
        else: res[prod] = False
    return res


def magazyn():
    while True:
        print("-" * 50)
        user_prod = input("Enter a product you want to buy (separated by space): ").lower().split()
        prod_to_buy = prodcheck(*user_prod)
        if all(prod_to_buy.values()):
            while True:
                a = input("buy or price? (or exit): ").lower()
                if a == "buy":
                    print("Congrats!")
                    break
                elif a == "price":
                    total = 0
                    for product in user_prod:
                        total += prodlist[product]
                    print("total price: ", convert(total))
                elif a == "exit":
                    return -1
                else:
                    print("try again")
                    print("-" * 25)
        else:
            print("No, the product was incorrect")
            print("-"*50)

def main():
    num = float(input("Enter a number: "))
    print(convert(num))
    result = prodcheck("chlib", "computer", "jay", "grusha", "jablko", "banan")
    print(result)
    magazyn()


if __name__ == '__main__':
    main()


if __name__ == '__main__':
    main()


