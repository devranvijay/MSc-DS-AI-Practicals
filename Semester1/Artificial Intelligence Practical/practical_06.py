def display(board):
  for i in range(0,9,3):
    print(board[i:i+3])
  print()
def move_title(board,direction):
  pos=board.index(0)
  if direction =='w' and pos >2:
    new_pos=pos-3
  elif direction =='s' and pos <6:
    new_pos=pos+3
  elif direction =='a' and pos%3 !=0:
    new_pos=pos-1
  elif direction =='d' and pos%3 !=2:
    new_pos=pos+1
  else:
    print("Invalid move!")
    return
  board[pos],board[new_pos]=board[new_pos],board[pos]
board=[1,2,3,
       4,0,6,
       7,5,8]
print("Number Puzzle Game")
print("Use W=Up,S=Down,A=Left,D=Right")
print("0 represents the empty space")
while board !=[1,2,3,4,5,6,7,8,0]:
  display(board)
  move_title(board,input("Enter your move:").lower())
print("Congratulations! Puzzle Solved")
display(board)
