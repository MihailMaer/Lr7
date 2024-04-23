text = str(input("Введите текст "))
glasn = 0
sogl = 0
vow = set("аеиоуыэюяАЕИОУЫЭЮЯ")
dow = set("йцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТБЬ")
for letter in text:
    if letter in vow:
        glasn += 1
    if letter in dow:
        sogl += 1
print("Количество гласных = ", glasn)
print("Количестов согласных = ", sogl) 

