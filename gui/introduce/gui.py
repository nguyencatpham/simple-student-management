from tkinter import Toplevel, Canvas, Entry, Button
from controller import *
from ..main_window.main import mainWindow

def introduceWindow():
    Intro()


class Intro(Toplevel):
    def gotoMainWindow(self):
        self.destroy()
        mainWindow()

    def __init__(self, *args, **kwargs):

        Toplevel.__init__(self, *args, **kwargs)

        self.title("Quan Ly Hoc Sinh - Nhom QNK")

        self.geometry("1012x506")
        self.configure(bg="#5E95FF")

        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=506,
            width=1012,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            469.0, 0.0, 1012.0, 506.0, fill="#FFFFFF", outline=""
        )

        entry_1 = Entry(self.canvas, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry_1.place(x=568.0, y=294.0, width=336.0, height=0)

        entry_2 = Entry(self.canvas, bd=0, bg="#EFEFEF", highlightthickness=0)
        entry_2.place(x=568.0, y=192.0, width=336.0, height=0)

        self.canvas.create_text(
            553.0,
            66.0,
            anchor="nw",
            text="ĐỀ TÀI: QUẢN LÝ HỌC SINH",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        # left
        self.canvas.create_text(
            85.0,
            77.0,
            anchor="nw",
            text="Nhom QNK",
            fill="#FFFFFF",
            font=("Montserrat Bold", 50 * -1),
        )
        self.canvas.create_text(
            90.0,
            150.0,
            anchor="nw",
            text="MÔN : Lập Trình Nâng Cao",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )
        self.canvas.create_text(
            90.0,
            179.0,
            anchor="nw",
            text="MÃ MÔN HỌC: 1001074620",
            fill="#FFFFFF",
            font=("Montserrat Regular", 18 * -1),
        )
        self.canvas.create_text(
            90.0,
            431.0,
            anchor="nw",
            text="HỌC KỲ: 5 – NĂM HỌC: 2022-2023",
            fill="#FFFFFF",
            font=("Montserrat Bold", 18 * -1),
        )
        
        # right
        self.canvas.create_text(
            553.0,
            109.0,
            anchor="nw",
            text="GVHD: Lương Trần Hy Hiển",
            fill="#333333",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            553.0,
            130.0,
            anchor="nw",
            text="Trưởng nhóm: Nghiêm Phúc Minh Quân - 2100010315",
            fill="#333333",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            553.0,
            150.0,
            anchor="nw",
            text="Hồ Hào Kiệt - 2100004816",
            fill="#333333",
            font=("Montserrat Bold", 16 * -1),
        )
        self.canvas.create_text(
            553.0,
            170.0,
            anchor="nw",
            text="Chu Huỳnh Anh Khoa - 2100006053",
            fill="#333333",
            font=("Montserrat Bold", 16 * -1),
        )
        self.canvas.create_text(
            553.0,
            190.0,
            anchor="nw",
            text="Trịnh Văn Nguyên - 2100004998",
            fill="#333333",
            font=("Montserrat Bold", 16 * -1),
        )
        button_1 = Button(
            self.canvas,
            text='Truy cập',
            bg="#0958d9",
            fg="#FFFFFF",
            borderwidth=0,
            highlightthickness=0,
            command=self.gotoMainWindow,
            relief="flat",
        )
        button_1.place(x=641.0, y=412.0, width=190.0, height=48.0)

        self.resizable(False, False)
        self.mainloop()
