"""
Start at 10 seconds and count down until 1 and then print "Happy New Year! 🎉"
"""
import time

x = 10
while x > 0:
    print(x)
    x -= 1
    time.sleep(1)
print('Happy New Year! 🎉')
