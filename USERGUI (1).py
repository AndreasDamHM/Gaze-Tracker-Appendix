import tkinter as tk
import time

# Create the main window
root = tk.Tk()

# Set the size of the window to the full screen
root.attributes('-fullscreen', True)

#another text box
text_box1 = tk.Text(root, height=1, font=("Helvetica", 24))
text_box1.pack(side=tk.TOP, fill=tk.X)
# Set the anchor to 'center' to make the text start in the middle
text_box1.tag_configure("center", justify='center')
text_box1.insert("1.0", "Blink to write text", "center")

# Create the text box at the top of the screen height=1 (only 1 line to write on)
text_box = tk.Text(root, height=1, font=("Helvetica", 36))
text_box.pack(side=tk.TOP, fill=tk.X)

#text in the center instead of on the right (optional)
text_box.tag_configure("center", justify='center')
text_box.insert("1.0", " ", "center")


# Create the 2x4 matrix
matrix_frame = tk.Frame(root)
matrix_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)


# Create a style for the labels
label_style = {"font": ("Helvetica", 20), "width": 24, "height": 12, "bg": "white"}

# Create the labels for the boxes in the matrix
label_a_g = tk.Label(matrix_frame, text='a-g', **label_style, highlightbackground="black", highlightthickness=2, )
label_a_g.grid(row=0, column=1)

label_h_o = tk.Label(matrix_frame, text='h-o', **label_style, highlightbackground="black", highlightthickness=2)
label_h_o.grid(row=0, column=2)

label_p_v = tk.Label(matrix_frame, text='p-v', **label_style, highlightbackground="black", highlightthickness=2)
label_p_v.grid(row=1, column=1)

label_w_å = tk.Label(matrix_frame, text='w-å', **label_style, highlightbackground="black", highlightthickness=2)
label_w_å.grid(row=1, column=2)

#create spacebar box
label_space = tk.Label(matrix_frame, text='space', **label_style, highlightbackground="black", highlightthickness=2)
label_space.grid(row=0, column=3)

#create delete box
label_delete1 = tk.Label(matrix_frame, text='delete', **label_style, highlightbackground="black", highlightthickness=2)
label_delete1.grid(row=1, column=3)

# Create 0-7 box
label_numbers = tk.Label(matrix_frame, text='0-7', **label_style, highlightbackground="black", highlightthickness=2)
label_numbers.grid(row=0, column=0)

#create 8, 9 and specials
label_special = tk.Label(matrix_frame, text='8, 9 and specials', **label_style, highlightbackground="black", highlightthickness=2)
label_special.grid(row=1, column=0)


#matrix for writing a to g
def a_to_g_matrix():
    # Create a new window
    matrix_window = tk.Toplevel(root)
    matrix_window.attributes('-fullscreen', True)

    # Create the 3x3 matrix
    matrix_frame = tk.Frame(matrix_window)
    matrix_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Add borders to the matrix
    matrix_frame.grid_columnconfigure((0,1,2), weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(0, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(1, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(2, weight=1, minsize=100)

    # Create the labels for the boxes in the matrix
    label_a = tk.Label(matrix_frame, text='a', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_a.grid(row=0, column=0, sticky='nsew')

    label_b = tk.Label(matrix_frame, text='b', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_b.grid(row=0, column=1, sticky='nsew')

    label_c = tk.Label(matrix_frame, text='c', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_c.grid(row=0, column=2, sticky='nsew')

    label_d = tk.Label(matrix_frame, text='d', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_d.grid(row=1, column=0, sticky='nsew')

    label_e = tk.Label(matrix_frame, text='e', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_e.grid(row=1, column=1, sticky='nsew')

    label_f = tk.Label(matrix_frame, text='f', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_f.grid(row=1, column=2, sticky='nsew')

    label_g = tk.Label(matrix_frame, text='g', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_g.grid(row=2, column=0, sticky='nsew')

    # Create the button to go back to the original GUI
    button_go_back = tk.Button(matrix_frame, text='Go back', command=matrix_window.destroy, font=("Helvetica", 28))
    button_go_back.grid(row=2, column=2, sticky='nsew')

    # Create the click events for the boxes in the matrix
    label_a.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'a'), matrix_window.destroy()))
    label_b.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'b'), matrix_window.destroy()))
    label_c.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'c'), matrix_window.destroy()))
    label_d.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'd'), matrix_window.destroy()))
    label_e.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'e'), matrix_window.destroy()))
    label_f.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'f'), matrix_window.destroy()))
    label_g.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'g'), matrix_window.destroy()))

