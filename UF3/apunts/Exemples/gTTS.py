"""
  JAB Javier Amaya Boira
  ITB Institut Tecnològic de Barcelona
  09/03/2023
  ASIXc M03 UF3 Fitxers
  Exemple: gTTS (Google Text-to-Speech)
           A Python library and CLI tool to interface with Google Translate's text-to-speech API.
           Write spoken mp3 data to a file, a file-like object (bytestring) for further audio
         manipulation, or stdout.
           http://gtts.readthedocs.org/
"""
"""
"# Import the required module for text
# to speech conversion
from gtts import gTTS


# The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert
language = 'en'

# Passing the text and language to the engine,
# here we have marked slow=False. Which tells
# the module that the converted audio should
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)

# Saving the converted audio in a mp3 file named
# welcome
myobj.save("welcome.mp3")

# Playing the converted file
os.system("mpg321 welcome.mp3")
os.system("start hello.mp3")
os.system("ffplay hello.mp3")   #ffplay
os.system("mpg123 hello.mp3")   #mpg123
os.system("mplayer hello.mp3")  #mplayer
"""
# pip install gtts
# pip install playsound

import os #is used to OS separator "/" or "\" calling fucntion "os.path.join"
from gtts import gTTS
from playsound import playsound
TEMP_PATH=os.path.join(".","temp")
text="Please be quiet. This is an example the how intelligent your teacher is"
tts=gTTS(text,lang="en")

tts.save(os.path.join(TEMP_PATH,"text2speech.mp3")) #tts.save("./temp/text2speech.mp3")

playsound(os.path.join(TEMP_PATH,"text2speech.mp3")) #playsound("./temp/text2speech.mp3")

