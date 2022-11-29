import speech_recognition as sr


def main():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Please say something")
        audio = r.listen(source, phrase_time_limit=5)
        print("Recognizing Now .... ")
        # recognize speech using google

        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            # return text
            print("Audio Recorded Successfully \n ")

        except Exception as e:
            print("Error :  " + str(e))
            return 0

        # write audio
        with open("recorded.wav", "wb") as f:
            f.write(audio.get_wav_data())


if __name__ == "__main__":
    main()
