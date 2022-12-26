from tkinter import *
from PIL import ImageTk, Image
import openai

#Place your OpenAI api key here
openai.api_key = ""

root = Tk()
root.title('Intelligent AI')
root.geometry("540x600")
root.resizable(True,True)


#Frame
frame = Frame(
    root,
    width=700,
    height=700
    )
frame.pack(expand=True, fill=BOTH)

#Create a canvas
canvas= Canvas(root, width= 1500, height= 1000,  scrollregion=(0,0,700,700))
canvas.configure(bg='#1a1a1a')
canvas.pack()


#Open Image(You can change this)
img= (Image.open("C:\\Users\\HP\\Downloads\\ai_pic.png"))
 

#Resize the Image using resize method
resized_image= img.resize((80,90), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

#Position Image
absolute_pos = Label(root, image=new_image)
absolute_pos.image = new_image
absolute_pos.place(x=35,y=20)


# creating a label for name using widget Label
title_label = Label(root, text = 'Extremely Intelligent AI',  bg="#1a1a1a", fg="white",font=('courier new',19, 'bold'))
canvas.create_window(270, 50, window=title_label)
title_label.place(x=125,y=50)

# creating an entry for input
enter_url = Entry(root,font=("courier new",15,"bold"),bg="#191919")
canvas.create_window(280, 110, window=enter_url)
enter_url.insert(0,"   Enter Instruction here...")
enter_url.place(width=520,height=90,x=10, y= 120)



def execute():
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt=enter_url.get(),
  temperature=0.6,
  max_tokens=150,
  top_p=1,
  frequency_penalty=1,
  presence_penalty=1
     )
     #insert text to textbox
    T.insert(END, response.choices[0].text)
   


def clear():
    T.delete(1.0,END)
    enter_url.delete(0,END)



# Create text widget and specify size.
T = Text(root,font=("courier new",15), height = 5, width = 52,bg="#191919")
canvas.create_window(280,110,width=260,window=T)
T.place(width=520,height=260,x=10, y= 220)


#Execute Button
executebtn = Button(text='Execute',command=execute,fg="white",bg="#76B947",font=("courier new",15,"bold"))
canvas.create_window(280,110,width=260,window=executebtn)
executebtn.place(width=520,height=40,x=10, y= 500)

#Clear Button
clearbtn = Button(text='Clear',command=clear,fg="white",bg="#990033",font=("courier new",15,"bold"))
canvas.create_window(280,110,width=260,window=clearbtn)
clearbtn.place(width=520,height=40,x=10, y= 550)


if __name__ == "__main__":
    root.mainloop()
