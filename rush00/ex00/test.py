
text = """\
R...
.K..
.P..
....\
"""

rook = []
king =  []
pawn = []
bishop = []
queen = []

arr = [list(line) for line in text.splitlines() if line.strip()]
print(arr)
print(arr[1])
print(len(arr[1]))

for row in arr:
    print(row)
    match row:
        case _ if(len(row) != len(arr)):
            #return "error"
            print("error")
        case _ if(len(row) > 20):
            #return "error"
            print("error")

#row as x
#column as y
for x in range(len(arr)):
    row = arr[x]
    for y in range (len(row)):
        match row[y].upper():
            case "R":
                rook.append((x, y))
            case "K":
                king.append((x, y))
            case "P":
                pawn.append((x, y))
            case "B":
                bishop.append((x, y))
            case _:
                pass

if len(king) > 1:
    #return "error"
    print("error")

print(rook, king, bishop, pawn)
print(arr)