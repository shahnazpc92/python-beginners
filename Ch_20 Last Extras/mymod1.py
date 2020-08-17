def myadd(x,y):
    return x + y
    
def mysub(x,y):
    return x - y

print(__name__)
if __name__ == '__main__':
    print("From module",myadd(10,5))
    print("From module",mysub(10,5))
    