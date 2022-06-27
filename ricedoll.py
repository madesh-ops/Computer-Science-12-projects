import random
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

while True:
  speak("Select which you want")
  print("1.Roll the Dice    2.To Exit")
  user = int(input("What you want to do\n"))
  if user==1:
    speak("selected roll the dice")
    number = random.randint(1,6)
    print("The Dice Rolling Number is : ",number)
  else:
    speak("selected to exit")
    break