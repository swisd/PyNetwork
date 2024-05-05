import customtkinter



customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("600x780")
app.title("LoopbackServerA1 Config")



def start_serv():
    print(f"Protocol: {optionmenu_1.get()}")
    print(f"TDM: {switch_3.get()}")
    print(f"IP Addr: {combobox_1.get()}")
    print(f"IP Log: {switch_1.get()}")
    print(f"Errors: {switch_2.get()}")
    print(f"IPCs: {switch_4.get()}")
    print(f"SDL: {checkbox_1.get()}")




frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)

label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text='General Settings', font=("Calibri", 24))
label_1.pack(pady=10, padx=10)

optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["HTTP/FTP", "HTTP", "FTP"])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("Protocol")

switch_3 = customtkinter.CTkSwitch(master=frame_1, text="Time/Data Measurements")
switch_3.pack(pady=10, padx=10)



label_2 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, text="IP/LOC", font=("Calibri", 24))
label_2.pack(pady=10, padx=10)


combobox_1 = customtkinter.CTkOptionMenu(frame_1, values=["127.0.0.1", "Pre-Assigned", "Other"])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("Default IP")

switch_1 = customtkinter.CTkSwitch(master=frame_1, text='IP Logging')
switch_1.pack(pady=10, padx=10)

label_3 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, font=("Calibri", 24), text="Console")
label_3.pack(pady=10, padx=10)

switch_2 = customtkinter.CTkSwitch(master=frame_1, text="Display Errors")
switch_2.pack(pady=10, padx=10)

switch_4 = customtkinter.CTkSwitch(master=frame_1, text="Display IPCs")
switch_4.pack(pady=10, padx=10)

label_5 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT, font=("Calibri", 24), text="Start Params")
label_5.pack(pady=10, padx=10)

text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "")


checkbox_1 = customtkinter.CTkCheckBox(master=frame_1, text='SDL')
checkbox_1.pack(pady=10, padx=10)





button_1 = customtkinter.CTkButton(master=frame_1, text="START", command=start_serv)
button_1.pack(pady=10, padx=10)

app.mainloop()