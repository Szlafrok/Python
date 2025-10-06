import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import dotenv

with open('menu.json', 'r', encoding='utf-8') as f:
    menu = json.load(f)
    list_of_pizzas = menu['menu']

list_of_pizza_names = [pizza["pizza"] for pizza in list_of_pizzas]

def calculate_cost(ordered_pizza):
    for pizza in list_of_pizzas:
        if pizza["pizza"] == ordered_pizza["pizza_name"]:
            cost = int(ordered_pizza["pizza_amount"]) * int(pizza["ceny"][ordered_pizza["size"]])
    return cost


order = [] # LISTA NA ZAMÓWIENIE


def send_email(t):
    dotenv.load_dotenv()
    subject = "Potwierdzenie zamówienia pizzy"
    sender_email = os.getenv("sender_email")
    recipient_email = os.getenv("recipient_email")
    sender_password = os.getenv("sender_password")
    smtp_server = "smtp.wp.pl"
    smtp_port = 465

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject
    body_part = MIMEText(t)
    message.attach(body_part)

    with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, message.as_string())


def main_page():
    print("1. Wyświetl menu")
    print("2. Dodaj pizzę do zamówienia")
    print("3. Wyczyść zamówienie")
    print("4. Wyślij zamówienie")
    print("5. Zakończ")

    option = input("Wprowadź opcję: ")

    if option == "1":
        for pizza in list_of_pizzas:
            print(pizza["pizza"])
            print(", ".join(pizza["dodatki"]))
            print(f"Mała: {pizza['ceny']['S']} zł.")
            print(f"Średnia: {pizza['ceny']['M']} zł.")
            print(f"Duża: {pizza['ceny']['L']} zł.")
        input("Wciśnij dowolny klawisz, aby wrócić do menu")
        main_page()
    elif option == "2":
        for i in range(len(list_of_pizza_names)):
            print(f"{i + 1}. {list_of_pizza_names[i]}")
        pizza_name_number = int(input("Podaj numer pizzy: "))
        pizza_amount = int(input("Podaj ilość: "))
        size = input("Jakiego rozmiaru S/M/L?: ")
        order.append({
            "size": size,
            "pizza_amount": pizza_amount,
            "pizza_name": list_of_pizza_names[pizza_name_number - 1],
        })
        main_page() # DODAĆ
    elif option == "3":
        order.clear()
        main_page()
    elif option == "4":
        text = "Dziękujemy! Oto podsumowanie:\n"
        total_cost = 0
        for pizza in order:
            cost = calculate_cost(pizza)
            text += f"{pizza['pizza_amount']} x {pizza['pizza_name']} {pizza['size']}: {cost}\n "
            total_cost += cost
        text += f"Suma: {total_cost} zł\n"
        send_email(text)
        print("Wysłano potwierdzenie")
    elif option == "5":
        quit(0)
    else:
        print("Wybrano złą opcję.")

main_page()