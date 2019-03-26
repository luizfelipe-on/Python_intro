def do_twice (f,x): 
    f (x)
    f (x)

def print_twice (x): 
    print(x)
    print(x)

def do_four (o,y):
    do_twice(o,y)
    do_twice(o,y)

do_twice (print_twice,'spam')
do_four(print_twice,'spam')
