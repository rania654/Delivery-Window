from tkinter import *
root = Tk()

root.geometry("500x500")
root.configure(bg='red')
root.title("Delivery Window")

label=Label(root,text = "Email", background = "grey")
label.pack(pady= 10, padx= 3)

label2=Label(root,text = "Password", background = "grey")
label2.pack(pady = 20, padx= 3 )

entry = Entry(root, width=50)
entry.pack()

entry2 = Entry(root, width=50)
entry2.pack()

label3=Label(root,text = "What food would you like: Chicken sandwich, B.L.T, Veg sandwich or None?", background = "grey")
label3.pack()

entry3 = Entry(root, width=50)
entry3.pack()

spinbox = Spinbox(root,values = ("Chicken sandwich","B.L.T","Veg Sandwich","None"))
spinbox.pack()

label4=Label(root,text = "What drink would you like: cola, fanta, orange juice, water or None?", background = "grey")
label4.pack()

entry4 = Entry(root, width=50)
entry4.pack()

spinbox2 = Spinbox(root,values = ("Cola","Fanta","Orange juice","Water","None"))
spinbox2.pack( )

label5=Label(root,text = "What dessert would you like: ice cream, ice lolly, chocolate cake or None?", background = "grey")
label5.pack()

entry5 = Entry(root, width=50)
entry5.pack()

spinbox3 = Spinbox(root,values = ("Ice Cream","Ice Lolly","Chocolate Cake","None"))
spinbox3.place()

btn = Button(root, text = "Submit Order",background = "grey",command = root.destroy, bd = 5)
btn.pack()

entry6 = Entry(root, width=50)
entry6.pack()








root.mainloop()