listProducts = ["Молоко" , "Хліб", "Капуста" , "Шоколад" , "Яблука"] # 1 завдання
listProducts.append("Банан")
print (listProducts)

listgrades = [10, 9, 8, 10, 7 ,11]                                   # 2 завдання
print(sum(listgrades)/len(listgrades))

listNames = ["Illia" , "Olia" , "Vadim" , "Artem" , "Anna"]          # 3 завдання
listNames.sort()
print(listNames)

listCities = ["Костпіль" , "Рівне" , "Львів" , "Одеса" , "Київ"]     # 4 завдання
listCities[1] = "Луцьк"
print(listCities[0])
print(listCities[-1])

listMusicInstruments = ["Гітара" , "Піаніно", "Барабани" , "Електрогітара" , "Скрипка"]    # 5 завдання
listMusicInstruments.remove(listMusicInstruments[2])
listMusicInstruments.reverse()
print(listMusicInstruments)