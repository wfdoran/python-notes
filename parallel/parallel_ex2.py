from multiprocessing import Process, Pipe

def sqr(conn):
    for i in range(10):
        conn.send(i*i)
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=sqr, args=(child_conn,))
    p.start()
    while True:
        if parent_conn.poll(1):
            x = parent_conn.recv()
            print(x)
        else:
            break
    p.join()