from Tkconstants import NE
import Tkinter
# from L07CanvasGridCoord import drawGrid

top = Tkinter.Tk()

frame = Tkinter.Frame(top, width=800, height=800)


def key_press(event):
	print "pressed", repr(event.char)

move_step = 3


def left_pressed(event):
	fx0, fy0, fx1, fy1 = canvas.coords(face)
	ex0, ey0, ex1, ey1 = canvas.coords(eye)
	canvas.coords(face, fx0 - move_step, fy0, fx1 - move_step, fy1)
	canvas.coords(eye, ex0 - move_step, ey0, ex1 - move_step, ey1)


def right_pressed(event):
	fx0, fy0, fx1, fy1 = canvas.coords(face)
	ex0, ey0, ex1, ey1 = canvas.coords(eye)
	canvas.coords(face, fx0 + move_step, fy0, fx1 + move_step, fy1)
	canvas.coords(eye, ex0 + move_step, ey0, ex1 + move_step, ey1)


def up_pressed(event):
	fx0, fy0, fx1, fy1 = canvas.coords(face)
	ex0, ey0, ex1, ey1 = canvas.coords(eye)
	canvas.coords(face, fx0, fy0 - move_step, fx1, fy1 - move_step)
	canvas.coords(eye, ex0, ey0 - move_step, ex1, ey1 - move_step)


def down_pressed(event):
	fx0, fy0, fx1, fy1 = canvas.coords(face)
	ex0, ey0, ex1, ey1 = canvas.coords(eye)
	canvas.coords(face, fx0, fy0 + move_step, fx1, fy1 + move_step)
	canvas.coords(eye, ex0, ey0 + move_step, ex1, ey1 + move_step)


def a_pressed(event):
	bx0, by0 = canvas.coords(ball)
	canvas.coords(ball, bx0 - move_step, by0)


def d_pressed(event):
	bx0, by0 = canvas.coords(ball)
	canvas.coords(ball, bx0 + move_step, by0)


def w_pressed(event):
	bx0, by0 = canvas.coords(ball)
	canvas.coords(ball, bx0, by0 - move_step)


def s_pressed(event):
	bx0, by0 = canvas.coords(ball)
	canvas.coords(ball, bx0, by0 + move_step)


top.bind("a", a_pressed)
top.bind("d", d_pressed)
top.bind("s", s_pressed)
top.bind("w", w_pressed)

top.bind("<Left>", left_pressed)
top.bind("<Right>", right_pressed)
top.bind("<Up>", up_pressed)
top.bind("<Down>", down_pressed)

frame.pack()

canvas = Tkinter.Canvas(frame, height=800, width=800, bg="white")

# canvas.bind("a", key_press)
filename = Tkinter.PhotoImage(file="ball.gif")
ball = canvas.create_image(150, 150, anchor=NE, image=filename)


def draw_monster(canvas, fx0, fy0):
	fw, fh = 80, 80
	ew, eh = 40, 30

	ex0 = fx0 + 30
	ey0 = fy0 - 20

	global face
	face = canvas.create_arc(fx0 - fw, fy0 - fh, fx0 + fw, fy0 + fh, start=0, extent=270, fill="red")

	global eye
	eye = canvas.create_oval(ex0, ey0, ex0 + ew, ey0 + eh, fill="blue")


draw_monster(canvas, 100, 100)

canvas.pack()
top.focus()
top.mainloop()
