from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
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

#DC TAB


img_dc1 = Image.open("dc_chart.jpg")
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

pi.place(x=ox,y=oy)
ei.place(x=ox,y=oy+os)
ii.place(x=ox,y=oy+(os*2))
ri.place(x=ox,y=oy+(os*3))


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


#watts
pv = StringVar()
pv.set(dc_p[0])
pd = ttk.OptionMenu(dc, pv, *dc_p)

#volts
ev = StringVar()
ev.set(dc_e[0])
ed = ttk.OptionMenu(dc, ev, *dc_e)

#amps
iv = StringVar()
iv.set(dc_i[0])
id = ttk.OptionMenu(dc, iv, *dc_i)

#ohms
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






dci = Frame(notebook, width=1920, height=1080, bg=dark)
dci.pack(fill="both", expand=1)

Inter = ttk.Notebook(dci, width=1920, height=1080)
Inter.pack()



single = Frame(Inter, width=1920, height=1080, bg=dark)
single.pack()
series = Frame(Inter, width=1920, height=1080, bg=dark)
series.pack()
par = Frame(Inter, width=1920, height=1080, bg=dark)
par.pack()

#single_dc
img_single1 = Image.open("single.png")
img_single2 = ImageTk.PhotoImage(img_single1)
single_chart = Label(single, image = img_single2)
single_chart.pack()





def clear_single():
    single_v.delete("1.0","end")
    single_a.delete("1.0","end")
    single_o.delete("1.0","end")
    global pv, ev,iv, rv
    e_sin.set(dc_e[0])
    i_sin.set(dc_i[0])
    r_sin.set(dc_r[0])


#Volts
single_volts = Label(single, text="Volts:", bg=dark)
single_volts.place(x=260, y= 285)

single_v = Text(single, width=10, height=1)
single_v.place(x=300, y=285)

e_sin = StringVar()
e_sin.set(dc_e[0])
ed_sin = ttk.OptionMenu(single, e_sin, *dc_e)
ed_sin.place(x=390, y=285)

#Amps
single_amps = Label(single, text="Amps:", bg=dark)
single_amps.place(x=490, y=520)

single_a = Text(single, width=10, height=1)
single_a.place(x=530, y=520)

i_sin = StringVar()
i_sin.set(dc_i[0])
id_sin = ttk.OptionMenu(single, i_sin, *dc_i)
id_sin.place(x=620, y=520)

#ohms
single_ohms = Label(single, text="Ohms:", bg=dark)
single_ohms.place(x=770, y=285)

single_o = Text(single, width=10, height=1)
single_o.place(x=810, y=285)

r_sin = StringVar()
r_sin.set(dc_r[0])
rd_sin = ttk.OptionMenu(single, r_sin, *dc_r)
rd_sin.place(x=900, y=285)



def calc_single():
    #volts
    e_i = single_v.get(1.0, END + "-1c")
    #amps
    i_i = single_a.get(1.0, END + "-1c")
    #ohms
    r_i = single_o.get(1.0, END + "-1c")

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


    if e_i:
        e_i = float(e_i)
        drop = e_sin.get()
        size()
        e_i = e_i * s

    if i_i:
        i_i = float(i_i)
        drop = i_sin.get()
        size()
        i_i = i_i * s

    if r_i:
        r_i = float(r_i)
        drop = r_sin.get()
        size()
        r_i = r_i * s



    if e_i == "":
        if r_i and i_i:
            e_i = (r_i * i_i)
            single_v.insert(INSERT, e_i)

    if i_i == "":
        if e_i and r_i:
            i_i = (e_i / r_i)
            single_a.insert(INSERT, i_i)
    if r_i == "":
        if e_i and  i_i:
            r_i = (e_i / i_i)
            single_o.insert(INSERT, r_i)


del_dc_single = ttk.Button(single, text="Clear", command = clear_single)
del_dc_single.place(x=610, y=285)

