import threading
import time

def worker():
    print("I am a thread")
    t = threading.current_thread()
    time.sleep(100)
    print(t.getName())


print("I am aumujun")

t = threading.current_thread()
print(t.getName())

new_t = threading.Thread(target=worker, name='I am subthread.')
new_t.start()
