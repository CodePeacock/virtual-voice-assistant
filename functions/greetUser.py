import datetime
import shutil
from functions.voiceAssistant import speak
from functions.voiceAssistant import takeCommand, sr

VANAME = "Alice"
source = sr.Microphone


def wishMe():
    """
    It takes the current hour and if it's between 0 and 1p, it says "Good Morning", if it's between 12
    and 18, it says "Gqqqqood Afternoon", and if it's between 18 and 24, it says "Good Evening".
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Buddy !")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Buddy !")

    else:
        speak("Good Evening Buddy !")

    speak(f"I am {VANAME}")


def username():
    """
    It asks the user for a name, then greets the user with that name.
    """
    speak("What should i call you Buddy")
    uname = takeCommand()
    speak("Welcome Buddy")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome", uname.center(columns))
    print("#####################".center(columns))

    speak("How can i Help you?, Buddy")
