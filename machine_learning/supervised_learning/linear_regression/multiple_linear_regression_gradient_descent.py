import copy, math
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=2)  


def compute_cost(x,y,w,b):
    m = x.shape[0]
    cost=0.0
    for i in range (m):
        f_wb=np.dot(x[i], w)+b
        cost += (f_wb-y[i])**2
    cost /= 2*m
    return cost

def compute_gradient(x,y,w,b):
    m , n = x.shape
    dj_dw= np.zeros(n,)
    dj_db = 0

    for i in range (m):
        err = (np.dot(x[i], w)+b) - y[i]
        dj_db += err
        for j in range (n):
            dj_dw[j] += err*x[i,j]
    dj_dw /=m
    dj_db /=m

    return dj_dw, dj_db

def gradient_descent(x , y, w_in , b_in ,alpha, num_iters ):
    w = copy.deepcopy(w_in)
    b = b_in
    for i in range(num_iters):
        dj_dw , dj_db = compute_gradient(x,y,w,b)
        w -= alpha*dj_dw
        b-= alpha*dj_db
    return w,b

X_train = np.array([[2104, 5, 1, 45], [1416, 3, 2, 40], [852, 2, 1, 35]])
y_train = np.array([460, 232, 178])
m , n = X_train.shape
mu = X_train.mean(axis=0)
sigma = X_train.std(axis=0)
Xn = (X_train - mu) / sigma

w_init = np.zeros(n,)
b_init = 0
w, b = gradient_descent(Xn, y_train, w_init, b_init, alpha=0.01, num_iters=10000)
print("w:", w, "b:", b)
print("cost:", compute_cost(Xn, y_train, w, b))

print(compute_cost(X_train, y_train, w,b))
