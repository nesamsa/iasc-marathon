name_list = ["Illia" , "Olia" , "Vadim" , "Artem" , "Anna"]
def hello_world() :
    print("Hello world!")
hello_world()
#-------------------------------------------
def greet(name) :
    print("Привіт " + name)
greet("Анна")
#-------------------------------------------
def square(n) :
    print("Квадрат числа : ",n * n)
square(2)
#-------------------------------------------
def add(a, b) :
    sum = (a + b)
    return sum
print("Сума : " , add(5,2))
#-------------------------------------------
def greet(name="Гість"):
    print("Привіт " + name)
greet(name="Гість")
#-------------------------------------------
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)
factorial(4)
#-------------------------------------------
def is_even(n) :
    if(n % 2):
        print("False")
    else :
        print("True")
is_even(2)
#-------------------------------------------
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)
print_numbers(5)
#-------------------------------------------
def find_name(name, name_list):
    for names in name_list:
        if(name == names):
            print("True")
            break    
    else:
        print("False")
find_name("Illia", name_list)
#-------------------------------------------
def max_of_three(a, b, c):
    print (max(a,b,c))
max_of_three(1,6,3)
#-------------------------------------------
def reverse_string(s):
    reverse_text = ''.join(reversed(s))
    print(reverse_text)
reverse_string("Hello world")
#-------------------------------------------
def count_vowels(s):
    vowels = "aeiouAEIOUаіеиоуэюяАІЕИОУЭЮЯ"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    print(count)
count_vowels("Hello world")
#-------------------------------------------
def average(*numbers):
    return sum(numbers) / len(numbers)
print("Середнє значення : " ,average(1,2,3,4,5))
#-------------------------------------------
user_info = {
    "name":"Illia",
    "age": "17",
    "country":"Ukraine"
}
def print_user_info(info):
    info = user_info.items()
    return info
print(print_user_info(user_info))
#-------------------------------------------
def outer():
    def inner():
        print("Я - вкладена функція!")
    inner()
outer()