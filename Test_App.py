from tkinter import *
import tkinter as tk

import gspread
sa = gspread.service_account(filename="credentialsfile.json")
sh = sa.open("Tracks (after spring) (Responses)")
wks = sh.worksheet("Form Responses 1")
array = wks.get('A1:A90')

window = Tk()

window.wm_title("MyRankApp By Fares Hesham")
window.iconbitmap("icon.ico")
window.geometry("1000x800")
window.configure(bg = "#82dfff")
gpa_var = tk.StringVar()

def btn_clicked():
    x = gpa_var.get()
    count = 0
    while len(x) != 4:
        if len(x)==1:
            x = x + '.'
        else:
             x = x+'0'
             count += 1
    count = 0
    check = False
    for i in array:
        if array[count][0] == x:
            check = True
            if count == 11 or count == 12 or count == 13:
                canvas.itemconfig(result, text = f'Congratulations you are the {count}th!')
            elif count%10 == 1:
                canvas.itemconfig(result, text = f'Congratulations you are the {count}st!')
            elif count%10 == 2:
                canvas.itemconfig(result, text = f'Congratulations you are the {count}nd!')
            elif count%10 == 3:
                canvas.itemconfig(result, text = f'Congratulations you are the {count}rd!')
            else:
                canvas.itemconfig(result, text = f'Congratulations you are the {count}th!')
            break;
        count += 1
    if check == False:
        canvas.itemconfig(result, text = "Please Fill the Form and Try Again")
    count_c = wks.get('D2')
    count_e = wks.get('D3')
    canvas.itemconfig(track_c, text = f'Track C (Computer) = {count_c[0][0]}')
    canvas.itemconfig(track_e, text = f'Track E (Communication) = {count_e[0][0]}')

canvas = Canvas(
    window,
    bg = "#82dfff",
    height = 800,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    483.5, 464.0,
    image=background_img)

canvas.create_text(
    750.0, 250.0,
    text = "Enter your GPA (/4.00)",
    fill = "#415973",
    font = ("KellySlab-Regular", int(24.0)))

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    694.0, 312.0,
    image = entry0_img)

result = canvas.create_text(
    750.0, 400.0,
    text = "",
    fill = "#415973",
    font = ("KellySlab-Regular", int(24.0)))

track_c = canvas.create_text(
    750.0, 500.0,
    text = "Statistics will Load",
    fill = "#415973",
    font = ("KellySlab-Regular", int(24.0))) 
track_e = canvas.create_text(
    752.0, 550.0,
    text = "when you Submit...",
    fill = "#415973",
    font = ("KellySlab-Regular", int(24.0)))

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    694.0, 312.0,
    image = entry0_img)

entry0 = Entry(window, textvariable = gpa_var, bd = 0, bg = "#ffffff", highlightthickness = 0)
#track_c = Label(window, text = "Statistics will Load", font = ("KellySlab-Regular", int(24.0)), bg = '#82DFFF')
#track_e = Label(window, text = "when you Submit...", font = ("KellySlab-Regular", int(24.0)), bg = '#82DFFF')
#track_c.place(x = 500.0, y = 500)
#track_e.place(x=500.0, y = 550)
entry0.place(
    x = 561.0, y = 289,
    width = 266.0,
    height = 43)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 853, y = 289,
    width = 101,
    height = 46)


window.resizable(False, False)
window.mainloop()
