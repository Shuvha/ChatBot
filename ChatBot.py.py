import random
from tkinter import*

root = Tk()
root.title("ChatBot")
root.geometry("500x300+100+100")

botSaid =StringVar()


hellow = ["hi","is anyone there?", "hello", "good day!","hello there!"]
bye = ["cya", "see you later!","bye" ,"goodbye", "i am Leaving!", "have a Good day!"]
howare = ["how are you?","whats up","how you doing"]
name = ["whats your name?","what is your name?","do you have any name?","what should i call you?","name?"]
menu = ["i want to buy something!", "what is on the menu?", "what do you reccommend?", "could i get something to eat!"]
hours = ["when are you guys open?", "what are your hours?", "hours of operation?","time?","work time?","time period?",]
TimeMorning = ["Gd Mrng!"]
TimeNight = ["Good Night!"]
Weather = ["What is the weather?"]
Day = ["What is the Day?"]
Doing =["What are u doing?"]
Felling=["What are u Feel now?"]
like=["What are u like?","What do u like most?"]

print("*******************\n")

def chat():
	

	if userInput.get().lower() in hellow:
		botans = ["Hello !","hi","hi there","welcome"]
		botSaid.set(random.choice(botans))

	elif userInput.get().lower() in bye:
		botans = ["sad to see you go :(","bye","miss you"]
		botSaid.set(random.choice(botans))

	elif userInput.get().lower() in howare:
		botans = ["I am fine ,thanks ","Happy","I am good"]
		botSaid.set(random.choice(botans))

	elif userInput.get().lower() in name:
		botans = ["My name is TVC bot","You can call me TVC bot","TVC Bot in your service","My friends call me TVC Bot"]
		botSaid.set(random.choice(botans))

	elif userInput.get().lower() in bye:
		botans = ["Sad to see you go :(", "Talk to you later", "Goodbye!","Have a nice Day"]
		botSaid.set(random.choice(botans))

	elif userInput.get().lower() in menu:
		botans = ["We sell apples!", "Apples are on the menu!","Please take a look at Apples"]
		botSaid.set(random.choice(botans))

	elif userInput.get().lower() in hours:
		botans = ["We are open 7am-4pm Monday-Friday!"]
		botSaid.set(random.choice(botans))

	elif userInput.get() in TimeMorning:
		botans = ["Good Morning! Have a nice day!"]
		botSaid.set(random.choice(botans))

	elif userInput.get()  in TimeNight:
		botans = ["Good Night! Sweet Dreams"]
		botSaid.set(random.choice(botans))

	elif userInput.get()  in Weather :
		botans = ["Sunney!","Rainy","Fantastic","Not Good"]
		botSaid.set(random.choice(botans))

	elif userInput.get()  in Day:
		botans = ["Sunday","Monday","Wednesday","Friday","Suturday"]
		botSaid.set(random.choice(botans))

	elif userInput.get()  in Doing:
		botans = ["I am study now!","I am Sleepling!","I am Playing!!"]
		botSaid.set(random.choice(botans))

	elif userInput.get()  in Felling:
		botans = ["bad!","Good!!"]
		botSaid.set(random.choice(botans))

	elif userInput.get()  in like:
		botans = ["Outing","Smiling","Jocking"]
		botSaid.set(random.choice(botans))

	else:
		botSaid.set("Sorry what?")
		
head = Label(root,text="CHAT BOT",font=("times new roman",20))
head.place(x=200,y=10)

holder = Frame(root)
holder.place(x=80,y=100)

userText = Label(holder,text="Input-",font=("times new roman",15))
userText.grid(row=0,column=0)

userInput = Entry(holder,font=("times new roman",15))
userInput.grid(row=0,column=1)

submitBtn = Button(holder,text="submit",font=("times new roman",15),command=chat)
submitBtn.grid(row=0,column=2)

botText = Label(holder,text="Bot-",font=("times new roman",15))
botText.grid(row=1,column=0,pady=50)

botOutput = Entry(holder,textvariable=botSaid,font=("times new roman",15))
botOutput.grid(row=1,column=1)

root.mainloop()