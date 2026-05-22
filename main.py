from tkinter import *
from tkinter import messagebox

# 🌊 Ocean Theme Colors
bg_color = "#061a2b"
button_color = "#00d4ff"
text_color = "#e6f7ff"

def check_winner():
    win_combos = [
        (button1, button2, button3),
        (button4, button5, button6),
        (button7, button8, button9),
        (button1, button5, button9),
        (button3, button5, button7),
        (button1, button4, button7),
        (button2, button5, button8),
        (button3, button6, button9)
    ]

    for b1, b2, b3 in win_combos:
        if b1["text"] == b2["text"] == b3["text"] != " ":
            messagebox.showinfo("Tic Tac Toe", f"Player {b1['text']} won!")
            disable_buttons()
            return True
    return False


def disable_buttons():
    for b in buttons:
        b.config(state=DISABLED)


def Button_click(button):
    global x_o, flag

    if button["text"] == " ":
        if x_o:
            button["text"] = "X"
            button["fg"] = "black"
            x_o = False
        else:
            button["text"] = "O"
            button["fg"] = "black"
            x_o = True

        flag += 1
        check_winner()
    else:
        messagebox.showinfo("Tic Tac Toe", "Already played!")


main = Tk()
main.title("Tic Tac Toe 🌊 Ocean Theme")
main.configure(bg=bg_color)

x_o = True
flag = 0

buttons = []

def make_button(command):
    return Button(main,
                  text=" ",
                  font=("Arial", 60, "bold"),
                  bg=button_color,
                  fg="black",
                  activebackground="#00ffa3",
                  width=3,
                  command=command)

# 🌊 Buttons
button1 = make_button(lambda: Button_click(button1))
button1.grid(row=0, column=0)
buttons.append(button1)

button2 = make_button(lambda: Button_click(button2))
button2.grid(row=0, column=1)
buttons.append(button2)

button3 = make_button(lambda: Button_click(button3))
button3.grid(row=0, column=2)
buttons.append(button3)

button4 = make_button(lambda: Button_click(button4))
button4.grid(row=1, column=0)
buttons.append(button4)

button5 = make_button(lambda: Button_click(button5))
button5.grid(row=1, column=1)
buttons.append(button5)

button6 = make_button(lambda: Button_click(button6))
button6.grid(row=1, column=2)
buttons.append(button6)

button7 = make_button(lambda: Button_click(button7))
button7.grid(row=2, column=0)
buttons.append(button7)

button8 = make_button(lambda: Button_click(button8))
button8.grid(row=2, column=1)
buttons.append(button8)

button9 = make_button(lambda: Button_click(button9))
button9.grid(row=2, column=2)
buttons.append(button9)

main.mainloop()