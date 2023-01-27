from tkinter import *  # framework to create GUI
import os

def restart():
    os.system("shutdown /r /t 1")   #1 son los segundos

def restart_time():
    os.system("shutdown /r /t 20")

def logoout():
    os.system("shutdown -1")

def shutdown():
    os.system("shutdown /s /t 1")



st = Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="Blue")

r_buttton = Button(st, text="Restart", font=(
    "Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=restart)  # tiene un + el cursor)   #me aparece un boton
r_buttton.place(x=150, y=60, height=50, width=200)


rt_buttton = Button(st, text="Restart Time", font=(
    "Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=restart_time)  # tiene un + el cursor)   #me aparece un boton
rt_buttton.place(x=150, y=170, height=50, width=200)


lo_buttton = Button(st, text="Log-Out", font=(
    "Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=logoout)  # tiene un + el cursor)   #me aparece un boton
lo_buttton.place(x=150, y=270, height=50, width=200)

sd_buttton = Button(st, text="ShutDown", font=(
    "Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=shutdown)  # tiene un + el cursor)   #me aparece un boton
sd_buttton.place(x=150, y=370, height=50, width=200)

st.mainloop()   # cuando corro esto en el cmd, me abre una ventanita de tk
