import speech_recognition
import pyttsx3
from datetime import date
from datetime import datetime


robot_ear = speech_recognition.Recognizer()
robot_mount = pyttsx3.init()
robot_brain = ""

with speech_recognition.Microphone() as mic:
	print ("Robot: I'm Listening")
	audio = robot_ear.listen(mic)
print ("Robot: ...")


try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""
print ("You: " + you)

if you == "":
	robot_brain = "I can't hear you, try again"
elif you == "hello":
	robot_brain = "Hello Nelson Tran"
elif you == "US president":
	robot_brain = "Donald Trump"
elif you == "today":
	today = date.today()
	robot_brain = today.strftime("%B %d, %Y")
elif you == "time":
	now = datetime.now()
	robot_brain = now.strftime("%H hours %M minutes %S seconds")
else:
	robot_brain = "I'm fine thank you and you"

print("Robot = " + robot_brain)

robot_mount.say(robot_brain)
robot_mount.runAndWait()
