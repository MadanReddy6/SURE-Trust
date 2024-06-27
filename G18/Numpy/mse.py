# mean squared error
import numpy as np

x = np.random.randint(1,11, (15))
x_ = x.mean()
print(x, x_)

diff = x_-x
diff_sq = diff**2
total_err= diff_sq.sum()

mse = total_err/len(x)

print(mse)