calc_dc_single= Button(single, text="Calculate", command= calc_single)
calc_dc_single.place(x=550, y=285)






#series_dc
img_series1 = Image.open("series.png")
img_series2 = ImageTk.PhotoImage(img_series1)
series_chart = Label(series, image = img_series2)
series_chart.pack()



def clear_series():
    series_v1.delete("1.0","end")
    series_v2.delete("1.0","end")
    series_v3.delete("1.0","end")
    series_a.delete("1.0","end")
    series_o1.delete("1.0","end")
    series_o2.delete("1.0","end")
    e_ser1.set(dc_e[0])
    e_ser2.set(dc_e[0])
    e_ser3.set(dc_e[0])
    i_ser.set(dc_i[0])
    r_ser1.set(dc_r[0])
    r_ser2.set(dc_r[0])



#Volts
series_volts1 = Label(series, text="Volts:", bg=dark)
series_volts1.place(x=260, y= 350)

series_v1 = Text(series, width=10, height=1)
series_v1.place(x=300, y=350)

e_ser1 = StringVar()
e_ser1.set(dc_e[0])
ed_ser1 = ttk.OptionMenu(series, e_ser1, *dc_e)
ed_ser1.place(x=390, y=350)

#Volts2
series_volts2 = Label(series, text="Volts:", bg=dark)
series_volts2.place(x=825, y= 170)

series_v2 = Text(series, width=10, height=1)
series_v2.place(x=870, y=170)

e_ser2 = StringVar()
e_ser2.set(dc_e[0])
ed_ser2 = ttk.OptionMenu(series, e_ser2, *dc_e)
ed_ser2.place(x=960, y=170)

#Volts3
series_volts3 = Label(series, text="Volts:", bg=dark)
series_volts3.place(x=260, y= 170)

series_v3 = Text(series, width=10, height=1)
series_v3.place(x=300, y=170)

e_ser3 = StringVar()
e_ser3.set(dc_e[0])
ed_ser3 = ttk.OptionMenu(series, e_ser3, *dc_e)
ed_ser3.place(x=390, y=170)

#Amps
series_amps = Label(series, text="Amps:", bg=dark)
series_amps.place(x=540, y=520)

series_a = Text(series, width=10, height=1)
series_a.place(x=580, y=520)

i_ser = StringVar()
i_ser.set(dc_i[0])
id_ser = ttk.OptionMenu(series, i_ser, *dc_i)
id_ser.place(x=670, y=520)

#ohms 1
series_ohms1 = Label(series, text="Ohms:", bg=dark)
series_ohms1.place(x=825, y=350)

series_o1 = Text(series, width=10, height=1)
series_o1.place(x=870, y=350)

r_ser1 = StringVar()
r_ser1.set(dc_r[0])
rd_ser1 = ttk.OptionMenu(series, r_ser1, *dc_r)
rd_ser1.place(x=960, y=350)

#ohms 2
series_ohms2 = Label(series, text="Ohms:", bg=dark)
series_ohms2.place(x=540, y=170)

series_o2 = Text(series, width=10, height=1)
series_o2.place(x=580, y=170)

r_ser2 = StringVar()
r_ser2.set(dc_r[0])
rd_ser2 = ttk.OptionMenu(series, r_ser2, *dc_r)
rd_ser2.place(x=670, y=170)



