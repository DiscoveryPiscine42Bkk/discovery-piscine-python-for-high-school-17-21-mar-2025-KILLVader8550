def checkmate(board):
    rook = []
    king =  []
    pawn = []
    bishop = []
    queen = []
    move_path = []
    postion_of_every_pawn = []

    arr = [list(line) for line in board.splitlines() if line.strip()]
    board_size = len(arr)
    
    for row in arr:
        match row:
            case _ if len(row) != len(arr):
                return print("error")
            case _ if len(row) > 20:
                return print("error")
            case _:
                pass

    for y in range(len(arr)):
        row = arr[y]
        for x in range (len(row)):
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
        return print("error")
    
    for row in arr:
        print(row)
 
    print(f"r: {rook} k: {king}, q: {queen}, b: {bishop}, p:{pawn}")
    
    #condition check-----------
    def move_up_right(x_new, y_new):
        while True:
            if ((x_new,y_new) not in postion_of_every_pawn) and (y_new <= board_size) and (x_new <= board_size):
                move_path.append([x_new + 1, y_new + 1])
                x_new += 1
                y_new += 1
            else:
                break
    
    def move_down_left(x_new, y_new):
        while True:
            if ((x_new,y_new) not in postion_of_every_pawn) and (y_new >= 0) and (x_new >= 0):
                move_path.append([x_new - 1, y_new - 1])
                x_new -= 1
                y_new -= 1
            else:
                break

    def move_down_right(x_new, y_new):
        while True:
            if ([x_new,y_new] not in postion_of_every_pawn) and (y_new >= 0) and (x_new <= board_size):
                move_path.append([x_new + 1, y_new - 1])
                x_new += 1
                y_new -= 1
            else:
                break
    
    def move_up_left(x_new, y_new):
        while True:
            if ((x_new,y_new) not in postion_of_every_pawn) and (y_new <= board_size) and (x_new >= 0):
                move_path.append([x_new - 1, y_new + 1])
                x_new -= 1
                y_new += 1
            else:
                break

    def move_right(x_new, y):
        while True:
            if ((x_new,y) not in postion_of_every_pawn) and (x_new <= board_size):
                move_path.append([x_new,y])
                x_new += 1
            else:
                break

    def move_left(x_new, y):
        while True:
            if ((x_new,y) not in postion_of_every_pawn) and (x_new >= 0):
                move_path.append([x_new,y])
                x_new -= 1
            else:
                break

    def move_up(x, y_new):
        while True:
            if ((x,y_new) not in postion_of_every_pawn) and (y_new <= board_size):
                move_path.append([x,y_new])
                y_new += 1
            else:
                break

    def move_down(x, y_new):
        while True:
            if ((x, y_new) not in postion_of_every_pawn) and (y_new >= 0):
                move_path.append([x, y_new])
                y_new -= 1
            else:
                break

    def rook_move(x, y):
        move_left(x, y)
        move_right(x, y)
        move_up(x, y)
        move_down(x, y)

    def bishop_move (x,y):
        move_up_right(x,y)
        move_down_left(x, y)
        move_down_right(x, y)
        move_up_left(x, y)

    def queen_move(x, y):
        move_up_right(x,y)
        move_down_left(x, y)
        move_down_right(x, y)
        move_up_left(x, y)
        move_left(x, y)
        move_right(x, y)
        move_up(x, y)
        move_down(x, y)

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

    print(f"King: {king}")

    if king[0] in move_path:
        return print("Success")
    else:
        return print("Fail")