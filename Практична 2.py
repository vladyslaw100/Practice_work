lists = [1, 4, 2, 9, 3, 8, 12, 14, 11, 7,
             "australia", "house", "lake", "way", "key",
             "wave", "road", "city", "river", "tree"]

num = []
text = []

for item in lists:
    if type(item) == int:
        num.append(item)
    else:
        text.append(item)

num.sort()
text.sort()

sorted = num + text

obiednannia = []
for i in num:
    if i % 2 == 0:
        obiednannia.append(i)

upper_text = []
for s in text:
    upper_text.append(s.upper())

print("Cписок:", lists)
print("Відсортований список:", sorted)
print("Елементи, кратні двом:", obiednannia)
print("Рядки капсом:", upper_text)
