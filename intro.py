x = 2
def f():
    x = 4
    print (x) 			# LINE:1

print (x) 			# LINE:2

def g():
    f()
    x = 10
    print (x) 			# LINE:3

g()
f()
# LINE:4