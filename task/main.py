ПользовательскийВВод = str(input()).lower()
КолГл = 0
КолСогл = 0
ГлБукв = ["е","ы","а","о","э","я","и","ю"]
СоглБукв = "цкнгшщзхъфвпрлджчсмтьб"
for символ in ПользовательскийВВод:
    if символ in ГлБукв:
        КолГл += 1
    elif символ in СоглБукв:
        КолСогл += 1
print(КолСогл, КолГл)

