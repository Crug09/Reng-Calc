from this import s
from tkinter import *
from tkinter import ttk
from tkinter.tix import TEXT
from PIL import ImageTk, Image
from tkinter import constants
import math

dark="#3b4f55"

root = Tk()
root.title('RENG')
root.geometry("1280x720")
root.configure(bg=dark)
root.resizable(False, False)


notebook = ttk.Notebook(root, width=1920, height=1080)
notebook.pack()

dc = Frame(notebook, width=1920, height=1080, bg=dark)
dc.pack(fill="both", expand=1)

# For App
# img_dc1 = Image.open(f'dc_chart.jpg')

# For Testing 
img_dc1 = Image.open("Reng Calc\dc_chart.jpg")
img_dc2 = ImageTk.PhotoImage(img_dc1)
dc_chart = Label(dc, image = img_dc2)
dc_chart.pack(anchor=E)



ox=50
oy=100
os=60

pi = Text(dc, width=20, height=1)
ei = Text(dc, width=20, height=1)
ii = Text(dc, width=20, height=1)
ri = Text(dc, width=20, height=1)
# pi = Entry(dc)
# ei = Entry(dc)
# ii = Entry(dc)
# ri = Entry(dc)

pi.place(x=ox,y=oy)
ei.place(x=ox,y=oy+os)
ii.place(x=ox,y=oy+(os*2))
ri.place(x=ox,y=oy+(os*3))

# pi.insert(INSERT, "hello")

p = Label(dc, text="Watts:", bg=dark).place(x=0, y=oy)
e = Label(dc, text="Volts:", bg=dark).place(x=0, y=oy+os)
i = Label(dc, text="Amps:", bg=dark).place(x=0, y=oy+(os*2))
r = Label(dc, text="Ohms:", bg=dark).place(x=0, y=oy+(os*3))


ox2=220

def clear_dc():
    pi.delete("1.0","end")
    ei.delete("1.0","end")
    ii.delete("1.0","end")
    ri.delete("1.0","end")
    global pv, ev,iv, rv
    pv.set(dc_p[0])
    ev.set(dc_e[0])
    iv.set(dc_i[0])
    rv.set(dc_r[0])

dc_p = [
    "watts (W)",
    "mircowatts (μW)",
    "milliwatts (mW)",
    "watts (W)",
    "kilowatts (kW)",
    "megawatts (MW)"
]
dc_e = [
    "volts (V)",
    "mircovolts (μV)",
    "millivolts (mV)",
    "volts (V)",
    "kilovolts (kV)",
    "megavolts (MV)"
]
dc_i = [
    "amps (A)",
    "mircoamps (μA)",
    "milliamps (mA)",
    "amps (A)",
    "kiloamps (kA)",
    "megaamps (MA)"
]
dc_r = [
    "ohms (Ω)",
    "ohms (Ω)",
    "kiloohms (kΩ)",
    "megaohms (MΩ)"
]



pv = StringVar()
pv.set(dc_p[0])
pd = ttk.OptionMenu(dc, pv, *dc_p)

ev = StringVar()
ev.set(dc_e[0])
ed = ttk.OptionMenu(dc, ev, *dc_e)

iv = StringVar()
iv.set(dc_i[0])
id = ttk.OptionMenu(dc, iv, *dc_i)

rv = StringVar()
rv.set(dc_r[0])
rd = ttk.OptionMenu(dc, rv, *dc_r)



def calc_dc():
    p_i = pi.get(1.0, END + "-1c")
    e_i = ei.get(1.0, END + "-1c")
    i_i = ii.get(1.0, END + "-1c")
    r_i = ri.get(1.0, END + "-1c")

    drop = 0

    def size():
        global s
        if "mirco" in drop:
            s = 0.000001
        elif "milli" in drop:
            s = 0.001
        elif "kilo" in drop:
            s = 1000
        elif "mega" in drop:
            s = 1000000
        else:
            s = 1


    if p_i:
        p_i = float(p_i)
        drop = pv.get()
        size()
        p_i = p_i * s

    if e_i:
        e_i = float(e_i)
        drop = ev.get()
        size()
        e_i = e_i * s

    if i_i:
        i_i = float(i_i)
        drop = iv.get()
        size()
        i_i = i_i * s

    if r_i:
        r_i = float(r_i)
        drop = rv.get()
        size()
        r_i = r_i * s


    if p_i == "":
        if e_i and r_i:
            p_i = ((e_i)*e_i)/r_i
            pi.insert(INSERT, p_i)
        elif e_i and i_i:
            p_i = (e_i * i_i)
            pi.insert(INSERT, p_i)
        elif r_i and i_i:
            p_i = (r_i * i_i * i_i)
            pi.insert(INSERT, p_i)
    if e_i == "":
        if p_i and r_i:
            e_i = math.sqrt((p_i * r_i))
            ei.insert(INSERT, e_i)
        elif p_i and i_i:
            e_i = (p_i / i_i)
            ei.insert(INSERT, e_i)
        elif r_i and i_i:
            e_i = (r_i * i_i)
            ei.insert(INSERT, e_i)
    if i_i == "":
        if p_i and r_i:
            i_i = math.sqrt(p_i / r_i)
            ii.insert(INSERT, i_i)
        elif p_i and e_i:
            i_i = (p_i / i_i)
            ii.insert(INSERT, i_i)
        elif e_i and r_i:
            i_i = (e_i / r_i)
            ii.insert(INSERT, i_i)
    if r_i == "":
        if p_i and i_i:
            r_i = (p_i / (i_i * i_i))
            ri.insert(INSERT, r_i)
        elif e_i and p_i:
            r_i = ((e_i * e_i) / p_i)
            ri.insert(INSERT, r_i)
        elif e_i and  i_i:
            r_i = (e_i / i_i)
            ri.insert(INSERT, r_i)


pd.place(x=ox2,y=oy)
ed.place(x=ox2,y=oy+os)
id.place(x=ox2,y=oy+(os*2))
rd.place(x=ox2,y=oy+(os*3))

del_dc = ttk.Button(dc, text="Clear", command = clear_dc)
del_dc.place(x=160, y=310)

calc_dc= Button(dc, text="Calculate", command= calc_dc)
calc_dc.place(x=100, y=310)

notebook.add(dc, text="DC Calculator")
root.mainloop()
 