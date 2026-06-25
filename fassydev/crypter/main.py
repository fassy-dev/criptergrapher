# from os import name #Not suppored.
import time
import caesar
import vigenere

while True:
    print("Главное меню")
    print("1. Расшифровать текст")
    print("2. Зашифровать текст")
    print("3. Создатель кода")
    print("9. Выйти из программы")
    try:
        main_choice = input("Выберите нужное действие (1, 2, 3, 4): ")
    except KeyboardInterrupt:
        print("\nПрограмма была остановлена пользователем...")
        exit(0)

    if main_choice == "1":
        print("Вы выбрали: Расшифровальщик, какой шифр будем использовать?")
        print("1. Шифр Цезаря")
        print("2. Шифр Вижинера")
        sub_choice_decrypt = input("Выберите подпункт (1-2): ")

        if sub_choice_decrypt == "1":
            print("Вы выбрали: Расшифровальщик, Шифр Цезаря")
            encrypted_message = input("Зашифрованное слово: ")
            # encrypted_message = input( "Encrypted word: "), or the word itself,
            # it will look like this: encrypted_message = "Word"
            key = int(input("Сдвиг: "))
            # key = int(input("Shift: ")), or write the shift instead, it will look like this: key = "5"

            result = caesar.decrypt(encrypted_message, key)
            print("Расшифрованный текст:", result)

        elif sub_choice_decrypt == "2":
            print("Вы выбрали: Расшифровальщик, Шифр Вижинера")
            user_cipher = input("Введите зашифрованный текст: ")
            user_key = input("Введите ключ (только русские буквы): ")

            while not all(c.lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" for c in user_key) or not user_key:
                print("Ошибка! Ключ должен состоять только из русских букв.")
                user_key = input("Введите корректный ключ: ")

            result = vigenere.decrypt(user_cipher, user_key)
            print("\nРезультат расшифрования:")
            print(result)

        else:
            print("Ошибка! Неверный подпункт меню.")

    elif main_choice == "2":
        print("Вы выбрали: Шифровальщик, какой шифр будем использовать?")
        print("1. Шифр Цезаря")
        print("2. Шифр Вижинера")
        sub_choice_encrypt = input("Выберите подпункт (1-2): ")

        if sub_choice_encrypt == "1":
            print("Вы выбрали: Шифровальщик, Шифр Цезаря")
            message = input("Исходное слово: ")
            # if name.isalpha():
            # break
            # else:
            # print("В вашем тексте найды цифры, разрешены только буквы.")
            # input("Initial word: "), or the word itself in "Word", will look like this: message = "Word".lower()
            key = int(input("Сдвиг: "))
            # int(input("Shift: ")), or write shift instead: key = "Numbers"

            result = caesar.encrypt(message, key)
            print("Зашифрованный текст:", result)
            time.sleep(2)

        elif sub_choice_encrypt == "2":
            print("Вы выбрали: Шифровальщик, Шифр Вигенера  (Vigener)")
            user_text = input("Введите текст для шифрования: ")
            user_key = input("Введите ключ (только русские буквы): ")

            while not all(c.lower() in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" for c in user_key) or not user_key:
                print("Ошибка! Ключ должен состоять только из русских букв.")
                user_key = input("Введите корректный ключ: ")

            result = vigenere.encrypt(user_text, user_key)
            print("\nРезультат шифрования:")
            print(result)

        else:
            print("Ошибка! Неверный подпункт меню.")

    elif main_choice == "3":
        print("Создатель данного кода Fassydev (Github)")
        time.sleep(2)

    elif main_choice == "9" or main_choice == "exit":
        print("Закрываюсь...")
        time.sleep(1.5)
        break

    else:
        print("Ошибка! Пожалуйста, введите только 1, 2, 3, 4.")
        time.sleep(0.5)