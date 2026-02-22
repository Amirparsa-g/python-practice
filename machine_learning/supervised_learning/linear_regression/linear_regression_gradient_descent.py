import numpy as np
import matplotlib.pyplot as plt

def compute_cost(x,y,w,b):
    m = x.shape[0]
    cost_sum=0
    for i in range (m):
        f_wb= w*x[i] + b
        cost = (f_wb - y[i])**2
        cost_sum+=cost
    
    total_cost=(1 / ( 2 * m )) * cost_sum
    return total_cost

def compute_gradient(x,y,w,b):
    m = x.shape[0]
    dj_dw = 0
    dj_db = 0

    for i in range (m):
        f_wb = w*x[i] + b
        dj_dw_i = x[i]*(f_wb - y[i])
        dj_db_i = f_wb-y[i]
        dj_dw += dj_dw_i
        dj_db += dj_db_i
    dj_dw /= m
    dj_db /= m

    return dj_dw , dj_db

def gradient_descent(x , y, w_in , b_in ,alpha, num_iters ):
    w = w_in
    b = b_in
    for i in range(num_iters):
        dj_dw , dj_db = compute_gradient(x,y,w,b)
        w-= alpha*dj_dw
        b-= alpha*dj_db
    return w , b

x_train = np.array([1,2,3,4,5])
y_train = np.array([300,400,500,600,700])
w_init = 0
b_init = 0
w , b = gradient_descent(x_train, y_train , w_init, b_init, 0.01, 10000)

print (f"w:{w}\nb:{b}")
print (compute_cost(x_train, y_train,w,b))

