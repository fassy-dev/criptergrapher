def encrypt(message, key):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    encrypted_message = ""
    message = message.lower()

    for letter in message:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            new_index = (current_index + key) % len(alphabet)
            correct_letter = alphabet[new_index]
            encrypted_message = encrypted_message + correct_letter
        else:
            encrypted_message = encrypted_message + letter
    return encrypted_message

def decrypt(encrypted_message, key):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    decrypted_message = ""

    for letter in encrypted_message:
        if letter in alphabet:
            current_index = alphabet.index(letter)
            new_index = (current_index - key) % len(alphabet)
            correct_letter = alphabet[new_index]
            decrypted_message = decrypted_message + correct_letter
        else:
            decrypted_message = decrypted_message + letter
    return decrypted_message
