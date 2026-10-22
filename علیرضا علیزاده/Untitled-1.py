from tkinter import *
from tkinter import messagebox
from database import *

win = Tk()
win.title("login")
win.geometry("600x450")
win.resizable(False, False)

lname = Label(win, text=":نام خانوادگی ")
lname.place(x=220, y=20)
ent_lname = Entry(win, width=25)
ent_lname.place(x=40, y=20)

fname = Label(win, text=":نام")
fname.place(x=500, y=20)
ent_fname = Entry(win, width=25)
ent_fname.place(x=300, y=20)

password_lbl = Label(win, text=":رمز ورود ")
password_lbl.place(x=220, y=60)
ent_password = Entry(win, width=25, show="*")
ent_password.place(x=40, y=60)

course = Label(win, text=":نام دوره")
course.place(x=500, y=60)
ent_course = Entry(win, width=25)
ent_course.place(x=300, y=60)

lis = Listbox(win, width=50, height=12)
lis.place(x=40, y=130)

login_label = Label(win, text=":رمز عبور")
login_label.place(x=300, y=360)
ent_login_pass = Entry(win, width=40, show="*")
ent_login_pass.place(x=40, y=360)

lbl_message = Label(win, text="")
lbl_message.place(x=40, y=370)

def clear_ent():
    ent_fname.delete(0, END)
    ent_lname.delete(0, END)
    ent_password.delete(0, END)
    ent_course.delete(0, END)
    ent_login_pass.delete(0, END)
    lbl_message.config(text="")

def show_student():
    lis.delete(0, END)
    for i in show_all():
        text = f"{i[0]} {i[1]} {i[2]} {i[3]}"
        lis.insert(END, text)


def add_student():
    name = ent_fname.get().strip()
    family = ent_lname.get().strip()
    password = ent_password.get().strip()
    course = ent_course.get().strip()

    if not name or not family or not password:
        messagebox.showerror("خطا", "نام، نام خانوادگی و رمز الزامی هستند")
        return

    insert_record(name, family, course, password)
    show_student()
    clear_ent()


def delete_student_gui():
    if not lis.curselection():
        return
    answer = messagebox.askquestion("حذف", "آیا حذف شود؟")
    if answer == "yes":
        item = lis.get(lis.curselection())
        student_id = int(item.split()[0])
        delete_student(student_id)
        show_student()
        clear_ent()


def select_item(event):
    if not lis.curselection():
        return
    item = lis.get(lis.curselection())
    student_id = int(item.split()[0])
    student = get_student(student_id)

    clear_ent()
    ent_fname.insert(0, student[1])
    ent_lname.insert(0, student[2])
    ent_course.insert(0, student[3])
    ent_password.insert(0, student[4])


lis.bind("<<ListboxSelect>>", select_item)


def login_system():
    pwd = ent_login_pass.get().strip()
    if not pwd:
        lbl_message.config(text="رمز را وارد کنید")
        return

    result = login(pwd)
    if result:
        lbl_message.config(text="وارد شدید")
    else:
        lbl_message.config(text="اشتباه است")

def exit_program():
    answer = messagebox.askquestion("خروج", "آیا می‌خواهید خارج شوید؟")
    if answer == "yes":
        close_db()
        win.destroy()


Button(win, text="مشاهده همه", width=25, command=show_student).place(x=400, y=120)
Button(win, text="اضافه کردن", width=25, command=add_student).place(x=400, y=155)
Button(win, text="خالی کردن ورودی‌ها", width=25, command=clear_ent).place(x=400, y=190)
Button(win, text="حذف کردن", width=25, command=delete_student_gui).place(x=400, y=225)
Button(win, text="خروج", width=25, command=exit_program).place(x=400, y=260)
Button(win, text="ورود سامانه", width=25, command=login_system).place(x=400, y=295)

show_student()
win.mainloop()
