class MorseCodeTranslator:
    def __init__(self):
        """
        Initializes the MorseCodeTranslator class with a dictionary mapping characters to Morse Code
        """
        self.morse_code_dict = {
            #Letters Mappings
            'a':'.-','b':'-...','c':'-.-.','d':'-..', 'e':'.','f':'..-.','g':'--.','h':'....',
            'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.',
            'q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-',
            'y':'-.--','z':'--..',
            #Numbers Mappings
            '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...',
            '8':'---..','9':'----.','0':'-----',
            #Special Characters Mappings
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
                 print("Input given is insuppoted for encryption.")
    
    def decrypt(self,morse_code):
        """
        Decrypts the given Morse code into text

        Args:
            morse_code(str): The Morse code to be decrypted
        
        Returns:
            str: the english text
        """
        try:
            # Split the Morse code into individual codes
            morse_code = morse_code.split(' ')
            text = ''
            # Iterate through each Morse code
            for code in morse_code:
                # Iterate through the Morse code dictionary to find the corresponding character 
                for key, value in self.morse_code_dict.items():
                    if code == value:
                        text += key
                    else:
                        raise TypeError
                return text 
        except TypeError as e:
            print("Input given is insupported for decryption as it is not found in dictionary.")


def main():
    """
    Main function to run the Morse code translator program.
    """

    translator = MorseCodeTranslator()
    while True:
        print("\nChoose an option:")
        print("1.Encrypt")
        print("2.Decrypt")
        print("3.Exit")

        choice = int(input("Enter your choice(1,2 or 3)"))

        try:
            if choice == 1:
                text = input("Enter the text to encrypt: ")
                encrypted_text = translator.encrypt(text)
                if encrypted_text == "":
                    print(f"Encrypted text: {encrypted_text}")
        except ValueError as e:
            print("Wrong Input!")
            print("Invalid choice. Please enter 1, 2 or 3.")




        
            

            
