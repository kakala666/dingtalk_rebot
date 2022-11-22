import multiprocessing
import time
import text
def homework(间隔,wehook,secret,talk_body):
    while True:
        #text.talktext(wehook,secret,"要发的内容")
        print(talk_body)
        time.sleep(间隔)
