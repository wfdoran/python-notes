import multiprocessing as mp

def sqr(x):
    return x * x

num_procs = 4
with mp.Pool(num_procs) as p:
    print(sum(p.map(sqr, range(101))))

