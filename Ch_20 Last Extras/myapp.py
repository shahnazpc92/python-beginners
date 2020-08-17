import sys
sys.path.append(r'C:\pyscripts\lib')

import mymod
def myadd():
    print("myadd")
if __name__ == '__main__':
    print("From app",mymod.myadd(10,5))
    print("From app",mymod.mysub(10,5))
    myadd()