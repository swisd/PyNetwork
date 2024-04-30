import colorsys
from tkinter import *
from tkinter import messagebox

# usage.
# run this script, in particular the function convert_rgb_to_hsv()
# edit red, green, blue


def convert_rgb_to_hsv():
    # rgb normal: range (0-255, 0-255, 0.255)
    red = 40
    green = 32
    blue = 28

    # get rgb percentage: range (0-1, 0-1, 0-1 )
    red_percentage = red / float (255)
    green_percentage = green / float (255)
    blue_percentage = blue / float (255)

    # get hsv percentage: range (0-1, 0-1, 0-1)
    color_hsv_percentage = colorsys.rgb_to_hsv (red_percentage, green_percentage, blue_percentage)
    print ('color_hsv_percentage: ', color_hsv_percentage)

    # get normal hsv: range (0-360, 0-255, 0-255)
    color_h = round (360 * color_hsv_percentage[0])
    color_s = round (255 * color_hsv_percentage[1])
    color_v = round (255 * color_hsv_percentage[2])
    color_hsv = (color_h , color_s, color_v)

    print ('color_hsv: ', color_hsv)


# INVOCATE MAIN FUNCTION
convert_rgb_to_hsv ( )

ws = Tk()
ws.title('PythonGuides')
ws.geometry('200x200')

def viewSelected():
    choice = var.get ( )
    if choice == 1:
        output = "RGBA"

    elif choice == 2:
        output = "HSV"

    elif choice == 3:
        output = "HSL"
    else:
        output = "Invalid selection"

var = IntVar( )
Radiobutton(ws, text="RGBA", variable=var, value=1, command=viewSelected).pack ( )
Radiobutton(ws, text="HSV", variable=var, value=2, command=viewSelected).pack ( )
Radiobutton(ws, text="HSL", variable=var, value=3, command=viewSelected).pack ( )
