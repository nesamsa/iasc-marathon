students = ["Anna", "Ivan", "Olha", "Taras", "Katya"]
grades = [95, 62, 47, 88, 53]
maxgrade = max(grades)
topstudent = students[grades.index(maxgrade)]
print("Студент з найвищою оцінкою:", topstudent)

passedstudents = [students[i] for i in range(len(grades)) if grades[i] > 60]
print("Студенти з оцінкою понад 60:", passedstudents)

failedcount = sum(1 for grade in grades if grade < 60)
print("Кількість студентів, які не склали:", failedcount)

#------------------------------------------------------------------------------------

logs = ["ok", "error", "fail", "ok", "error", "warning", "ok", "fail"]
print(logs.count("error"), "з" , len(logs) , "слов являється словом error" )

#------------------------------------------------------------------------------------

expenses = [
    ["Понеділок", 120],
    ["Вівторок", 80],
    ["Середа", 150],
    ["Четвер", 0],
    ["П’ятниця", 250],
    ["Субота", 300],
    ["Неділя", 200]
]
maxday = max(expenses, key=lambda x: x[1])[0]
totalexpenses = sum(day[1] for day in expenses)
daysover100 = [day[0] for day in expenses if day[1] > 100]
print(f"Найбільші витрати були у: {maxday}")
print(f"Загальні витрати за тиждень: {totalexpenses} грн")
print("Дні, коли витрати були більше 100 грн:", ", ".join(daysover100))

#------------------------------------------------------------------------------------

products = [
    ["яблуко", 2, 12.5],
    ["банан", 5, 8.0],
    ["молоко", 1, 34.0],
    ["хліб", 2, 16.0]
]
sumproduct = 0
for product in products:
    sumproduct += product[1] * product[2]
expenproduct = products[0]
for product in products:
    if product[2] > expenproduct[2]:
       expenproduct = product
priceproduct = []
for product in products:
    name = product[0]
    num = product[1]
    price = product[2]
    sum = num * price
    priceproduct.append(f"{name} - {sum} грн")
print("Загальна сума чеку:", sumproduct, "грн")
print("Найдорожчий товар:", expenproduct[0])
print("Список товарів і сум:")
for item in priceproduct:
    print(item)
    
    #------------------------------------------------------------------------------------

excluded = [10, 14, 18]

squares = [x**2 for x in range(1, 31) if x % 2 == 0 and x % 4 != 0 and x not in excluded]

print(squares)