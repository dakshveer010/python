import time
def countdown(seconds):
    while seconds >0:
        min=int(seconds/60)
        sec=int(seconds%60)
        timer= f'{mins}:{secs}'
        print(timer,end='\r')
        time.sleep(1)
        seconds-=1
    print("timer")
seconds=input("enter seconds")
countdown=int(seconds)



