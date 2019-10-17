# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# # имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
# # параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def users_info(name, surname, birth_year, city, email, phone_n):
    # function takes user information and shows all the information on the screen
    while not len(birth_year) == 4 or not birth_year.isdigit():
        birth_year = input("birth year (four digits): ")
    while not len(phone_n) == 11 or not phone_n.isdigit():
        phone_n = input("birth year (eleven digits): ")
    # verify that the year and phone number are entered correctly
    name, surname, city = name.title(), surname.title(), city.title()
    # changes first letter to big in surname name and city

    print(f"{name} {surname}, {birth_year} birth year, live in {city}.\n"
          f"Contact info: e mail - {email}, phone number - {phone_n}")


users_info(name=input("name: "), surname=input("surname: "), birth_year=input("birth year: "),
           city=input("city of residence: "), email=input("e mail: "), phone_n=input("phone number: "))
