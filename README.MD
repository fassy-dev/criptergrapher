This is a code cryptographer, Upon startup, the following menu will appear:
    print("Main Menu")
    print("1. Decrypt Text")
    print("2. Encrypt Text")
    print("3. Code Creator")
    print("9. Exit Program")

After completing, for example, encryption, you will be thrown back into this menu. 
To close this program, press the number "9", next Enter.

If you absolutely must include the word and shifts in the code, so you don't have to write them after running the script, change these lines:
For Decryptor:
Line 15 encrypted_message = input("Encrypted word: ")
Correct to encrypted_message = "Word"
Line 17: key = (input("Shift: "))
Correct to: key = "Shift digit"

For Encryptor:
Line 35: message = input("Original word: ").lower()
Correct to: message = "Word ".lower()
Line 37: key = int(input("Shift: "))
Correct to: key = "Digits"

The menu was created using elif, and the tab looks like this:
if choice == "1":
print("You selected: Decryptor")
The code goes on...

Creator: Fassy-dev (or Fassydev)
Github: https://github.com/fassy-dev