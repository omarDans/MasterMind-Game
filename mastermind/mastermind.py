import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4

def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        code.append(random.choice(COLORS))
    return code

def guess_code():
    while True:
        guess = input('Intento (COLORES: R, G, B, Y, W, O): ').upper().strip().split(" ")
        if len(guess) > CODE_LENGTH or len(guess) < CODE_LENGTH:
            print(f"Tu intento debe de ser de {CODE_LENGTH} colores")
            continue
        for i in guess:
            if i not in COLORS:
                print(f"{i} no es un color válido")
                break
        else:
            break
    return guess


def check_code(guess, real_code):
    colors_count = {}
    incorrect_pos = 0
    correct_pos = 0

    for color in real_code:
        if color not in colors_count:
            colors_count[color] = 0
        colors_count[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            colors_count[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in colors_count and colors_count[guess_color] > 0:
            incorrect_pos += 1
            colors_count[guess_color] -= 1

    return correct_pos, incorrect_pos



def main():
    code = generate_code()
    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_pos, incorrect_pos = check_code(guess, code)
        print(f"Posiciones correctas: {correct_pos} | Posciones incorrectas: {incorrect_pos}")
        if guess == code:
            print("Enhorabuena has ganado!")
            play_again = input("Presiona enter para jugar otra vez ('q' para salir): ").lower()
            if play_again.strip() == 'q':
                break
            else:
                main()
        else:
            print(f"Intento número: {attempts}")
            continue
    else:
        print("Se acabaron los intentos, has perdido :(")
        print(code)

main()