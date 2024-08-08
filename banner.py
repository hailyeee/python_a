import pyfiglet

while True:

    user_text = input("글자를 입력하세요")

    if user_text == "0":
        break

    font = pyfiglet.Figlet(font='standard')

    ascii_art = font.renderText(user_text)

    print(ascii_art)