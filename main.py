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

distance_between_dots = size_of_board / number_of_dots
dot_width = .25 * distance_between_dots
edge_width = .1 * distance_between_dots

#Setup
window = Tk()
window.title("Dots and Lines 5x5")
canvas = Canvas(window, width = size_of_board, height = size_of_board)
canvas.pack()
window.mainloop(30)

#Grid
for i in range(0, number_of_dots):
  canvas.create_line(50, 50+(i*distance_between_dots), 550,50+(i*distance_between_dots), fill = "gray", dash = (2,2))
  canvas.create_line(50+(i*distance_between_dots), 50, 50+(i*distance_between_dots), 550, fill='gray', dash=(2,2))