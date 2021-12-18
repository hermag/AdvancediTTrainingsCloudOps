import time

def timer(func):
    def wrapper():
        before=time.time()
        func()
        print("Function took: ",time.time()-before," seconds")
    return wrapper

def run():
    time.sleep(3)

run() 