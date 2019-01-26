#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from time import sleep
from RPi import GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

for i in range(5):
    GPIO.output(4, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(4, GPIO.LOW)
    sleep(0.5)

GPIO.cleanup()


# In[ ]:




