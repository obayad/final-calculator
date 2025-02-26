import customtkinter as ctk

root = ctk.CTk()
root.geometry("400x600")
root.resizable(False, False)
root.title("Calculator")

btn_height=36
btn_color= "#f8f8f8"
btn_text_color = "Black"

equation_text ="0"
equation_label = ctk.StringVar(value=equation_text)

def btn_click(num):
    pass

def btn_backspace():
    pass

def btn_equal():
    pass

def btn_clear():
    pass

bfont = "Mukta Semibold"
main_label = ctk.CTkLabel(root, 
                          textvariable=equation_label, 
                          font=("Mukta Semibold", 40),
                          text_color="Black", 
                          height=200, width=400, 
                          anchor="e", padx=8, pady=20)
main_label.pack()

#tabmenu frame

tab = ctk.CTkTabview(root,fg_color="transparent", width=400, height=50)
tab.pack()

#create tabs
trigonometry_tab = tab.add("Trigonometry")
exponential_tab = tab.add("Exponential")

#trigonometry tab Frame
trigonometry_tab.columnconfigure(0,weight=1)
trigonometry_tab.columnconfigure(1,weight=1)
trigonometry_tab.columnconfigure(2,weight=1)

#exponential tab Frame
exponential_tab.columnconfigure(0,weight=1)
exponential_tab.columnconfigure(1,weight=1)
exponential_tab.columnconfigure(2,weight=1)


#trigonometry frame
btn_sin = ctk.CTkButton(trigonometry_tab, text="sin", font=(bfont, 16),fg_color="#f8f8f8",text_color="Black",height=btn_height)
btn_sin.grid(row=0,column=0, sticky="nsew", padx=2)
btn_sin = ctk.CTkButton(trigonometry_tab, text="cos", font=(bfont, 16),fg_color="#f8f8f8",text_color="Black",height=btn_height)
btn_sin.grid(row=0,column=1, sticky="nsew", padx=2)
btn_sin = ctk.CTkButton(trigonometry_tab, text="tan", font=(bfont, 16),fg_color="#f8f8f8",text_color="Black",height=btn_height)
btn_sin.grid(row=0,column=2, sticky="nsew", padx=2)

#exponential frame
btn_log = ctk.CTkButton(exponential_tab, text="log", font=(bfont, 16),fg_color="#f8f8f8",text_color="Black",height=btn_height)
btn_log.grid(row=0,column=0, sticky="nsew", padx=2)
btn_log = ctk.CTkButton(exponential_tab, text="ln", font=(bfont, 16),fg_color="#f8f8f8",text_color="Black",height=btn_height)
btn_log.grid(row=0,column=1, sticky="nsew", padx=2)
btn_log = ctk.CTkButton(exponential_tab, text="exp", font=(bfont, 16),fg_color="#f8f8f8",text_color="Black",height=btn_height)
btn_log.grid(row=0,column=2, sticky="nsew", padx=2)

#button Frame
btn_frame = ctk.CTkFrame(root, fg_color="transparent")

btn_frame.columnconfigure(0,weight=1)
btn_frame.columnconfigure(1,weight=1)
btn_frame.columnconfigure(2,weight=1)
btn_frame.columnconfigure(3,weight=1)
btn_frame.columnconfigure(4,weight=1)



