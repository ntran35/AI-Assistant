import pyttsx3

robot_brain = "Say somthing please I would like to hear."

robot_mount = pyttsx3.init()
robot_mount.say(robot_brain)
robot_mount.runAndWait()
