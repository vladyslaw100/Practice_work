from decoratore import checkcpu

@checkcpu
def add(a, b, cpu):
    print("it is equals:", a + b)

def main():
    while True:
        a = input("num or stop ")
        if a == "stop":
            break
        b = input("num or stop ")
        if b == "stop":
            break
        elif a and b:
            add(int(a),int(b),5)
        else:
            print("error")
            continue

if __name__ == '__main__':
    main()