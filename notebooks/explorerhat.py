#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from time import sleep
import explorerhat

for i in range(5):
    explorerhat.motor.one.forwards(100)
    sleep(1)
    explorerhat.motor.one.stop()
    sleep(0.5)
    


# In[ ]:




