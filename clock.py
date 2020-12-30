from datetime import datetime
import tkinter as tk

window = tk.Tk()

frm_time = tk.Frame(master= window,
                    relief = 'sunken',
                    borderwidth= 1,
                    bg = 'black')
frm_time.pack()

lbl_time = tk.Label(master = frm_time,
                bg = 'black',
                fg = 'lime',
                width = 10,
                height = 3
                )

lbl_time.pack(side = tk.LEFT)


frm_date = tk.Frame(master= window, relief = 'sunken', borderwidth= 1, bg = 'black')
frm_date.pack()

lbl_date = tk.Label(master = frm_date,
                bg = 'black',
                fg = 'lime',
                width = 10,
                height = 3
                )

lbl_date.pack(side = tk.LEFT)


#get the date and time together, then splits them into separate variables
def timer():
    fulldate = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    date, time = fulldate.split()
    year, month, day = date.split('-')
    hour, minute, second = time.split(':')

    lbl_time.config(text = hour + ':' + minute + ':' + second),
    lbl_date.config(text = day + '-' + month + '-' + year)

    lbl_time.after(1000, timer)

timer()

window.mainloop()