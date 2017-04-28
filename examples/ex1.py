import matplotlib.pyplot as plt

x = [1,2,3,4,6]
y = [i*i - 5 * i for i in x]

plt.plot(x,y,"r*-")
plt.xlabel("foo")
plt.ylabel("bar")
plt.title("title")
plt.show()
