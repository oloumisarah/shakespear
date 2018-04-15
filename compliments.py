from guizero import App, Text, PushButton, Picture
#import random to randomly select the words
import random
#define function for complimentMe
def complimentMe():
    first = random.choice(adjectiveOne)
    second = random.choice(adjectiveTwo)
    third = random.choice(noun)
    compliment = "Thou " + first + " " + second + " "+ third +"!"
    return compliment
# this code will read cvs file line by line and then split each
# column into a seperate list

def newCompliment():
    newCompliment= complimentMe()
    message.value = newCompliment

adjectiveOne=[]
adjectiveTwo=[]
noun=[]
#open compliments.csv in read mode
with open("compliments.csv","r") as file:
    for singleLine in file:
        word = singleLine.split(",")
        adjectiveOne.append(word[0])
        adjectiveTwo.append(word[1])
        noun.append(word[2].strip())

#create gui
app = App(bg="#C0C5FF")
app.title="Compliment with Shakespear"
picture = Picture(app,image="theman.png")
picture.height = 400
picture.weidth = 350
picture.bg ="#C0C5FF"
message = Text (app,complimentMe()) # creates a Text object, adds it to the app and then calls the function to get an insult
message.font="arial bold"
message.bg="#C0C5FF"#create PushButton object
#calls new Insult function
button = PushButton(app, newCompliment, text="Compliment me again!")
app.display()
