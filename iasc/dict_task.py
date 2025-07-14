contacts = {"Anna": "093-123-45-67",
            "Ivan": "050-888-99-00",
            "Olha": "097-777-33-22"}
contacts.update({"Taras": "063-000-11-22"})
contacts.pop("Ivan")
print(contacts)
print(contacts.get('Katya', 'Немає номера Катерини'))

#--------------------------------------------------------------------

grades = {
"math": 88,
"physics": 75,
"english": 93,
"history": 59}
maxgrade = max(grades, key = grades.get)
print("Предмет з найвищою оцінкою:",maxgrade)
avaragegrd = sum(grades.values()) / len(grades)
print("Середній бал з усіх предметів: " , avaragegrd)
passgrades = [subject for subject, grade in grades.items() if grade > 80]
print("Предмети з оцінкою більше 80:", passgrades)

#--------------------------------------------------------------------

transactions = [("Anna", 200),
                ("Ivan", -50),
                ("Anna", 100),
                ("Olha", 500),
                ("Ivan", 150),
                ("Olha", -100),]
balances = {"Anna" : 300,
            "Ivan" : 100,
            "Olha" : 400 }
maxbalance = max(balances, key = balances.get)
print(maxbalance, "має найбільший баланс.")
minusbalance = [money for money, balance in balances.items() if balance < -1]
print(minusbalance)

#--------------------------------------------------------------------

text = "hello world hello again hello world test world"
splittext = text.split()
wordcount = {}
for word in splittext:
    if word in wordcount:
        wordcount[word] += 1
    else:
        wordcount[word] = 1
print(wordcount)

#--------------------------------------------------------------------

student = {"name": "Anna",
           "age": 20,
           "courses": ["math", "physics", "english"]
}
import json

xstudent = json.dumps(student)

print(xstudent)

student = json.loads(xstudent)
student.update({"courses" : "history"})
print(student["courses"])