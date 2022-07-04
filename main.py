from calendar import day_abbr
from re import A
from tkinter import *
from imageio import save
from PIL import Image
from matplotlib.pyplot import text
import time

from numpy import double, r_
import Calculation as c

savedata = {}
cal_count = 1

app = Tk()

app.title("Offset Slider crank")
app.geometry("720x576")

app['background'] = '#256dd6'

# region widgets

l = Label(app, text = "OFFSET SLIDER CRANK")
l.config(font =("Courier", 20))

l.place(x=250, y=10)

r_label = Label(app,text = "Crank Len (r)",bg="white", width=13)
r_field = Entry(app)
r=r_field.get()

l_label = Label(app,text = "Conn-Rod Len (l)",bg="white",width=13)
l_field = Entry(app) 

e_length = Label(app,text="Offset (e)",bg="white", width=13)
e_field=Entry(app)

w_label = Label(app,text = "Ang Velo (ω)",bg="white" ,width=13)
w_field = Entry(app) 

t_label = Label(app,text = "Time period (t)",bg="white", width=13)
t_field = Entry(app)

a_label=Label(app,text="Angular Accn (α) ",bg="white", width=13)
a_field=Entry(app)
#grid

x_l=Label(app, text="X = ", bg="white")
v_l=Label(app, text="V = ", bg="white")
a_l=Label(app, text="A = ", bg="white")

x_f = Entry(app)
v_f = Entry(app)
a_f = Entry(app)

fn_l=Label(app, text="filename", bg="white")
fn_f = Entry(app)
fn_f.place(x=500,y=250)
fn_l.place(x=420,y=250)

x_l.place(x=460,y=100)
v_l.place(x=460,y=150)
a_l.place(x=460,y=200)

r_label.place(x=100,y=300)
r_field.place(x=200,y=300)

l_label.place(x=100,y=350)
l_field.place(x=200,y=350) 

e_length.place(x=100,y=400)
e_field.place(x=200,y=400)

w_label.place(x=400,y=300)
w_field.place(x=500,y=300) 

t_label.place(x=400,y=350)
t_field.place(x=500,y=350)

a_label.place(x=400,y=400)
a_field.place(x=500,y=400)

x_f.place(x=500,y=100)
v_f.place(x=500,y=150)
a_f.place(x=500,y=200)

# endregion 

def Calculate() :

    global r_field, l_field, t_field, w_field, a_field, e_field, x_f , v_f , a_f, count, savedata

    x_f.delete(0,END)
    v_f.delete(0,END)
    a_f.delete(0,END)

    crl = double(r_field.get())
    col = double(l_field.get())
    tme = int(t_field.get())
    avo = double(w_field.get())
    aac = double(a_field.get())
    ecc = double(e_field.get())
    
    result = c.Calculate(aac, tme, col, crl, avo, ecc)
    pos = result[0]
    vel = result[1]
    acc = result[2]
    
    x_range=[]
    v_range=[]
    a_range=[]
    i=1
    result1=c.Calculate(aac, i, col, crl, avo, ecc)
    for i in range (1,tme+1):
        x_range.append((result1[0]))
        v_range.append((result1[1]))
        a_range.append((result1[2]))

    savedata[count] = {
        "Crank" :  crl,
        "Connec" : col ,
        "Time" : tme ,
        "AngVelo" : avo ,
        "AngAcc" : aac ,
        "Eccity" : ecc ,
        "pos" : x_range ,
        "velo" : v_range ,
        "acc" : a_range
    }

    count += 1

    x_f.insert(0, str(pos))
    v_f.insert(0, str(vel))
    a_f.insert(0, str(acc))

    print( savedata )

def Reset() :

    global r_field, l_field, t_field, w_field, a_field, e_field

    r_field.delete(0,END)
    l_field.delete(0,END)
    t_field.delete(0,END)
    w_field.delete(0,END)
    a_field.delete(0,END)
    e_field.delete(0,END)

def Exit() :
    exit()

def Save() :

    global savedata, fn_f

    data = ""

    filename = fn_f.get()

    if( filename.strip() == "" ) : return

    outer_keys = savedata

    if len(outer_keys) == 0 : return 

    for key1 in outer_keys :

        data += f"{str(key1)} |"

        for key2 in savedata[key1].keys() :

            data += f"{str(key2)} = { str( savedata[key1][key2] ) } |"
        
        data += "\n"
    
    print(data)

    filename = filename + ".txt"

    with open( filename, 'w' ) as textfile :

        textfile.write( data )


calc_but=Button(app,text="Calculate", width=25,height=7, command=Calculate) 
calc_but.place(x=5,y=450)

reset_but=Button(app,text="Reset", width=25,height=7,command=Reset) 
reset_but.place(x=165,y=450)

save_but=Button(app,text="Save", width=25,height=7, command=Save) 
save_but.place(x=345,y=450)

exit_but=Button(app,text="Exit", width=25,height=7,command=Exit)
exit_but.place(x=525,y=450)

canvas = Canvas(width=300 , height= 168.75, bg="black")
canvas.place(x=90,y=70)

root = app
file="ezgif-2-6eae9f531a.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):

    time.sleep(0.001)
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))

def stop_animation():
    root.after_cancel(anim)

gif_label = Label(root,image="")
gif_label.place(x=90,y=70)

start = Button(root,text="start",command=lambda :animation(count))
start.place(x=400,y=100)

stop = Button(root,text="stop",command=stop_animation)
stop.place(x=400,y=150)

app.mainloop()
