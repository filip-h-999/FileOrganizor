import customtkinter
import fOrganizor
from tkinter import filedialog 

def organizorGui():
    global setPath
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    win = customtkinter.CTk()
    win.geometry("410x200+800+200")
    win.title("FIle Organizor")
    # win.resizable(False,False)

    # win.wm_attributes("-transparentcolor", 'grey')

    frame = customtkinter.CTkFrame(master=win)
    frame.pack(pady=10, padx=10, fill="both", expand=True)

    lab = customtkinter.CTkLabel(master=frame, text="Which directory you want to organize?", font=('Roboto', 17))
    lab.pack(pady=12, padx=10)

    path = customtkinter.StringVar()
    txt = customtkinter.CTkEntry(master=frame, width=250, textvariable=path)
    txt.place(x=50, y=63)

    if not path.get(): # if path is empty
        txt.insert(0, r"Path: C:\Users\Documents...")

    def setPath():
        root.destroy()
        getPath = txt.get()
        correctPath = fOrganizor.organize(getPath)
        print(correctPath)
        # print(getPath)
        if correctPath == True:
            txt._entry.config(foreground="limegreen")

        if correctPath == False:
            txt._entry.config(foreground="red")

        # if organized == True:
        #     txt._entry.config(foreground="white")
        #     print("organized")
        
    def searchFolder():
        selected_directory = filedialog.askdirectory()
        path.set(selected_directory)
        txt._entry.config(foreground="limegreen")
        

    btn = customtkinter.CTkButton(master=frame, text="organize", command=permission_window)
    btn.place(x=125, y=120)

    btn2 = customtkinter.CTkButton(master=frame, text="📁", width=27, border_color='#565B5E', border_width=2, fg_color="#343638", command=searchFolder)
    btn2.place(x=305, y=63)

    win.mainloop()


def permission_window():
    global root
    customtkinter.set_appearance_mode("dark")

    root = customtkinter.CTk()
    root.geometry('410x130+800+230')
    root.title("Confirm")

    frame2 = customtkinter.CTkFrame(master=root)
    frame2.pack(pady=10, padx=10, fill="both", expand=True)

    lab = customtkinter.CTkLabel(master=frame2, text="Are you sure you want to organize this Folder?", font=('Roboto', 17))
    lab.pack(pady=12, padx=10)

    btn = customtkinter.CTkButton(master=frame2, text="yes", command=setPath)
    btn.place(x=35, y=65)

    btn2 = customtkinter.CTkButton(master=frame2, text="cancle", command=root.destroy, fg_color="red")
    btn2.place(x=220, y=65)

    root.mainloop()


organizorGui()