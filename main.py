import tkinter
from tkinter import filedialog, messagebox
import os
from PIL import Image, ImageFont, ImageFont

# Define
color_bg = "#F5F7F8"
color_fg = "#45474B"
color_tint1 = "#F4CE14"
color_tint2 = "#495E57"
filename = ''


# Open file explorer window
def browse():
    global filename
    filetypes = (
        ("jpeg", "*.jpeg"),
        ("jpg", "*.jpg"),
        ("png", "*.png"),
        ('All files', '*.*')
    )
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=filetypes)
    label_open_file_location.configure(text=os.path.basename(filename))


# Add watermark

# Window config
window = tkinter.Tk()
window.title("Watermark project")
# window.geometry("400x250")
window.config(padx=20, pady=20, bg=color_bg)

# Labels
label_header = tkinter.Label(text="Place a watermark on your image", font=("Arial", 16), pady=10, bg=color_bg, fg=color_tint2)
label_file_location = tkinter.Label(text="File location:", font=("Arial", 12), pady=10, bg=color_bg, fg=color_fg)
label_open_file_location = tkinter.Label(text="..select image..", font=("Arial", 12), pady=10, bg=color_bg, fg=color_fg)
label_browse_file = tkinter.Label(text="Choose a file:", font=("Arial", 12), pady=10, bg=color_bg, fg=color_fg)
label_watermark = tkinter.Label(text="Watermark text:", font=("Arial", 12), pady=10, bg=color_bg, fg=color_fg)

# Input
input_watermark = tkinter.Entry(font=("Arial", 12, "bold"), width=18, bg=color_tint1, fg=color_tint2)

# Buttons
button_browse_file = tkinter.Button(text="Browse", font=("Arial", 12), width=17, bg=color_tint1, command=browse)
button_watermark = tkinter.Button(text="Place watermark", font=("Arial", 12), width=17, bg=color_tint1, command='')
button_exit = tkinter.Button(text="Exit", font=("Arial", 12), width=17, bg=color_tint2, fg=color_bg, command=exit)

# Grid setup
#   Row 0
label_header.grid(row=0, column=0, columnspan=2)
#   Row 1
label_file_location.grid(row=1, column=0)
label_open_file_location.grid(row=1, column=1)
#   Row 2
label_browse_file.grid(row=2, column=0)
button_browse_file.grid(row=2, column=1)
#   Row 3
label_watermark.grid(row=3, column=0)
input_watermark.grid(row=3, column=1)
#   Row 4
button_watermark.grid(row=4, column=0)
#   Row 5
button_exit.grid(row=4, column=1)
# Stay on screen
window.mainloop()
