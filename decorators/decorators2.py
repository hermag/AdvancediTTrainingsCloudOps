def f1(func):
    def wrapper(*args, **kwargs):
        print("Started")
        func(*args, **kwargs)
        print("Ended")
    return wrapper

@f1
def f(a,b,c=9):
    sum=a+b+c
    print(sum)

f(2,3,c=9)
#f1(f)()

# x = f1(f)
# x()
