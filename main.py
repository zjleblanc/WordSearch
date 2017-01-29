from test import Test
from AllTheThings import Scanner

class Start:
    
    def run(self, wordSearch, wordBank):
    	scanner = Scanner([1,1], wordSearch, wordBank)
    	scanner.scan_for_words()
        
        #be sure to call test.run in order to see if your code passes
        #Test().run()