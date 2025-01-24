import time

a=int(input("timer starts after?(in secs):"))
print("timer starts now")

for i in reversed(range(0,a)):
    sec=i%60
    minutes = (i // 60) % 60
    hours = i // 3600
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{sec:02}")
print("-------------")
time.sleep(1)
print("times ups")