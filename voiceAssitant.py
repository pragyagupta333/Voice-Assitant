import  pyttsx3 # Converts Text into speech
import webbrowser # Display Web-based documents
import speech_recognition as sr
import datetime # To fetch info for date and time
import pyjokes  # Outputs random jokes,facts,etc

def speechtotext():
    # recognizer - an object to call class named Recognizer 
    recognizer=sr.Recognizer() 
    with sr.Microphone() as source:
        print("I am Listening....")
        #how to remove noise
        recognizer.adjust_for_ambient_noise(source)
        # audio- variable which will store what user speaks
        audio = recognizer.listen(source)

        try:
            print("I am Recognizing.....") # Case when data is being recorded 
            data = recognizer.recognize_google(audio)# data - a variable which recorded user voice
            print(data)
            return data
        except sr.UnknownValueError:  # when failed to recognizing
            print("Sorry,Not Understood")
def textToSpeech(x):
    # engine - object to call the class.  
     # init() - we will use functions from this class to convert text to speech
    engine = pyttsx3.init() 
    voices = engine.getProperty("voices") #voice's'bcoz we are keeping 2 voices -male,female
    engine.setProperty('voice',voices[1].id) # 'voice' bcoz at a particular time we need only one voice
   # voices[0].id fetches male voice, 
   # voices[1].id fetches female voice
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150) # speed of speech of assitant
    engine.say(x) #x- textual data in passed in parameter of this func.
    engine.runAndWait()

if __name__ == '__main__':

    #if speechtotext().lower == "hi,priya" :
    while True:
            data1=speechtotext().lower()
            if "your name" in data1: # ask "what is ur name"
                name="my name is priya"
                textToSpeech(name)
            elif "how are you" in data1:
                ans="i am fine"
                textToSpeech(ans)
            elif "time right now" in data1: # ask "what is the time right now"
                # time=datetime.datetime.now() # this returns date,hr,min,s,ms(but currently we only need time in hr,min)
                time=datetime.datetime.now().strftime("%I%M%p") #strftime used to search time and date in this func. I tells ->hrs, M->min, p->am/pm
                textToSpeech(time)
            elif "today's date" in data1: # ask "what is todays's date"
                # time=datetime.datetime.now() # this returns date,hr,min,s,ms(but currently we only need time in hr,min)
                day=datetime.datetime.now().strftime("%d%B%Y") #strftime used to search time and date in this func.d-dayB-month,Y-year
                textToSpeech(day)
            elif 'wikipedia' in data1: #ask open wikipedia
                webbrowser.open("https://www.wikipedia.org/")
            elif "joke" in data1: # tell me a joke. # this lib randomly tells u a joke
                joke1=pyjokes.get_joke(language = 'en', category = 'neutral')
                print(joke1)
                textToSpeech(joke1)
            elif "okay bye" in data1:
                textToSpeech("thank you")
                break
        #else:
        
            #print("thanks")

# Calling Functions 
#speechtotext()
#textToSpeech("Hello,Welcome!")