#matrix for writing h to o
def h_to_o_matrix():
    # Create a new window
    matrix_window = tk.Toplevel(root)
    matrix_window.attributes('-fullscreen', True)

    # Create the 3x3 matrix
    matrix_frame = tk.Frame(matrix_window)
    matrix_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Add borders to the matrix
    matrix_frame.grid_columnconfigure((0,1,2), weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(0, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(1, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(2, weight=1, minsize=100)

    # Create the labels for the boxes in the matrix
    label_a = tk.Label(matrix_frame, text='h', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_a.grid(row=0, column=0, sticky='nsew')

    label_b = tk.Label(matrix_frame, text='i', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_b.grid(row=0, column=1, sticky='nsew')

    label_c = tk.Label(matrix_frame, text='j', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_c.grid(row=0, column=2, sticky='nsew')

    label_d = tk.Label(matrix_frame, text='k', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_d.grid(row=1, column=0, sticky='nsew')

    label_e = tk.Label(matrix_frame, text='l', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_e.grid(row=1, column=1, sticky='nsew')

    label_f = tk.Label(matrix_frame, text='m', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_f.grid(row=1, column=2, sticky='nsew')

    label_g = tk.Label(matrix_frame, text='n', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_g.grid(row=2, column=0, sticky='nsew')

    label_h = tk.Label(matrix_frame, text='o', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_h.grid(row=2, column=1, sticky='nsew')

    # Create the button to go back to the original GUI
    button_go_back = tk.Button(matrix_frame, text='Go back', command=matrix_window.destroy, font=("Helvetica", 28))
    button_go_back.grid(row=2, column=2, sticky='nsew')

    # Create the click events for the boxes in the matrix
    label_a.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'h'), matrix_window.destroy()))
    label_b.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'i'), matrix_window.destroy()))
    label_c.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'j'), matrix_window.destroy()))
    label_d.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'k'), matrix_window.destroy()))
    label_e.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'l'), matrix_window.destroy()))
    label_f.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'm'), matrix_window.destroy()))
    label_g.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'n'), matrix_window.destroy()))
    label_h.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'o'), matrix_window.destroy()))

#create matrix for p to v
def p_to_v_matrix():
    # Create a new window
    matrix_window = tk.Toplevel(root)
    matrix_window.attributes('-fullscreen', True)

    # Create the 3x3 matrix
    matrix_frame = tk.Frame(matrix_window)
    matrix_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Add borders to the matrix
    matrix_frame.grid_columnconfigure((0,1,2), weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(0, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(1, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(2, weight=1, minsize=100)

    # Create the labels for the boxes in the matrix
    label_a = tk.Label(matrix_frame, text='p', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_a.grid(row=0, column=0, sticky='nsew')

    label_b = tk.Label(matrix_frame, text='q', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_b.grid(row=0, column=1, sticky='nsew')

    label_c = tk.Label(matrix_frame, text='r', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_c.grid(row=0, column=2, sticky='nsew')

    label_d = tk.Label(matrix_frame, text='s', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_d.grid(row=1, column=0, sticky='nsew')

    label_e = tk.Label(matrix_frame, text='t', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_e.grid(row=1, column=1, sticky='nsew')

    label_f = tk.Label(matrix_frame, text='u', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_f.grid(row=1, column=2, sticky='nsew')

    label_g = tk.Label(matrix_frame, text='v', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_g.grid(row=2, column=0, sticky='nsew')

    # Create the button to go back to the original GUI
    button_go_back = tk.Button(matrix_frame, text='Go back', command=matrix_window.destroy, font=("Helvetica", 28))
    button_go_back.grid(row=2, column=2, sticky='nsew')

    # Create the click events for the boxes in the matrix
    label_a.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'p'), matrix_window.destroy()))
    label_b.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'q'), matrix_window.destroy()))
    label_c.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'r'), matrix_window.destroy()))
    label_d.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 's'), matrix_window.destroy()))
    label_e.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 't'), matrix_window.destroy()))
    label_f.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'u'), matrix_window.destroy()))
    label_g.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'v'), matrix_window.destroy()))