def calc_series():
    #volts1
    e_i1 = series_v1.get(1.0, END + "-1c")
    #volts2
    e_i2 = series_v2.get(1.0, END + "-1c")
    #volts3
    e_i3 = series_v3.get(1.0, END + "-1c")
    #amps
    i_i = series_a.get(1.0, END + "-1c")
    #ohms1
    r_i1 = series_o1.get(1.0, END + "-1c")
    #ohms2
    r_i2 = series_o2.get(1.0, END + "-1c")

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


    if e_i1:
        e_i1 = float(e_i1)
        drop = e_ser1.get()
        size()
        e_i1 = e_i1 * s

    if e_i2:
        e_i2 = float(e_i2)
        drop = e_ser2.get()
        size()
        e_i2 = e_i2 * s

    if e_i3:
        e_i3 = float(e_i3)
        drop = e_ser3.get()
        size()
        e_i3 = e_i3 * s

    if i_i:
        i_i = float(i_i)
        drop = i_ser.get()
        size()
        i_i = i_i * s

    if r_i1:
        r_i1 = float(r_i1)
        drop = r_ser1.get()
        size()
        r_i1 = r_i1 * s

    if r_i2:
        r_i2 = float(r_i2)
        drop = r_ser2.get()
        size()
        r_i2 = r_i2 * s


    if i_i == "":
        if e_i1 and r_i1 and r_i2:
            rser = (r_i1 + r_i2)
            i_i = (e_i1 / rser)
            print(i_i)
            series_a.insert(INSERT, i_i)
            if e_i2 == "" and e_i3 == "":
                e_i2 = (i_i * r_i1)
                series_v2.insert(INSERT, e_i2)
                e_i3 = (i_i * r_i2)
                series_v3.insert(INSERT, e_i3)
        elif r_i1 and e_i2:
            i_i = (e_i2 / r_i1)
            series_a.insert(INSERT, i_i)
        elif r_i2 and e_i3:
            i_i = (e_i3 / r_i2)
            series_a.insert(INSERT, i_i)
            # if r_i1 == "" and e_i2 == "":
                


    if e_i1 == "":
        if i_i and r_i1 and r_i2:
            e_i1 = (i_i * (r_i1 + r_i2))
            series_v1.insert(INSERT, e_i1)
            if e_i2 == "" and e_i3 == "":
                e_i2 = (i_i * r_i1)
                series_v2.insert(INSERT, e_i2)
                e_i3 = (i_i * r_i2)
                series_v3.insert(INSERT, e_i3)
    if r_i1 == "" and r_i2 == "":
        if i_i and e_i2 and e_i3:
            r_i1 = (e_i2 / i_i)
            series_o1.insert(INSERT, r_i1)
            r_i2 = (e_i3 / i_i)
            series_o2.insert(INSERT, r_i2)
            if e_i1 == "":
                if i_i and r_i1 and r_i2:
                    e_i1 = (i_i * (r_i1 + r_i2))
                    series_v1.insert(INSERT, e_i1)

del_dc_series = ttk.Button(series, text="Clear", command = clear_series)
del_dc_series.place(x=660, y=350)

calc_dc_series= Button(series, text="Calculate", command= calc_series)
calc_dc_series.place(x=600, y=350)









#par_dc
img_par1 = Image.open("parellell.png")
img_par2 = ImageTk.PhotoImage(img_par1)
par_chart = Label(par, image = img_par2)
par_chart.pack()


def clear_par():
    par_v.delete("1.0","end")
    par_a1.delete("1.0","end")
    par_a2.delete("1.0","end")
    par_o1.delete("1.0","end")
    par_o2.delete("1.0","end")
    e_par.set(dc_e[0])
    i_par1.set(dc_i[0])
    i_par2.set(dc_i[0])
    r_par1.set(dc_r[0])
    r_par2.set(dc_r[0])



#Volts
par_volts = Label(par, text="Volts:", bg=dark)
par_volts.place(x=325, y= 350)

par_v = Text(par, width=10, height=1)
par_v.place(x=365, y=350)

e_par = StringVar()
e_par.set(dc_e[0])
ed_par = ttk.OptionMenu(par, e_par, *dc_e)
ed_par.place(x=455, y=350)

#Amps1
par_amps1 = Label(par, text="Amps:", bg=dark)
par_amps1.place(x=600, y=560)

par_a1 = Text(par, width=10, height=1)
par_a1.place(x=640, y=560)

