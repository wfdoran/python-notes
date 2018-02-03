import multiprocessing as mp
import time

def hello(proc_id, channel):
    print("start: ", proc_id)
    channel.put(str(proc_id))
    time.sleep(1)
    print("end: ", proc_id)
    
if __name__ == '__main__':
    num_procs = 4
    channel = mp.Queue()
    procs = [mp.Process(target=hello, args=(proc_id, channel)) for proc_id in range(num_procs)]

    for p in procs:
        p.start()

    for p in procs:
        p.join()

    results = [channel.get() for p in procs]
    print(results)
