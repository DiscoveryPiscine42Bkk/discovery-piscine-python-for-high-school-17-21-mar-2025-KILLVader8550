move_path = []

class Move_pattern:
    def __init__ (self, x, y, board_size, postion_of_every_pawn, ):
        self.x = x
        self.y = y
        self.board_size = board_size
        self.position_of_every_pawn = postion_of_every_pawn
    
    def move_up_right(self, x_new, y_new):
        while True:
            if ((x_new,y_new) not in self.postion_of_every_pawn) and (y_new <= self.board_size) and (x_new <= self.board_size):
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
            if ((x_new,y_new) not in postion_of_every_pawn) and (y_new >= 0) and (x_new <= board_size):
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
    def move_right(x_new):
        while True:
            if ((x_new,y) not in postion_of_every_pawn) and (x_new <= board_size):
                move_path.append([x_new,y])
                x_new += 1
            else:
                break

    def move_left(x_new):
        while True:
            if ((x_new,y) not in postion_of_every_pawn) and (x_new >= 0):
                move_path.append([x_new,y])
                x_new -= 1
                print(x_new,y)
            else:
                break

    def move_up(y_new):
        while True:
            if ((x,y_new) not in postion_of_every_pawn) and (y_new <= board_size):
                move_path.append([x,y_new])
                y_new += 1
            else:
                break

    def move_down(y_new):
        while True:
            if ((x, y_new) not in postion_of_every_pawn) and (y_new >= 0):
                move_path.append([x, y_new])
                y_new -= 1
            else:
                break

