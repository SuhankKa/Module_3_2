# Рассылка писем

def send_email(massage, recipient, *, sender = "university.help@gmail.com"):
   
        a = '@'
        b = ['.com', '.ru', '.net']

        if recipient == sender:
                print("Нельзя отправить письмо самому себе!")
                return
        
        if sender != "university.help@gmail.com":
                print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")    
                return

        if a not in recipient and a not in sender:
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
                return           

        if not any(domain in recipient for domain in b):
                print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        else:
                print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")

 

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com') # Письмо успешно отправлено с адреса university.help@gmail.com на адрес vasyok1337@gmail.com
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com') # НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса urban.info@gmail.com на адрес urban.fan@mail.ru
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.uk', sender='university.help@gmail.com') # Невозможно отправить письмо с адреса urban.teacher@mail.uk на адрес urban.student@mail.ru
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru') # Нельзя отправить письмо самому себе!