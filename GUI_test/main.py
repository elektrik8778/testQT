import customtkinter
from pythonping import ping


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Аптеки")
        self.geometry("500x350")

        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.label1 = customtkinter.CTkLabel(self.frame,
                                             width=240,
                                             text="аптека_1",
                                             font=("Roboto", 14),
                                             bg_color="green",
                                             )
        self.label1.pack(pady=12,
                         padx=10,
                         )
        self.label2 = customtkinter.CTkLabel(self.frame,
                                             width=240,
                                             text="аптека_2",
                                             font=("Roboto", 14),
                                             bg_color="red",
                                             )
        self.label2.pack(pady=12,
                         padx=10,
                         )

        self.label1.after(1000, self.setColor())

    def setColor(self):
        if ping('192.168.0.104', timeout=1, count=1).success():
            self.label1.configure(bg_color="green")
        else:
            self.label1.configure(bg_color="red")
        self.after(5000, self.setColor)


if __name__ == "__main__":
    app = App()
    app.mainloop()

