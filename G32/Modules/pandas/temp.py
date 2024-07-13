def decorator(func):
    
    def x(_):
        print("Starting")
        func(_)
        print("End")
    
    return x

def doublecall(func):
    
    def x(_):
        func(_)
        func(_)
    
    return x

@doublecall
def wish(x):
    print(x)

wish("Hi")   
    