i_par1 = StringVar()
i_par1.set(dc_i[0])
id_par1 = ttk.OptionMenu(par, i_par1, *dc_i)
id_par1.place(x=730, y=560)

#Amps2
par_amps2 = Label(par, text="Amps:", bg=dark)
par_amps2.place(x=890, y=560)

par_a2 = Text(par, width=10, height=1)
par_a2.place(x=930, y=560)

i_par2 = StringVar()
i_par2.set(dc_i[0])
id_par2 = ttk.OptionMenu(par, i_par2, *dc_i)
id_par2.place(x=1020, y=560)

#ohms 1
par_ohms1 = Label(par, text="Ohms:", bg=dark)
par_ohms1.place(x=600, y=350)

par_o1 = Text(par, width=10, height=1)
par_o1.place(x=640, y=350)

r_par1 = StringVar()
r_par1.set(dc_r[0])
rd_par1 = ttk.OptionMenu(par, r_par1, *dc_r)
rd_par1.place(x=730, y=350)

#ohms 2
par_ohms2 = Label(par, text="Ohms:", bg=dark)
par_ohms2.place(x=880, y=350)

par_o2 = Text(par, width=10, height=1)
par_o2.place(x=920, y=350)

r_par2 = StringVar()
r_par2.set(dc_r[0])
rd_par2 = ttk.OptionMenu(par, r_par2, *dc_r)
rd_par2.place(x=1010, y=350)



def calc_par():
    #volts
    e_i = par_v.get(1.0, END + "-1c")
    #amps1
    i_i1 = par_a1.get(1.0, END + "-1c")
    #amps2
    i_i2 = par_a2.get(1.0, END + "-1c")
    #ohms1
    r_i1 = par_o1.get(1.0, END + "-1c")
    #ohms2
    r_i2 = par_o2.get(1.0, END + "-1c")

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


    if e_i:
        e_i = float(e_i)
        drop = e_par.get()
        size()
        e_i = e_i * s

    if i_i1:
        i_i1 = float(i_i1)
        drop = i_par1.get()
        size()
        i_i1 = i_i1 * s

    if i_i2:
        i_i2 = float(i_i2)
        drop = i_par2.get()
        size()
        i_i2 = i_i2 * s

    if r_i1:
        r_i1 = float(r_i1)
        drop = r_par1.get()
        size()
        r_i1 = r_i1 * s

    if r_i2:
        r_i2 = float(r_i2)
        drop = r_par2.get()
        size()
        r_i2 = r_i2 * s

    if e_i == "":
        if i_i1 and r_i1:
            e_i = (i_i1 * r_i1)
            par_v.insert(INSERT, e_i)
        elif i_i2 and r_i2:
            e_i = (i_i2 * r_i2)
            par_v.insert(INSERT, e_i)
    if i_i1 == "":
        if e_i and r_i1:
            i_i1 = (e_i / r_i1)
            par_a1.insert(INSERT, i_i1)
    if i_i2 == "":
        if e_i and r_i2:
            i_i2 = (e_i / r_i2)
            par_a2.insert(INSERT, i_i2)
    if r_i1 == "":
        if e_i and i_i1:
            r_i1 = (e_i / i_i1)
            par_o1.insert(INSERT, r_i1)
    if r_i2 == "":
        if e_i and i_i2:
            r_i2 = (e_i / i_i2)
            par_o2.insert(INSERT, r_i2)

    
        


                



del_dc_par = ttk.Button(par, text="Clear", command = clear_par)
del_dc_par.place(x=340, y=600)

calc_dc_par= Button(par, text="Calculate", command= calc_par)
calc_dc_par.place(x=280, y=600)





# 1272
# 668

Inter.add(single, text="Single")
Inter.add(series, text="Series")
Inter.add(par, text="Parellel")





notebook.add(dc, text="DC Calculator")
notebook.add(dci, text="DC Interactive")
root.mainloop()