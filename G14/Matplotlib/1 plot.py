from matplotlib import pyplot as plt

x_axis = [1,2,3,4,5,6,7,8,9,10]
y_axis = [4,5,4,5,6,1,6,4,5,5]


plt.title("Figure 3")
# first we need to give the x and then y values
# plt.plot(x_axis,y_axis)
 
# this time let’s interchange the values
# and give a new param color
# plt.plot(y_axis,x_axis, color="red")
 
# finally you need to show the plot
# and yes we can show more than one plot at a time
# plt.show()


# first we need to give the x and then y values
plt.plot(x_axis,y_axis, linestyle="dotted",linewidth=6)
# we can also change linestypes from [dotted, dashed, -, -.,--.]
# and the line width

# we can also control the shape and size of the intersections
# plt.plot(y_axis,x_axis,marker="*", markersize=15)
# markers can be from 'o','*','-' and a few more
plt.show()

