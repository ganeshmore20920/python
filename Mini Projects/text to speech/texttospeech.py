from gtts import gTTS
import os

text = "hello world... i am your personal computer"
language = 'en'
obj = gTTS(text= text , lang = language, slow = False)
obj.save('sample.mp3')
os.system('sample.mp3')