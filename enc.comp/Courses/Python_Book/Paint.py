from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser, messagebox
from tkinter.filedialog import asksaveasfilename
import PIL.ImageGrab as ImageGrab  # pip install pillow
color = 'white'
i = 1
color = 'white'
i = 1
class Paint:
    def __init__(self, root):
        self.root = root
        self.root.title('Paint')
        self.root.geometry('800x520')
        self.root.configure(background='white')
        self.root.resizable(0, 0)
        self.pen_color = '#000000'
        self.color_frame = LabelFrame(
            self.root,
            text='Color',
            font=('arial', 15, 'bold'),
            bd=5,
            relief=RIDGE,
            bg='white',
            )
        self.color_frame.place(x=0, y=0, width=70, height=185)
        Colors = [
            '#ff0000',
            '#ff4dd2',
            '#ffff33',
            '#000000',
            '#0066ff',
            '#660033',
            '#4dff4d',
            '#b300b3',
            '#00ffff',
            '#808080',
            '#99ffcc',
            '#336600',
            '#ff9966',
            '#ff99ff',
            '#00cc99',
            ]
        i = j = 0
        for color in Colors:
            Button(
                self.color_frame,
                bg=color,
                command=lambda col=color: self.select_color(col),
                width=3,
                bd=2,
                relief=RIDGE,
                ).grid(row=i, column=j)
            i += 1
            if i == 6:
                i = 0
                j = 1
      
        self.clear_sreen_button = Button(
            self.root,
            text='Clear',
            bd=4,
            relief=RIDGE,
            width=8,
            command=lambda : self.canvas.delete('all'),
            bg='white',
            )
        self.clear_sreen_button.place(x=0, y=217)
        self.save_button = Button(
            self.root,
            text='Save',
            bd=4,
            relief=RIDGE,
            width=8,
            command=self.save_paint,
            bg='white',
            )
        self.save_button.place(x=0, y=247)
        self.pen_size_scale_frame = LabelFrame(
            self.root,
            text='Size',
            bd=5,
            relief=RIDGE,
            bg='white',
            font=('arial', 15, 'bold'),
            )
        self.pen_size_scale_frame.place(x=0, y=310, height=200,
                width=70)
        self.pen_size = Scale(
            self.pen_size_scale_frame,
            orient='vertical',
            from_=50,
            to=0,
            command=None,
            length=170,
            )
        self.pen_size.set(10)
        self.pen_size.grid(row=0, column=1, padx=15)
        self.canvas = Canvas(
            self.root,
            bg='white',
            bd=5,
            relief='groove',
            height=500,
            width=700,
            )
        self.canvas.place(x=80, y=0)
        # Blind mouse dragging event to canvas
        self.canvas.bind('<B1-Motion>', self.paint)
        self.old_x = None
        self.old_y = None
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        def paint(self, event):
         global pen_color
         if self.old_x and self.old_y:
            # self.canvas.config(cursor='plus')
            self.canvas.create_line(
                self.old_x,
                self.old_y,
                event.x,
                event.y,
                width=self.pen_size.get(),
                fill=self.pen_color,
                capstyle=ROUND,
                smooth=TRUE,
                splinesteps=36,
                )
        self.old_x = event.x
        self.old_y = event.y
    def reset(self,*args):
        self.old_x = None
        self.old_y = None
    def select_color(self, col):
        global i
        i = 1
        self.pen_color = col
    def eraser(self):
        global color
        global i
        self.pen_color = color
        # self.canvas.config(cursor='dot')
        i = 0
    def canvas_color(self):
        global color
        color = colorchooser.askcolor()
        color = color[1]
        self.canvas.config(background=color)
    def save_paint(self):
        try:
            self.canvas.update()
            filename = asksaveasfilename(defaultextension='.jpg')
            print(filename)
            x = self.root.winfo_rootx() + self.canvas.winfo_x()
            # print(x)
            y = self.root.winfo_rooty() + self.canvas.winfo_y()
            # print(y)
            x1 = x + self.canvas.winfo_width()
            # print(x1)
            y1 = y + self.canvas.winfo_height()
            # print(y1)
            ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
            messagebox.showinfo('paint says ', 'image is saved as '
                                + str(filename))
        except:
            pass
if __name__ == '__main__':
    root = Tk()
    Paint(root)
    root.mainloop()
