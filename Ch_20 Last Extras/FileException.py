import sys

for arg in sys.argv[1:]:  # pass the code in command line
    try:
        f = open(arg)
        
    except FileNotFoundError:
        print("no such file")
        
    else:
        print("Number of lines",len(f.readlines()))
        f.close()
        
#cd\
# cd pyscripts
# python FileException.py mod1.py my.py myapp.py

#OUTPUT:- Number of lines 10
#         no such file
#         Number of lines 11