from click import command
import gtts
from playsound import playsound

language = 'en'


def main():

    t1 = gtts.gTTS("hey this is mini")
    t1.save("mini.mp3")
    playsound("mini.mp3")


if __name__ == "__main__":
    main()