#create matrix for w to å
def w_to_å_matrix():
    # Create a new window
    matrix_window = tk.Toplevel(root)
    matrix_window.attributes('-fullscreen', True)

    # Create the 3x3 matrix
    matrix_frame = tk.Frame(matrix_window)
    matrix_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Add borders to the matrix
    matrix_frame.grid_columnconfigure((0,1,2), weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(0, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(1, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(2, weight=1, minsize=100)

    # Create the labels for the boxes in the matrix
    label_a = tk.Label(matrix_frame, text='w', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_a.grid(row=0, column=0, sticky='nsew')

    label_b = tk.Label(matrix_frame, text='x', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_b.grid(row=0, column=1, sticky='nsew')

    label_c = tk.Label(matrix_frame, text='y', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_c.grid(row=0, column=2, sticky='nsew')

    label_d = tk.Label(matrix_frame, text='z', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_d.grid(row=1, column=0, sticky='nsew')

    label_e = tk.Label(matrix_frame, text='æ', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_e.grid(row=1, column=1, sticky='nsew')

    label_f = tk.Label(matrix_frame, text='ø', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_f.grid(row=1, column=2, sticky='nsew')

    label_g = tk.Label(matrix_frame, text='å', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_g.grid(row=2, column=0, sticky='nsew')

    # Create the button to go back to the original GUI
    button_go_back = tk.Button(matrix_frame, text='Go back', command=matrix_window.destroy, font=("Helvetica", 28))
    button_go_back.grid(row=2, column=2, sticky='nsew')

    # Create the click events for the boxes in the matrix
    label_a.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'w'), matrix_window.destroy()))
    label_b.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'x'), matrix_window.destroy()))
    label_c.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'y'), matrix_window.destroy()))
    label_d.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'z'), matrix_window.destroy()))
    label_e.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'æ'), matrix_window.destroy()))
    label_f.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'ø'), matrix_window.destroy()))
    label_g.bind('<Button-1>', lambda event: (text_box.insert(tk.END, 'å'), matrix_window.destroy()))

#matrix for writing numbers 0 to 7
def numbers_matrix():
    # Create a new window
    matrix_window = tk.Toplevel(root)
    matrix_window.attributes('-fullscreen', True)

    # Create the 3x3 matrix
    matrix_frame = tk.Frame(matrix_window)
    matrix_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Add borders to the matrix
    matrix_frame.grid_columnconfigure((0,1,2), weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(0, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(1, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(2, weight=1, minsize=100)

    # Create the labels for the boxes in the matrix
    label_a = tk.Label(matrix_frame, text='0', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_a.grid(row=0, column=0, sticky='nsew')

    label_b = tk.Label(matrix_frame, text='1', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_b.grid(row=0, column=1, sticky='nsew')

    label_c = tk.Label(matrix_frame, text='2', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_c.grid(row=0, column=2, sticky='nsew')

    label_d = tk.Label(matrix_frame, text='3', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_d.grid(row=1, column=0, sticky='nsew')

    label_e = tk.Label(matrix_frame, text='4', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_e.grid(row=1, column=1, sticky='nsew')

    label_f = tk.Label(matrix_frame, text='5', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_f.grid(row=1, column=2, sticky='nsew')

    label_g = tk.Label(matrix_frame, text='6', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_g.grid(row=2, column=0, sticky='nsew')

    label_h = tk.Label(matrix_frame, text='7', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_h.grid(row=2, column=1, sticky='nsew')

    # Create the button to go back to the original GUI
    button_go_back = tk.Button(matrix_frame, text='Go back', command=matrix_window.destroy, font=("Helvetica", 28))
    button_go_back.grid(row=2, column=2, sticky='nsew')

    # Create the click events for the boxes in the matrix
    label_a.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '0'), matrix_window.destroy()))
    label_b.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '1'), matrix_window.destroy()))
    label_c.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '2'), matrix_window.destroy()))
    label_d.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '3'), matrix_window.destroy()))
    label_e.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '4'), matrix_window.destroy()))
    label_f.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '5'), matrix_window.destroy()))
    label_g.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '6'), matrix_window.destroy()))
    label_h.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '7'), matrix_window.destroy()))


