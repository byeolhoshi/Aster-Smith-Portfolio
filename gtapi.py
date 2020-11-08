#from googletrans import Translator 
import googletrans

from googletrans import Translator 

class trans:
    
    def __init__(self, filepath): 
        self.translator = Translator()
        self.target_lang = ''
        self.data = open(filepath, "r")
    
    
    def translate(self, targlang): 
        self.target_lang = targlang.lower()
        #print(googletrans.LANGUAGES.items())
        for k, v in googletrans.LANGUAGES.items():
            if v == self.target_lang: 
                self.target_lang = k 
                #print(self.target_lang)
                break 
            
        ''' if targlang not in googletrans.LANGUAGES.items():
            raise KeyError("Language Not Available") '''
        
        
        with self.data as f: 
            self.d = open("translated.txt", "w+")
            for line in f:
                #print(self.translator.translate(line, dest=str(targlang)).text)
                #self.transtxt = ''.join(self.translator.translate(line, dest = str(targlang)).text)
                print(type(self.d.write(self.translator.translate(line, dest = str(targlang)).text)))
               
            f.close()

        self.d.close()
        
        
        
    