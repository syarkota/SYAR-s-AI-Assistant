from tkinter import*
from PIL import Image, ImageTk
import speech_text
import action

def ask():
    user_val = speech_text.speech_text()
    bot_val = action.Action(user_val)
    text.insert(END , 'User--->' + user_val+"\n")
    if bot_val != None:
        text.insert(END , "BOT<---" +str(bot_val)+"\n")
        if bot_val == "ok sir" :
            root.destroy()
def send():
    user = speech_text.speech_text()
    send = entry1.get()
    bot = action.Action(send)
    bot = action.Action(user)
    text.insert(END , 'User--->'+send+ str(user) +"\n")
    if bot != None:
        text.insert(END, "BOT <---" + str(bot)+"\n")
    if bot == "ok sir" :
        root.destroy()

def delete():
    text.delete("1.0", "end")
    

root = Tk()
root.geometry("550x675")
root.title("SYAR-Assistant")
root.resizable(False,False)
root.config(bg="black")

Main_frame = LabelFrame(root , padx=100 ,  pady=7 , borderwidth=3 ,  relief="raised")
Main_frame.config(bg="azure")
Main_frame.grid(row = 0 ,  column= 1 ,  padx= 55 ,  pady =  10)

Text_lable = Label(Main_frame, text = "Syar's AI- Assistant" , font=("comic Sans ms" ,  14 , "bold" ) , bg = "azure")
Text_lable.grid(row=0 ,  column=0 , padx=20 , pady= 10)

Display_Image = ImageTk.PhotoImage(Image.open("image/assitant.png"))
Image_Lable = Label(Main_frame, image= Display_Image)
Image_Lable.grid(row = 1 ,  column=0 , pady=20)

text=Text(root , font= ('Courier 10 bold') , bg = "white")
text.grid(row = 2,  column= 0)
text.place(x= 100, y= 370, width= 380, height= 120) 

entry1 = Entry(root, justify = CENTER)
entry1.place(x=100 , y = 500 , width= 400, height= 30)

button1 =  Button(root,  text="ASK" , bg="white" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=ask)
button1.place(x= 70, y= 575)

button2 =  Button(root,  text="Send" , bg="white" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,  command=send)
button2.place(x= 400, y= 575)

button3 = Button(root, text="Delete", bg="white" , pady=16 ,  padx=40,  borderwidth=3 , relief=SOLID ,command=delete)
button3.place(x= 225, y= 575)

root.mainloop()
