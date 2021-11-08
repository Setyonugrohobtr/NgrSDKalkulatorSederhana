import pyttsx3


class PutarSuara:
    def __init__(self, voice='male', speakstatus=True):
        self.voice = 'male'
        self.speakstatus = speakstatus
        self.speakWords = {
            '1': 'satu',
            '2': 'dua',
            '3': 'tiga',
            '4': 'empat',
            '5': 'lima',
            '6': 'enam',
            '7': 'tujuh',
            '8': 'delapan',
            '9': 'sembilan',
            '0': 'nol',
            '/': 'bagi',
            'x': 'kali',
            '+': 'tambah',
            '=': 'jumlah',
            '-':'minus'
        }
        self.engine = pyttsx3.init()
        v = self.engine.getProperty('voices')
        self.engine.setProperty('voice', v[0].id)

    def speak(self, content):
        if self.speakstatus == True:
            self.engine.say(self.speakWords[content])
            self.engine.runAndWait()


if __name__ == '__main__':
    ob = PutarSuara()
    ob.speak('=')
