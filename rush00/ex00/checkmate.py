text = """\
k....
.r...
..q..
....
.....
"""
def main(text):
    rook = []
    king =  []
    pawn = []
    bishop = []
    queen = []
    move_path = []
    postion_of_every_pawn = []

    arr = [list(line) for line in text.splitlines() if line.strip()]
    board_size = len(arr)
    
    for row in arr:
        match row:
            case _ if len(row) != len(arr):
                return "error"
            case _ if len(row) > 20:
                return "error"
            case _:
                pass

    for y in range(len(arr)):
        row = arr[y]
        for x in range (len(row)):
            if row[x].upper() not in {"R", "K", "P", "B", "Q", "."}:
                return "error"
            else:
                match row[x].upper():
                    case "R":
                        rook.append([x, y])
                        postion_of_every_pawn.append([x, y])
                    case "K":
                        king.append([x, y])
                        postion_of_every_pawn.append([x, y])
                    case "P":
                        pawn.append([x, y])
                        postion_of_every_pawn.append([x, y])
                    case "B":
                        bishop.append([x, y])
                        postion_of_every_pawn.append([x, y])
                    case "Q":
                        queen.append([x, y])
                        postion_of_every_pawn.append([x, y])
                    case _:
                        pass

    if len(king) != 1:
        return "Where the fuck is your king!!!!"
    
    for row in arr:
        print(row)
    
    print(f"r: {rook} k: {king}, q: {queen}, b: {bishop}, p:{pawn}")

    def rook_move(x, y):
        def move_right(x_new):
            while True:
                answer = [x_new,y]
                if (answer not in postion_of_every_pawn) and (x_new < board_size) and (y <= board_size):
                    move_path.append(answer)
                    x_new += 1
                else:
                    break

        def move_left(x_new):
            while True:
                answer = [x_new,y]
                if (answer not in postion_of_every_pawn) and (x_new > 0) and (y <= board_size):
                    move_path.append(answer)
                    x_new -= 1
                else:
                    break

        def move_up(y_new):
            while True:
                answer = [x,y_new]
                if (answer not in postion_of_every_pawn) and (y_new < board_size):
                    move_path.append(answer)
                    y_new += 1
                else:
                    break

        def move_down(y_new):
            while True:
                answer = [x,y_new]
                if (answer not in postion_of_every_pawn) and (y_new > 0):
                    move_path.append(answer)
                    y_new -= 1
                else:
                    break

        move_right(x)
        move_down(x)
        move_up(y)
        move_left(y)

    def bishop_move (x,y):
        def move_up_right(x_new, y_new):
            while True:
                if ([x_new,y_new] not in postion_of_every_pawn) and (y_new < board_size) and (x_new < board_size):
                    move_path.append([x_new + 1, y_new + 1])
                    x_new += 1
                    y_new += 1
                else:
                    break
        
        def move_down_left(x_new, y_new):
            while True:
                if ([x_new,y_new] not in postion_of_every_pawn) and (y_new > 0) and (x_new > 0):
                    move_path.append([x_new - 1, y_new - 1])
                    x_new -= 1
                    y_new -= 1
                else:
                    break

        def move_down_right(x_new, y_new):
            while True:
                if ([x_new,y_new] not in postion_of_every_pawn) and (y_new > 0) and (x_new < board_size):
                    move_path.append([x_new + 1, y_new - 1])
                    x_new += 1
                    y_new -= 1
                else:
                    break
        def rook_moves(x, y, board_size=8):
            moves = [(x, j) for j in range(board_size) if j != y] + [(i, y) for i in range(board_size) if i != x]
            return moves


        def move_up_left(x_new, y_new):
            while True:
                if ([x_new,y_new] not in postion_of_every_pawn) and (y_new < board_size) and (x_new > 0):
                    move_path.append([x_new - 1, y_new + 1])
                    x_new -= 1
                    y_new += 1
                else:
                    break
                
        move_up_right(x,y)
        move_down_left(x, y)
        move_down_right(x, y)
        move_up_left(x, y)

    def queen_move(x, y):
        def move_up_right(x_new, y_new):
            while True:
                if ([x_new,y_new] not in postion_of_every_pawn) and (y_new < board_size) and (x_new < board_size):
                    move_path.append([x_new + 1, y_new + 1])
                    x_new += 1
                    y_new += 1
                else:
                    break
        
        def move_down_left(x_new, y_new):
            while True:
                if ([x_new,y_new] not in postion_of_every_pawn) and (y_new > 0) and (x_new > 0):
                    move_path.append([x_new - 1, y_new - 1])
                    x_new -= 1
                    y_new -= 1
                else:
                    break

        def move_down_right(x_new, y_new):
            while True:
                if ([x_new,y_new] not in postion_of_every_pawn) and (y_new > 0) and (x_new < board_size):
                    move_path.append([x_new + 1, y_new - 1])
                    x_new += 1
                    y_new -= 1
                else:
                    break
        
        def move_up_left(x_new, y_new):
            while True:
                if ([x_new,y_new] not in postion_of_every_pawn) and (y_new < board_size) and (x_new > 0):
                    move_path.append([x_new - 1, y_new + 1])
                    x_new -= 1
                    y_new += 1
                else:
                    break
        def move_right(x_new):
            while True:
                answer = [x_new,y]
                if (answer not in postion_of_every_pawn) and (x_new < board_size) and (y <= board_size):
                    move_path.append(answer)
                    x_new += 1
                else:
                    break

        def move_left(x_new):
            while True:
                answer = [x_new,y]
                if (answer not in postion_of_every_pawn) and (x_new > 0) and (y <= board_size):
                    move_path.append(answer)
                    x_new -= 1
                else:
                    break

        def move_up(y_new):
            while True:
                answer = [x,y_new]
                if (answer not in postion_of_every_pawn) and (y_new < board_size):
                    move_path.append(answer)
                    y_new += 1
                else:
                    break

        def move_down(y_new):
            while True:
                answer = [x,y_new]
                if (answer not in postion_of_every_pawn) and (y_new > 0):
                    move_path.append(answer)
                    y_new -= 1
                else:
                    break
        move_up_right(x,y)
        move_down_left(x, y)
        move_down_right(x, y)
        move_up_left(x, y)
        move_right(x)
        move_down(x)
        move_up(y)
        move_left(y)

    def pawn_move(x, y):
        if (x - 1 and y - 1) < board_size:
            move_path.append([x - 1, y - 1]) 
        if (x + 1 and y - 1) < board_size:
            move_path.append([x + 1, y - 1]) 

    for i in queen:
        queen_move(i[0], i[1])
    for i in pawn:
        pawn_move(i[0], i[1])
    for i in rook:
        rook_move(i[0], i[1])
    for i in bishop:
        bishop_move(i[0], i[1])

    print(move_path)
    print(f"King: {king}")
    if king[0] in move_path:
        return "Success"
    else:
        return "Fail"
    
if __name__ == "__main__":
    print(main(text))