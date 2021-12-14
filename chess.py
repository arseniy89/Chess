class Pawn:
    def move():
        if (cur == "♙ "):
            return ((fut == "  " and i1 - i2 == 1 and j2 == j1) or
                    (fut == "  " and i1 == 2+i2 == 6 and j2 == j1) or
                    (is_enemys(cur, fut) and i1-i2 == 1 and abs(j2-j1) == 1))
        else:
            return ((fut == "  " and i2 - i1 == 1 and j2 == j1) or
                    (fut == "  " and i1 == i2-2 == 1 and j2 == j1) or
                    (is_enemys(cur, fut) and i2-i1 == 1 and abs(j2-j1) == 1))


class Rock:
    def move():
        if (j1 == j2 and i1 != i2):
            for i in range(min(i1,i2)+1, max(i1,i2)):
                if (board[i][j1] != "  "):
                    return False
            return True
        if (j1 != j2 and i1 == i2):
            for j in range(min(j1,j2)+1, max(j1,j2)):
                if (board[i1][j] != "  "):
                    return False
            return True
        return False


class Horse:
    def move():
        return (((abs(i1-i2) == 1 and abs(j1-j2) == 2) or (abs(i1-i2) == 2 and abs(j1-j2) == 1)))


class Elephant:
    def move():
        if (i1-i2 == j1-j2):
            for i,j in zip(range(min(i1,i2)+1, max(i1,i2)), range(min(j1,j2)+1, max(j1,j2))):
                if (board[i][j] != "  "):
                    return False
            return True
        if (abs(i1 - i2) == abs(j1 - j2)):
            for i,j in zip(range(max(i1,i2)+1, min(i1,i2)), range(min(j1,j2)+1, max(j1,j2))):
                if (board[i][j] != "  "):
                    return False
            return True
        return False


class Queen:
    def move():
        return (Rock.move() or Elephant.move())


class King:
    def move():
        return ((-1 <= i1-i2 <= 1) and (-1 <= j1-j2 <= 1) and not(i1-i2 == j1-j2 == 0))


def tutorial():
    cout()
    print("Player:")
    print("● Enters the start Ox1")
    print("● Enters the start Oy1")
    print("● Enters the  end  Ox2")
    print("● Enters the  end  Oy2\n")


def first_completion():
    for i in range(0, 8):
        board[0][i], board[1][i] = f"{shapes2[i+1]} ", "♟ "
        board[7][i], board[6][i] = f"{shapes1[i+1]} ", "♙ "
        board[2][i], board[3][i], board[4][i], board[5][i] = "  ", "  ", "  ", "  "


def cout():
    print("\n")
    [print(f"    {i+1}", end="") for i in range(8)]
    print(f"\n  {'●━━━━'*8}●")
    for i in range(8):
        print(i+1, end= " ")
        [print(f"┃ {board[i][j]} ", end="") for j in range(8)]
        print(f"┃ {i+1}\n  {'●━━━━'*8}●")
    [print(f"    {i+1}", end="") for i in range(8)]
    print ()


def kings_alive():
    f1, f2 = False, False
    for i in range(8):
        if ("♔ " in board[i]):
            f1 = True
        if ("♚ " in board[i]):
            f2 = True
    return (f1 == f2 == True)


def reading(step):
    while(True):
        try:
            print("1st: " if (step) else "2nd: ")
            global i1, j1, i2, j2, cur, fut
            i1 = int(input("● Ox1: "))-1
            j1 = int(input("● Oy1: "))-1
            i2 = int(input("● Ox2: "))-1
            j2 = int(input("● Oy2: "))-1
            cur, fut = board[i1][j1], board[i2][j2]
            return 
        except: continue


def true_step(step):
    return ((step == 1 and cur in team1) or (step == 0 and cur in team2))


def is_enemys(sh1, sh2):
    return ((sh1 in team1 and sh2 in team2) or (sh1 in team2 and sh2 in team1))


def answer():
    f = False
    for i in range(8):
        if ("♔ " in board[i]):
            f = True; break
    print(("1st" if (f) else "2nd") + " won")


def gameplay():
    step = 1
    while (kings_alive()):
        reading(step)
        if (true_step(step) and (is_enemys(cur, fut) or fut == "  ")):
            if (((cur == "♙ " or cur == "♟ ") and Pawn.move()) or 
                ((cur == "♖ " or cur == "♜ ") and Rock.move()) or
                ((cur == "♘ " or cur == "♞ ") and Horse.move()) or
                ((cur == "♗ " or cur == "♝ ") and Elephant.move()) or
                ((cur == "♕ " or cur == "♛ ") and Queen.move()) or
                ((cur == "♔ " or cur == "♚ ") and King.move())): 
                board[i2][j2], board[i1][j1], step = cur, "  ", (step+1) % 2
                cout()
    answer()


def main():
    print("This is the game chess:")
    global shapes1, shapes2, team1, team2, board
    shapes1 = ["♙","♖","♘","♗","♕","♔","♗","♘","♖"]
    shapes2 = ["♟","♜","♞","♝","♛","♚","♝","♞","♜"]
    board = [["  "]*8 for i in range(8)]
    team1, team2 = [""]*6, [""]*6
    for i in range(6):
        team1[i], team2[i] = f"{shapes1[i]} ", f"{shapes2[i]} "
    tutorial()
    while (input("Play? (y) ") == 'y'):
        first_completion()
        cout(); gameplay()


main()
