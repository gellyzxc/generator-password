import random



class Password:

    version = "0.0.5"

    ARRAY_SYMBOLS = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'q', 'w', 'e', 'r', 't', 'y','u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
    'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'o', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'm',
    '/', '@', '$', '%', '&'
    ]

    COUNT_SYMBOLS = 8




    def __init__(self):
        self.password = None
        self.count_symbols = self.COUNT_SYMBOLS

    def generate(self, count_symbols):
        if count_symbols:
            self.count_symbols = self.count_symbols
        else:
            self.count_symbols = self.COUNT_SYMBOLS

        self.count_variants = len(self.ARRAY_SYMBOLS) ** self.count_symbols
                
        password = ''

        for i in range(0, count_symbols):
            password = password + f'{self.random_symbols()}'
        
        self.password = password
    
    def random_symbols(self):
        return self.ARRAY_SYMBOLS[
            random.randint(0, len(self.ARRAY_SYMBOLS) - 1)
    ]

    def get_array_symbols(self):
        return self.ARRAY_SYMBOLS
