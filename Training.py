import numpy as np
import matplotlib.pyplot as plt


def create_polynomial(x,i):
    return x**i






def Calibrate(data, targets,name,n, M=2):

    N = len(data) - len(targets)
    print(N)

    if N <= 0:
        K = np.mean(data) * np.ones(-N)
        data = np.append(data, K)
        print(len(data))
    else:
        K = 15.5 * np.ones(N)
        print(K)
        targets = np.append(targets, K)
        print(len(targets))

    phi = np.zeros([len(data), M])

    for i in range(len(data)):
        for j in range(M):
            phi[i,j] = create_polynomial(data[i],j)


    w = np.linalg.inv(phi.T @ phi) @ phi.T @ targets.T

    x = np.linspace(min(data),max(data),100)
    print("max data training= " + str(min(data)))

    y = list(map(lambda x : w[0] + w[1]*x, x))
    plt.scatter(data,targets)
    plt.plot(x,y)
    plt.title(name)
    plt.savefig(name)
    plt.show()
    if n ==1 :
        plt.close()

    return w


def targetsGUI1(data):


    N = round(len(data)/9)

    K = len(data) - N*9



    left = 5.16 * np.ones(N)
    right = 25.83 * np.ones(N)
    midHor = 15.5 * np.ones(N)
    top = 3.333 * np.ones(N)
    bottom = 16.666 * np.ones(N)
    midVer = 10 * np.ones(N)


    targetsHor = np.hstack((midHor, left, right, left, right, left, right, midHor, midHor, 15.5*np.ones(K)))
    targetsVer = np.hstack((midVer, top, bottom, bottom, top, midVer, midVer, top, bottom, 16.666 * np.ones(K)))

    return targetsHor, targetsVer


