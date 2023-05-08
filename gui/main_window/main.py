from tkinter import (
    Toplevel,
    Frame,
    Canvas,
    Button,
    StringVar,
)
from controller import *
from gui.main_window.bm1.main import BM1



def mainWindow():
    MainWindow()


class MainWindow(Toplevel):
    global user

    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.title("Quan Ly Hoc Sinh - Nhom QNK")

        self.geometry("1012x506")
        self.configure(bg="#5E95FF")

        self.current_window = None
        self.current_window_label = StringVar()

        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.create_text(
            28.0,
            21.0,
            anchor="nw",
            text="QLHS - QNK",
            fill="#FFFFFF",
            font=("Montserrat Bold", 28 * -1),
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            215, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )

        # Add a frame rectangle
        self.sidebar_indicator = Frame(self, background="#FFFFFF")

        self.sidebar_indicator.place(x=0, y=133, height=47, width=7)

        self.bm1_btn = Button(
            self.canvas,
            text='BM1: Tiếp nhận học sinh',
            bg="#0958d9",
            fg="#FFFFFF",
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.bm1_btn, "BM1: Tiếp nhận học sinh"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.bm1_btn.place(x=7.0, y=130.0, width=210.0, height=45.0)

        # self.rooms_btn = Button(
        #     self.canvas,
        #     text='BM2: Lập danh sách lớp',
        #     bg="#0958d9",
        #     fg="#FFFFFF",
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: self.handle_btn_press(self.rooms_btn, "roo"),
        #     cursor='hand2', activebackground="#5E95FF",
        #     relief="flat",
        # )
        # self.rooms_btn.place(x=7.0, y=180.0, width=210.0, height=45.0)

        # self.guests_btn = Button(
        #     self.canvas,
        #     text='BM3: Tra cứu học sinh',
        #     bg="#0958d9",
        #     fg="#FFFFFF",
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: self.handle_btn_press(self.guests_btn, "gue"),
        #     cursor='hand2', activebackground="#5E95FF",
        #     relief="flat",
        # )
        # self.guests_btn.place(x=7.0, y=230.0, width=210.0, height=45.0)

        # self.guests_btn = Button(
        #     self.canvas,
        #     text='BM4: Nhận bảng điểm môn',
        #     bg="#0958d9",
        #     fg="#FFFFFF",
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: self.handle_btn_press(self.guests_btn, "gue"),
        #     cursor='hand2', activebackground="#5E95FF",
        #     relief="flat",
        # )
        # self.guests_btn.place(x=7.0, y=280.0, width=210.0, height=45.0)

        # self.guests_btn = Button(
        #     self.canvas,
        #     text='BM5: Lập báo cáo tổng kết môn',
        #     bg="#0958d9",
        #     fg="#FFFFFF",
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: self.handle_btn_press(self.guests_btn, "gue"),
        #     cursor='hand2', activebackground="#5E95FF",
        #     relief="flat",
        # )
        # self.guests_btn.place(x=7.0, y=330.0, width=210.0, height=45.0)

        # self.guests_btn = Button(
        #     self.canvas,
        #     text='BM5: Lập báo cáo tổng kết HK',
        #     bg="#0958d9",
        #     fg="#FFFFFF",
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: self.handle_btn_press(self.guests_btn, "gue"),
        #     cursor='hand2', activebackground="#5E95FF",
        #     relief="flat",
        # )
        # self.guests_btn.place(x=7.0, y=380.0, width=210.0, height=45.0)

        # self.guests_btn = Button(
        #     self.canvas,
        #     text='BM6: Thay đổi qui định',
        #     bg="#0958d9",
        #     fg="#FFFFFF",
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=lambda: self.handle_btn_press(self.guests_btn, "gue"),
        #     cursor='hand2', activebackground="#5E95FF",
        #     relief="flat",
        # )
        # self.guests_btn.place(x=7.0, y=430.0, width=210.0, height=45.0)


        self.heading = self.canvas.create_text(
            255.0,
            33.0,
            anchor="nw",
            text="Trang chủ",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )
        self.canvas.create_text(
            341.0,
            213.0,
            anchor="nw",
            text="Vui lòng chọn biểu mẫu",
            fill="#5E95FF",
            font=("Montserrat Bold", 36 * -1),
        )
        # Loop through windows and place them
        self.windows = {
            "BM1: Tiếp nhận học sinh": BM1(self),
        }
        
        # self.handle_btn_press(self.bm1_btn, "BM1: Tiếp nhận học sinh")
        self.sidebar_indicator.place(x=0, y=133)

        self.current_window.place(x=215, y=72, width=1013.0, height=506.0)

        self.current_window.tkraise()
        self.resizable(False, False)
        self.mainloop()

    def place_sidebar_indicator(self):
        pass

    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set ucrrent Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=215, y=72, width=1013.0, height=506.0)

        # Handle label change
        self.canvas.itemconfigure(self.heading, text=name)
