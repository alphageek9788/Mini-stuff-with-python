import pyttsx3

engine = pyttsx3.init()

dic = {"hello": "hola", "good": "bien"}
x = input('Type kar:').lower()

if x in dic.keys():
    engine.say(dic[x])
    engine.runAndWait()
else:
    engine.say("Match not found")
    engine.runAndWait()
