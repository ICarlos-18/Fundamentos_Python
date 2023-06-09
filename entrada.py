# fuction input -> retorna string

num_a = input("Ingresa un numero: ")
num_a = input("Ingresa un numero: ")

print(num_a + num_b)

name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))
city = input("Ingresa tu ciudad/pueblo")

# string format
"""
  Holaa, soy name, tengo age años y vivo en city
"""
greeting = "Holaa, soy {}, tengo {} años y vivo en {}"
greeting.format(name, age, city)

greeting_2 = f"Holaa, soy { name }, tengo { age } años y vivo en { city }"

print(greeting_2)
