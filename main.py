import tkinter
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont


# Open file explorer window
def browse():
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select a File",
                                          filetypes=(("jpeg", "*.jpeg"),
                                                     ("jpg", "*.jpg"),
                                                     ("png", "*.png"))
                                          )
    label_open_file_location.configure(text=filename)


# Define
color_bg = "#F5F7F8"
color_fg = "#45474B"
color_tint1 = "#F4CE14"
color_tint2 = "#495E57"

# Window config
window = tkinter.Tk()
window.title("Watermark project")
window.geometry("400x280")
window.config(padx=20, pady=20, bg=color_bg)

# Labels
label_header = tkinter.Label(text="Place a watermark on your image", font=("Arial", 16), pady=10, bg=color_bg, fg=color_tint2)
label_open_file = tkinter.Label(text="File location:", font=("Arial", 12), pady=10, bg=color_bg, fg=color_fg)
label_open_file_location = tkinter.Label(text="..select image..", font=("Arial", 12), pady=10, bg=color_bg, fg=color_fg)
label_search_file = tkinter.Label(text="Choose a file:", font=("Arial", 12), pady=10, bg=color_bg, fg=color_fg)
label_watermark = tkinter.Label(text="Watermark text:", font=("Arial", 12), pady=10, bg=color_bg, fg=color_fg)

# Input
input_watermark = tkinter.Entry(font=("Arial", 12), width=20, bg=color_tint1, fg=color_tint2)

# Buttons
button_search_file = tkinter.Button(text="Browse", font=("Arial", 12), width=17, bg=color_tint1, command=browse)
button_replace = tkinter.Button(text="Place watermark", font=("Arial", 12), width=17, bg=color_tint1, command='')
button_exit = tkinter.Button(text="Exit", font=("Arial", 12), width=17, bg=color_tint2, fg=color_bg, command=exit)

# Grid setup
#   Row 0
label_header.grid(row=0, column=0, columnspan=2)
#   Row 1
label_open_file.grid(row=1, column=0)
label_open_file_location.grid(row=1, column=1)
#   Row 2
label_search_file.grid(row=2, column=0)
button_search_file.grid(row=2, column=1)
#   Row 3
label_watermark.grid(row=3, column=0)
input_watermark.grid(row=3, column=1)
#   Row 4
button_replace.grid(row=4, column=0)
#   Row 5
button_exit.grid(row=4, column=1)
# Stay on screen
window.mainloop()
