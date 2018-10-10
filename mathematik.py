class Mathe:
    msg = ""
    
    def __init__(self):
        self.msg = "Hallo :-)";
    
    def message(self):
        print self.msg
    
    def fibonacci(self, N = 5):
        self.message()
        
        a, b = 0, 1
        f = [a, b]
        while b < N:
            a, b = b, a + b
            f = f + [b]
        return f
        