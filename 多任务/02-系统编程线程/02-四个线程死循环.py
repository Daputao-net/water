from threading import Thread 
def test():
    while True:
        print("---test---")

t1=Thread(target=test)
t2=Thread(target=test)
t3=Thread(target=test)
t4=Thread(target=test)

t1.start()
t2.start()
t3.start()
t4.start()


