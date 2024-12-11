from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
window = Tk()
window.title("Thông tin nhân viên")
window.geometry("840x280")

option=IntVar()
lbl = Label(window, text="Thông tin nhân viên", fg="black", font=("Arial",15))
lbl.grid(column=0, row =0)

chk1 = Checkbutton(window, text="Là khách hàng", variable=option, onvalue=1, offvalue=0)
chk1.grid(row=0, column=1, padx=10, pady=5, sticky="W")

chk2 = Checkbutton(window, text="Là nhà cung cấp", variable=option, onvalue=2, offvalue=0)
chk2.grid(row=0, column=2, padx=10, pady=5, sticky="W")

ma = Label(window, text="Mã",fg="black",font=("Arial",10))
ma.grid(column=0, row=1,sticky="W")
entry_ma = Entry(window, width=30)
entry_ma.grid(column=0, row=2, padx=5, pady=5,sticky="w")

ten = Label(window, text="Tên",fg="black",font=("Arial",10))
ten.grid(column=1, row=1,sticky="W")
entry_ten = Entry(window, width=30)
entry_ten.grid(column=1, row=2, padx=5, pady=5)

ten = Label(window, text="Ngày sinh",fg="black",font=("Arial",10))
ten.grid(column=2, row=1,sticky="W")
date_entry = DateEntry(window, width=20, foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
date_entry.grid(column=2, row=2,sticky="W")

gt =Label(window, text="Giới tính",fg="black",font=("Arial",10))
gt.grid(column=3,row=1,sticky="W")
gender = IntVar()
chk3 = Radiobutton(window, text="Nam", variable=gender, value=1)
chk3.grid(row=2, column=3, padx=10, pady=5, sticky="W")
chk4 = Radiobutton(window, text="Nữ", variable=gender, value=2)
chk4.grid(row=2, column=4, padx=10, pady=5, sticky="W")

donvi= Label(window, text="Đơn vị",fg="black",font=("Arial",10))
donvi.grid(column=0,row=3,sticky="W")
donv=StringVar()
don = ["D24CQCC01-B", "D24CQCC02-B", "D24CQCC03-B", "D24CQCC04-B"]
combobox = ttk.Combobox(window, textvariable=donv, values=don, width=27, font=("Arial", 12), state="readonly")
combobox.grid(row=4, column=0, padx=5, pady=5, sticky="W")

CM = Label(window, text="Số CMND",fg="black",font=("Arial",10))
CM.grid(column=1, row=3,sticky="W")
so_entry = Entry(window, width=30)
so_entry.grid(column=1, row=4,sticky="W")

CM = Label(window, text="Ngày cấp",fg="black",font=("Arial",10))
CM.grid(column=2, row=3,sticky="W")
dat_entry = DateEntry(window, width=20, foreground='white', borderwidth=2, date_pattern='dd/mm/yyyy')
dat_entry.grid(column=2, row=4,sticky="W")

CD = Label(window, text="Chức danh",fg="black",font=("Arial",10))
CD.grid(column=0, row=5,sticky="W")
T_entry = Entry(window, width=40)
T_entry.grid(column=0, row=6,sticky="W")

NC = Label(window, text="Nơi cấp",fg="black",font=("Arial",10))
NC.grid(column=1, row=5,sticky="W")
S_entry = Entry(window, width=40)
S_entry.grid(column=1, row=6,sticky="W")

def send_data():
    print("Thành công")
btn_send = Button(window, text="Gửi", command=send_data, width=10, height=2)
btn_send.grid(row=7, column=2, padx=10, pady=20)
window.mainloop()

