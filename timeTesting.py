import time
from time import process_time

# start_time = time.time()
# print(start_time)
# time.sleep(1)
# print(time.localtime(start_time))

start_time = process_time()
print(start_time)
while True:
    # print(process_time())
    if process_time() >= start_time+1:
        print("DONE")