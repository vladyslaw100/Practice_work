
def generator(f):
    with open(f, "r", encoding="UTF-8") as file:
        for line in file:
            line = "".join(ch for ch in line if ch.isalpha())
            pairs = [line[i]+line[i+1] for i in range(len(line)-1)]
            for i in range(0, len(pairs), 3):
                yield pairs[i:i+3]

def main():
    total_pairs = 0
    for triple in generator("anything.txt"):
        total_pairs += len(triple)
        print(triple)
    print("Total_pairs", total_pairs)


if __name__ == "__main__":
    main()