
print("Для игры вводите две коордтнаты X и Y через пробел в формате; 0 1")

field = [[" "] * 3 for i in range(3)]  # Создаем переменную игорвого поля


# Создаем метки поля по горизонтали и вертикали: X = 0 1 2, Y = 0 1 2
def print_field():
    print(f"  0 1 2")
    for i in range(3):
        glue_lines = " ".join(field[i])
        print(f"{i} {glue_lines}")


def ask():
    while True:
        cords = input(" Ваш ход: ").split()
        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue
        x, y = cords
        if not (x.isdigit()) or not (y.isdigit()):
            print(" Введите числа! ")
            continue
        x, y = int(x), int(y)
        if 0 > x or x > 2 or 0 > y or y > 2:
            print(" Не верные координаты! Попробуйте еще раз ")
            continue
        if field[x][y] != " ":
            print(" Клетка занята! ")
            continue
        return x, y


def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл 'X' !!!")
            return True
        if symbols == ["O", "O", "O"]:
            print("Выиграл 'O' !!!")
            return True
    return False


num = 0
while True:
    num += 1
    print_field()
    if num % 2 == 1:
        print("Ходит: 'X'")
    else:
        print("Ходит: 'O'")
    x, y = ask()
    if num % 2 == 1:
        field[x][y] = "X"
    else:
        field[x][y] = "O"
    if check_win():
        break
    if num == 9:
        print("Ничья")
        break
