class MorseCodeTranslator:
    def __init__(self):
        """
        Initializes the MorseCodeTranslator class with a dictionary mapping characters to Morse Code
        """
        self.morse_code_dict = {
            #Letters
            'a':'.-','b':'-...','c':'-.-.','d':'-..', 'e':'.','f':'..-.','g':'--.','h':'....',
            'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
            'q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
            'y':'-.--','z':'--..',
            #Numbers
            '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
            '8':'---..','9':'----.','0':'-----',
            #Special Characters
            ' ':'/','@':'.--.-.',',':'--..--','?':'..--..',"'":'.----.','!':'-.-.--','/':'-..-.',
            '(':'-.--.',')':'-.--.-','&':'.-...',':':'---...',';':'-.-.-.','=':'-...-','+':'.-.-.',
            '_':'..--.-','"':'.-..-.','$':'...-..-','*':'-..-','@':'.--.-.'
        }
        
    def encrypt(self,text):
            """
            Encrypt the given text into Morse code.

            Arguments:
                text(str): The text to be encrypted.

            Return:
                str: the encrypted text in Morse code.
            """

            try:
                # Convert text to lowercase
                text = text.lower()
                #Generate a list of Morse code representations for each character in the text
                morse_code = [self.morse_code_dict[char] if char in self.morse_code_dict else KeyError for char in text]
                # Join the Morse code representations with a space between each code
                return ' '.join(morse_code)
            except TypeError as e:
                 raise ValueError("Input given is insuppoted for encryption.")
            

            
