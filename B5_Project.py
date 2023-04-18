#Создание матрицы для игрового поля
game_board = [["- "] *3 for i in range(3)]


#Создание игрового поля и его оформления
def board():
    print("  | 0  | 1  | 2 |")
    print("_________________")
    b = 0
    for i in game_board:
        a = " | ".join(i)
        print(f"{b} | {a}|")
        print("_________________")
        b += 1

# Проверка выиграшных значений
def check_conditions():
    check_conditions_win = (
                            ((0, 0), (0, 1), (0, 2)),
                            ((1, 0), (1, 1), (1, 2)),
                            ((2, 0), (2, 1), (2, 2)),
                            ((0, 0), (1, 0), (2, 0)),
                            ((0, 1), (1, 1), (2, 1)),
                            ((0, 2), (1, 2), (2, 2)),
                            ((0, 0), (1, 1), (2, 2)),
                            ((2, 0), (1, 1), (0, 2))
                            )

    for chen_win in check_conditions_win:
        cheking = []
        for i in chen_win:
            cheking.append(game_board[i[0]][i[1]])
            if cheking == ["X ", "X ", "X "]:
                print("\nПОЗДРАВЛЯЕМ, ВЫИГРАЛ X!\n")
                return True
            elif cheking == ["0 ", "0 ", "0 "]:
                print("\nПОЗДРАВЛЯЕМ, ВЫИГРАЛ 0!\n")
                return True


#Запуск игры и ввод значени
def game_launch():
    print("Добро пожаловать в игру 'Крестики-нолики'")
    print('Игрок "КРЕСТИКИ" делает ход первым')
    print()

    board()
    current_player = "X"
    step = 1
    print()

    while (step < 10):
        print(f"Текущий игрок: {current_player}")
        game_values = list(map(int, input("Введите значение полей без пробела\nномер строки - номер столбца: ")))

        if len(game_values) != 2:
            print("\nВведите корректное значение!!!\n")
            continue

        if game_values[0] > 2 and game_values[1] > 2:
            print("\nВВЕДИТЕ КОРРЕКТНЫЕ ЗНАЧЕНИЯ\n")
            continue

        if game_board[game_values[0]][game_values[1]] != "- ":
            print("\nЯчейка занята!!!\n")
            continue

        if current_player == "X":
            game_board[game_values[0]][game_values[1]] = "X "
            current_player = "0"

        elif current_player == "0":
            current_player = "X"
            game_board[game_values[0]][game_values[1]] = "0 "

        if check_conditions():
            break

        board()
        step += 1
        print(step)







game_launch()