#matrix for writing numbers 8, 9 and special signs
def special_matrix():
    # Create a new window
    matrix_window = tk.Toplevel(root)
    matrix_window.attributes('-fullscreen', True)

    # Create the 3x3 matrix
    matrix_frame = tk.Frame(matrix_window)
    matrix_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    # Add borders to the matrix
    matrix_frame.grid_columnconfigure((0,1,2), weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(0, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(1, weight=1, minsize=100)
    matrix_frame.grid_rowconfigure(2, weight=1, minsize=100)

    # Create the labels for the boxes in the matrix
    label_a = tk.Label(matrix_frame, text='8', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_a.grid(row=0, column=0, sticky='nsew')

    label_b = tk.Label(matrix_frame, text='9', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_b.grid(row=0, column=1, sticky='nsew')

    label_c = tk.Label(matrix_frame, text='!', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_c.grid(row=0, column=2, sticky='nsew')

    label_d = tk.Label(matrix_frame, text='?', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_d.grid(row=1, column=0, sticky='nsew')

    label_e = tk.Label(matrix_frame, text='-', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_e.grid(row=1, column=1, sticky='nsew')

    label_f = tk.Label(matrix_frame, text='+', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_f.grid(row=1, column=2, sticky='nsew')

    label_g = tk.Label(matrix_frame, text='=', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_g.grid(row=2, column=0, sticky='nsew')

    label_h = tk.Label(matrix_frame, text='@', bd=1, relief=tk.RIDGE, font=("Helvetica", 28))
    label_h.grid(row=2, column=1, sticky='nsew')

    # Create the button to go back to the original GUI
    button_go_back = tk.Button(matrix_frame, text='Go back', command=matrix_window.destroy, font=("Helvetica", 28))
    button_go_back.grid(row=2, column=2, sticky='nsew')

    # Create the click events for the boxes in the matrix
    label_a.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '8'), matrix_window.destroy()))
    label_b.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '9'), matrix_window.destroy()))
    label_c.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '!'), matrix_window.destroy()))
    label_d.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '?'), matrix_window.destroy()))
    label_e.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '-'), matrix_window.destroy()))
    label_f.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '+'), matrix_window.destroy()))
    label_g.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '='), matrix_window.destroy()))
    label_h.bind('<Button-1>', lambda event: (text_box.insert(tk.END, '@'), matrix_window.destroy()))

#delete the latest character
def delete_text():
    if text_box.get("1.0", "end-1c"):
        #split str value into two seperate values using split() method, and only convert column to an integer.
        current_pos = text_box.index(tk.INSERT).split('.')
        current_col = int(current_pos[1])
        text_box.delete(f"{current_pos[0]}.{current_col - 1}", tk.INSERT)
        #center the text again
        #text_box.insert("1.0", " ", "center")

# Create the click event for the a to g matrix
label_a_g.bind('<Button-1>', lambda event: a_to_g_matrix())

#create the click event for the h to o matrix
label_h_o.bind('<Button-1>', lambda event: h_to_o_matrix())

#create the click event for the p to v matrix
label_p_v.bind('<Button-1>', lambda event: p_to_v_matrix())

#create the click event for the w to å matrix
label_w_å.bind('<Button-1>', lambda event: w_to_å_matrix())

#create the click event for the 0 to 7 matrix
label_numbers.bind('<Button-1>', lambda event: numbers_matrix())

#create the click event for the numbers 8 and 9 and special signs.
label_special.bind('<Button-1>', lambda event: special_matrix())

#clicking space creates a space
label_space.bind('<Button-1>', lambda event: (text_box.insert(tk.END, ' ')))

#clicking on the delete box deletes the latest sign
label_delete1.bind('<Button-1>', lambda event: delete_text())


time.sleep(4)

#run the main loop
root.mainloop()