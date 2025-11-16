import speech_recognition as sr
import pyttsx3
import time
import webbrowser


def speak(text):
   engine = pyttsx3.init()
   engine.say(text)
   engine.runAndWait()
   engine.stop()


def process_command(command):

   command = command.lower()

   if "play" in command and "open youtube" in command:
      song = command.split("play", 1)[1].strip()
      print('Song is: ', song)
      speak(f"Playing {song} on YouTube")
      time.sleep(1)
      webbrowser.open(f"https://www.youtube.com/results?search_query={song}")

   elif "open youtube" in command:
      speak("opening youtube...")
      time.sleep(1)
      webbrowser.open("https://www.youtube.com/")

   elif "open google" in command:
      speak("opening google...")
      time.sleep(1)
      webbrowser.open("https://www.google.com/")

   elif "open facebook" in command:
      speak("opening facebook...")
      time.sleep(1)
      webbrowser.open("https://www.facebook.com/")

   elif "open instagram" in command:
      speak("opening instagram...")
      time.sleep(1)
      webbrowser.open('https://www.instagram.com/')

   elif "open chat gpt" in command:
      speak("opening chatgpt...")
      time.sleep(1)
      webbrowser.open('https://www.chatgpt.com/')

   elif "open linkdedin" in command:
      speak("opening linkedin...")
      time.sleep(1)
      webbrowser.open('https://www.linkedin.com/')

   else:
      pass



if __name__ ==  "__main__":

   speak("Initializing Jarvis...")

   r = sr.Recognizer()

   DEVICE_INDEX = 0
   while True:

      try:

         with sr.Microphone(device_index=DEVICE_INDEX) as source:
            print("Listening...")

            # Noise adjustment
            r.adjust_for_ambient_noise(source, duration=1)

            # avoid immediate failure
            audio = r.listen(source, timeout=8, phrase_time_limit=8)


         try:
            word = r.recognize_google(audio)
            print("You said:", word)
         except:
            print("Unable to understand audio.")
            continue

         if(word.lower() == 'stop'):
            break

         if(word.lower() == 'hey jarvis'):

            speak("Yes sir, how can i help you?")

            with sr.Microphone(device_index=DEVICE_INDEX) as source:
               print("Jarvis ativated...")
 
               r.adjust_for_ambient_noise(source, duration=1)

               try:
                  audio = r.listen(source, timeout=8, phrase_time_limit=8)
                  command = r.recognize_google(audio)
                  print('Command is: ', command)
                  process_command(command)
               except:
                  speak("unable to understand command, can you repeat")
                  continue




      except sr.WaitTimeoutError:
         print("No speech detected. Try again.")
         continue

      except OSError as e:
         print("Microphone error:", e)
         break

      except:
         print("Unable to understand audio.")
         continue

