import threading
import time

# 1. Execute this code twice. Describe the execution of this code as written.

# 2. Modify the code by either removing the argument to lock.acquire or setting the argument to True
# and describe the execution of this code. be sure to indicate what the impact of the argument False is

x = 0
def task(threadID, lock):
    global x

    if lock.acquire(False):
        print("thread " + str(threadID) + " is about to acquire the lock.")
        print("thread " + str(threadID) + " is executing the critical section")
        time.sleep(5)
        x+=1
        lock.release()
    else:
        print("thread " + str(threadID) + " is doing something else") 

def main():
    global x
    thread_nums = 20
    lock = threading.Lock()
    threads = []
    for i in range(thread_nums):
        thread = threading.Thread(target = task, args = [i, lock])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    
    print(f"final x = {x}")
main()
