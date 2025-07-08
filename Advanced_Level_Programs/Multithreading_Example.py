import threading

def print_even():
    for i in range(0, 10, 2):
        print("Even:", i)

def print_odd():
    for i in range(1, 10, 2):
        print("Odd:", i)

t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)

t1.start()
t2.start()

t1.join()
t2.join()
