import re,datetime
from pathlib import Path
from tkinter import Frame, Canvas, Entry, StringVar, Text, Button, PhotoImage, messagebox
from controller import *

def bm1():
    BM1()

import controller as db_controller

# regular expression to validate the date format
date_regex = r'^\d{2}/\d{2}/\d{4}$'

class BM1(Frame):
    def __init__(self, parent, controller=None, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.data = {"full_name": StringVar(), "birthday": StringVar(), "email": StringVar(), "sex": StringVar(), "address": StringVar()}

        self.configure(bg="#FFFFFF")

        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=432,
            width=797,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )
        self.canvas.place(x=0, y=0)
        # self.canvas.create_text(
        #     36.0,
        #     43.0,
        #     anchor="nw",
        #     text="HotinGo was created by",
        #     fill="#5E95FF",
        #     font=("Montserrat Bold", 26 * -1),
        # )
        self.canvas.create_text(
            50.0,
            130.0,
            anchor="nw",
            text="Họ và tên",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )
        full_name_entry = Entry(
            self,
            textvariable=self.data["full_name"],
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        full_name_entry.place(x=50.0, y=150.0, width=180.0, height=25.0)

        self.canvas.create_text(
            290.0,
            130.0,
            anchor="nw",
            text="Giới tính",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )
        sex_entry = Entry(
            self,
            textvariable=self.data["sex"],
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        sex_entry.place(x=290.0, y=150.0, width=180.0, height=25.0)


        self.canvas.create_text(
            50.0,
            180.0,
            anchor="nw",
            text="Ngày sinh",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )
        birthday_entry = Entry(
            self,
            textvariable=self.data["birthday"],
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        birthday_entry.place(x=50.0, y=200.0, width=180.0, height=25.0)

        self.canvas.create_text(
            290.0,
            180.0,
            anchor="nw",
            text="Địa chỉ",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )
        address_entry = Entry(
            self,
            textvariable=self.data["address"],
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        address_entry.place(x=290.0, y=200.0, width=180.0, height=25.0)

        self.canvas.create_text(
            50.0,
            230.0,
            anchor="nw",
            text="Email",
            fill="#5E95FF",
            font=("Montserrat Bold", 14 * -1),
        )
        email_entry = Entry(
            self,
            textvariable=self.data["email"],
            bd=0,
            bg="#EFEFEF",
            highlightthickness=0,
            font=("Montserrat Bold", 18 * -1),
            foreground="#777777",
        )
        email_entry.place(x=50.0, y=250.0, width=180.0, height=25.0)

        save_btn = Button(
            self,
            text='Lưu',
            bg="#0958d9",
            fg="#FFFFFF",
            borderwidth=0,
            highlightthickness=0,
            command=self.save,
            relief="flat",
        )
        save_btn.place(x=160.0, y=300.0, width=190.0, height=50.0)
    
    def save(self):
        # check if any fields are empty
        for val in self.data.values():
            if val.get() == "":
                messagebox.showinfo("Error", "Vui lòng nhập đầy đủ thông tin")
                return
            
        # kiem tra QĐ1: Tuổi học sinh từ 15 đến 20.
        # Dinh dang DD/MM/YYYY
        birthday = self.data['birthday'].get()
        year = self.validate_and_split_date(birthday)
        if year == -1:
            return
        current_year = datetime.datetime.now().year
        if current_year - year <15 or current_year - year >20:
            messagebox.showinfo("Error", "Vui lòng nhập Tuổi học sinh từ 15 đến 20")
            return

        # luu vao database
        result = db_controller.add_student(
            *[self.data[label].get() for label in ("full_name", "birthday", "email", "sex", "address")]
        )

        if result:
            messagebox.showinfo("Success", "Thành công")
            # clear all fields
            for label in self.data.keys():
                self.data[label].set(0)
        else:
            messagebox.showerror(
                "Error", "Xảy ra lỗi"
            )



    # function to validate the date format and split the year
    def validate_and_split_date(self,date_str):
        if not re.match(date_regex, date_str):
            messagebox.showinfo("Error", "Sai định dạng ngày sinh, vui lòng sử dụng định dạng DD/MM/YYYY")
            return -1

        day, month, year = date_str.split('/')
        return int(year)