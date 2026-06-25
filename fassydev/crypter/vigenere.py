def encrypt(plain_text, key):
    final_text = []
    key = key.upper().replace('Ё', 'Е')
    key_index = 0

    alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    for char in plain_text:
        if char.lower() in alphabet_lower:
            if char.isupper():
                alphabet = alphabet_upper
            else:
                alphabet = alphabet_lower

            p_i = alphabet.index(char)
            k_i = alphabet_upper.index(key[key_index])

            c_i = (p_i + k_i) % 33

            final_text.append(alphabet[c_i])
            key_index = (key_index + 1) % len(key)
        else:
            final_text.append(char)

    return "".join(final_text)

def decrypt(cipher_text, key):
    final_text = []
    key = key.upper().replace('Ё', 'Е')
    key_index = 0

    alphabet_upper = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alphabet_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    for char in cipher_text:
        if char.lower() in alphabet_lower:
            if char.isupper():
                alphabet = alphabet_upper
            else:
                alphabet = alphabet_lower

            c_i = alphabet.index(char)
            k_i = alphabet_upper.index(key[key_index])

            p_i = (c_i - k_i + 33) % 33

            final_text.append(alphabet[p_i])
            key_index = (key_index + 1) % len(key)
        else:
            final_text.append(char)

    return "".join(final_text)