#first row
btn1 = ctk.CTkButton(btn_frame, text="2ⁿ", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn1.grid(row=0,column=0, sticky="nsew", padx=2,pady=2)
btn2 = ctk.CTkButton(btn_frame, text="π", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn2.grid(row=0,column=1, sticky="nsew", padx=2,pady=2)
btn3 = ctk.CTkButton(btn_frame, text="e", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn3.grid(row=0,column=2, sticky="nsew", padx=2,pady=2)
btn4 = ctk.CTkButton(btn_frame, text="CE", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn4.grid(row=0,column=3, sticky="nsew", padx=2,pady=2)
btn5 = ctk.CTkButton(btn_frame, text="<-", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn5.grid(row=0,column=4, sticky="nsew", padx=2,pady=2)

#second row
btn6 = ctk.CTkButton(btn_frame, text="x2", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn6.grid(row=1,column=0, sticky="nsew", padx=2,pady=2)
btn7 = ctk.CTkButton(btn_frame, text="1/x", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn7.grid(row=1,column=1, sticky="nsew", padx=2,pady=2)
btn8 = ctk.CTkButton(btn_frame, text="|x|", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn8.grid(row=1,column=2, sticky="nsew", padx=2,pady=2)
btn9 = ctk.CTkButton(btn_frame, text="exp", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn9.grid(row=1,column=3, sticky="nsew", padx=2,pady=2)
btn10 = ctk.CTkButton(btn_frame, text="mod", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn10.grid(row=1,column=4, sticky="nsew", padx=2,pady=2)

#third row
btn11 = ctk.CTkButton(btn_frame, text="√", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn11.grid(row=2,column=0, sticky="nsew", padx=2,pady=2)
btn12 = ctk.CTkButton(btn_frame, text="(", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn12.grid(row=2,column=1, sticky="nsew", padx=2,pady=2)
btn13 = ctk.CTkButton(btn_frame, text=")", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn13.grid(row=2,column=2, sticky="nsew", padx=2,pady=2)
btn14 = ctk.CTkButton(btn_frame, text="n!", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn14.grid(row=2,column=3, sticky="nsew", padx=2,pady=2)
btn15 = ctk.CTkButton(btn_frame, text="/", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn15.grid(row=2,column=4, sticky="nsew", padx=2,pady=2)

#fourth row
btn16 = ctk.CTkButton(btn_frame, text="1", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn16.grid(row=3,column=0, sticky="nsew", padx=2,pady=2)
btn17 = ctk.CTkButton(btn_frame, text="7", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn17.grid(row=3,column=1, sticky="nsew", padx=2,pady=2)
btn18 = ctk.CTkButton(btn_frame, text="8", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn18.grid(row=3,column=2, sticky="nsew", padx=2,pady=2)
btn19 = ctk.CTkButton(btn_frame, text="9", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn19.grid(row=3,column=3, sticky="nsew", padx=2,pady=2)
btn20 = ctk.CTkButton(btn_frame, text="*", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn20.grid(row=3,column=4, sticky="nsew", padx=2,pady=2)

#fifth row
btn21 = ctk.CTkButton(btn_frame, text="1", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn21.grid(row=4,column=0, sticky="nsew", padx=2,pady=2)
btn22 = ctk.CTkButton(btn_frame, text="4", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn22.grid(row=4,column=1, sticky="nsew", padx=2,pady=2)
btn23 = ctk.CTkButton(btn_frame, text="5", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn23.grid(row=4,column=2, sticky="nsew", padx=2,pady=2)
btn24 = ctk.CTkButton(btn_frame, text="6", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn24.grid(row=4,column=3, sticky="nsew", padx=2,pady=2)
btn25 = ctk.CTkButton(btn_frame, text="-", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn25.grid(row=4,column=4, sticky="nsew", padx=2,pady=2)

#six row
btn26 = ctk.CTkButton(btn_frame, text="log", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn26.grid(row=5,column=0, sticky="nsew", padx=2,pady=2)
btn27 = ctk.CTkButton(btn_frame, text="1", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn27.grid(row=5,column=1, sticky="nsew", padx=2,pady=2)
btn28 = ctk.CTkButton(btn_frame, text="2", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn28.grid(row=5,column=2, sticky="nsew", padx=2,pady=2)
btn29 = ctk.CTkButton(btn_frame, text="3", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn29.grid(row=5,column=3, sticky="nsew", padx=2,pady=2)
btn30 = ctk.CTkButton(btn_frame, text="+", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn30.grid(row=5,column=4, sticky="nsew", padx=2,pady=2)

#seventh row
btn31 = ctk.CTkButton(btn_frame, text="ln", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn31.grid(row=6,column=0, sticky="nsew", padx=2,pady=2)
btn32 = ctk.CTkButton(btn_frame, text="+/-", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn32.grid(row=6,column=1, sticky="nsew", padx=2,pady=2)
btn33 = ctk.CTkButton(btn_frame, text="0", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn33.grid(row=6,column=2, sticky="nsew", padx=2,pady=2)
btn34 = ctk.CTkButton(btn_frame, text=".", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn34.grid(row=6,column=3, sticky="nsew", padx=2,pady=2)
btn35 = ctk.CTkButton(btn_frame, text="=", font=(bfont, 16),fg_color=btn_color,text_color=btn_text_color,height=btn_height)
btn35.grid(row=6,column=4, sticky="nsew", padx=2,pady=2)


btn_frame.pack(fill="both", expand=True, padx=2)


root.mainloop()