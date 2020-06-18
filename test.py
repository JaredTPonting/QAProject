# -*- coding: utf-8 -*-



import tkinter as tk


HEIGHT = 350
WIDTH = 400

def squareIt(a):	
	m = ""
	for i in range(100):
	    if i==0:
	    	continue
	    elif i**2 < int(a):
	        n=[0,0]
	        n[0] = i
	        n[1] = i**2
	        m = m + str(n[0]) + "  " + str(n[1]) + "\n"
	    else:
	        break
	return(m)
        
def formatIt(a):
    filler = squareIt(a)
    label['text'] = filler
        
def test_function(entrys):
    print("work? please..", entrys)
    

root = tk.Tk()

#bkImage = tk.PhotoImage(file = 'math.png')
background_label = tk.Label(root)
#background_label = tk.Label(root, image = bkImage)
background_label.place(relwidth=1,relheight=1)

canvas = tk.Canvas(root, height=HEIGHT,width = WIDTH)

background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root, bg = '#44c767',bd =3)
frame.place(relx = 0.1,relwidth=0.8,relheight=0.1, rely = 0.1)
frame2 = tk.Frame(root, bg = '#44c767',bd = 5)
frame2.place(relx = 0.1, rely = 0.3, relwidth=0.8,relheight = 0.6)
    


entry = tk.Entry(frame)
entry.place(relwidth = 0.65, relheight = 0.95)

B = tk.Button(frame, text ="Calculate!", command = lambda: formatIt(entry.get()))
B.place(relwidth = 0.33, relheight = 0.95, relx=0.67)
label = tk.Label(frame2,)
label.place(relwidth = 1, relheight = 1)


root.mainloop()