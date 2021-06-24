from tkinter import *

size_of_board = 600
number_of_dots = 6
symbol_size = (size_of_board / 3 - size_of_board / 8) / 2
symbol_thickness = 50
dot_color = '#7BC043'
player1_color = '#0492CF'
player1_color_light = '#67B0CF'
player2_color = '#EE4035'
player2_color_light = '#EE7E77'
Green_color = '#7BC043'
player_turn = 1;
player1_points = 0
player2_points = 0
marked_lines = []

# The following will help track which lines belong to a box and determining if a box has been completed.
box0 = [[1,0],[2,1],[1,2],[0,1]]
box1 = [[3,0],[4,1],[3,2],[2,1]]
box2 = [[5,0],[6,1],[5,2],[4,1]]
box3 = [[7,0],[8,1],[7,2],[6,1]]
box4 = [[9,0],[10,1],[9,2],[8,1]]
box5 = [[1,2],[2,3],[1,4],[0,3]]
box6 = [[3,2],[4,3],[3,4],[2,3]]
box7 = [[5,2],[6,3],[5,4],[4,3]]
box8 = [[7,2],[8,3],[7,4],[6,3]]
box9 = [[9,2],[10,3],[9,4],[8,3]]
box10 = [[1,4],[2,5],[1,6],[0,5]]
box11 = [[3,4],[4,5],[3,6],[2,5]]
box12 = [[5,4],[6,5],[5,6],[4,5]]
box13 = [[7,4],[8,5],[7,6],[6,5]]
box14 = [[9,4],[10,5],[9,6],[8,5]]
box15 = [[1,6],[2,7],[1,8],[0,7]]
box16 = [[3,6],[4,7],[3,8],[2,7]]
box17 = [[5,6],[6,7],[5,8],[4,7]]
box18 = [[7,6],[8,7],[7,8],[6,7]]
box19 = [[9,6],[10,7],[9,8],[8,7]]
box20 = [[1,8],[2,9],[1,10],[0,9]]
box21 = [[3,8],[4,9],[3,10],[2,9]]
box22 = [[5,8],[6,9],[5,10],[4,9]]
box23 = [[7,8],[8,9],[7,10],[6,9]]
box24 = [[9,8],[10,9],[9,10],[8,9]]
boxes = [box0, box1, box2, box3, box4, box5, box6, box7, box8, box9, box10, box11, box12, box13, box14, box15, box16, box17, box18, box19, box20, box21, box22, box23, box24]

distance_between_dots = size_of_board / number_of_dots
dot_width = .25 * distance_between_dots
edge_width = .1 * distance_between_dots

#Setup
window = Tk()
window.title("Dots and Lines 5x5")
canvas = Canvas(window, width = size_of_board, height = size_of_board)
canvas.pack()
window.mainloop(30)

def draw_board(c):
  #Grid
  for i in range(0, number_of_dots):
    canvas.create_line(50, 50+(i*distance_between_dots), 550,50+(i*distance_between_dots), fill = "gray", dash = (2,2))
    canvas.create_line(50+(i*distance_between_dots), 50, 50+(i*distance_between_dots), 550, fill='gray', dash=(2,2))

  for i in range(6):
      for j in range(6):
          start_x = i * 100 + 50
          end_x = j * 100 + 50
          canvas.create_oval(start_x - dot_width/2, end_x - dot_width/2, start_x + dot_width/2, end_x + dot_width/2, fill=dot_color, outline=dot_color)

def get_pos(x,y):
  print(x,y)
  xlog = (x - 25) // 50
  ylog = (y-25) // 50
  return [xlog, ylog]
  if isEven(xlog) == True:
    return "col"
  else:
    return "row"

def handle_click(e):
  get_pos(e.x,e.y)
  #if get_pos

def isEven(n):
  return n % 2 == 0

def mark_line(x,y,type):
  

draw_board(canvas)
window.bind("<Button-1>", handle_click)