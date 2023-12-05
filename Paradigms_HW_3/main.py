import tic_tac_toe as t

if __name__ == '__main__':
    t.print_field(t.array)
    win = False
    player = t.p1
    turn_number = 1
    while not win and turn_number < 10:
        print(f"-> Ход {turn_number}. Игрок {player}.")
        t.next_turn(player)
        if ((t.array[0][0] == t.array[1][1] == t.array[2][2] or
             t.array[0][2] == t.array[1][1] == t.array[2][0]) and
                t.array[1][1] != '_'):
            win = True
        elif t.win_condition(t.array):
            win = True
        else:
            if player == t.p1:
                player = t.p2
            else:
                player = t.p1
        turn_number += 1
    if win:
        print(f"-> Победил Игрок {player}!")
    else:
        print("-> Победила дружба!")
