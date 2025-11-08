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


def main():
    num = float(input("Enter a number: "))
    print(convert(num))
    result = prodcheck("chlib", "computer", "jay", "grusha")
    print(result)

    while True:
        user_prod = input("Enter a product (separated by space): ").lower().split()
        prod_to_buy = prodcheck(*user_prod)
        if all(prod_to_buy.values()):
            while True:
                a = input("buy or watch a price? (or exit to quit): ").lower()
                if a == "buy":
                    pass
                    break
                elif a == "watch":
                    total = 0
                    for product in user_prod:
                        total += prodlist[product]
                    print("total price: ", total)
                    continue
                elif a == "exit":
                    return
                else: print("anything else")
        else:
            print("No, the product was incorrect")

if __name__ == '__main__':
    main()
