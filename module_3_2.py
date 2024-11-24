


def send_email(message, recipient, sender="university.help@gmail.com"):
    if "@" not in recipient or "@" not in sender or not recipient.endswith((".com", ".ru", ".net")) or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")


message = input('Введите сообщение: ')
email = input('Введите email: ')
send_email(message,email)