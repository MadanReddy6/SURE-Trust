from matplotlib import pyplot as plt

# scale so the shape doesn't expands, or contracts
plt.xlim(0.5,3.5)
plt.ylim(0,4)

# axis labels can also be given
plt.xlabel("Length")
plt.ylabel("Height") 

# plot title
plt.title("Alphabet M")

x = [1,1]
y = [1,3]
plt.plot(x,y,color = '#cce85a',lw=15)
plt.plot(x,y,'o')
x = [1,1.5,2]
y = [3,2,3]
plt.plot(x,y,color = '#000000',lw=10)
plt.plot(x,y,'*')
x = [2,2]
y = [3,1]
plt.plot(x,y,color = '#809fff',lw=15)
plt.plot(x,y,'+')

plt.show()


