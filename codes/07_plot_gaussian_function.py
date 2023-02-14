import numpy as np
import matplotlib.pyplot as plt

def gaussian(mu, sigma, size):
    x = np.arange(-1,1,1/size)
    guass = (1/np.sqrt(2*np.pi*np.square(sigma)))*np.exp(-np.square(x-mu)/(2*np.square(sigma)))
    return guass

def plot_gauss(mu, sigma, size):
    rand_guass = np.random.normal(mu,sigma,size)
    plt.hist(rand_guass,30,density=True)
    plt.plot(x,gaussian(mu,sigma,size))
    plt.title(f"mu: {mu} sigma: {sigma}")

size = 1000
x = np.arange(-1,1,1/size)

plt.subplot(2,2,1)
mu,sigma = 0,0.1
plot_gauss(mu, sigma, size)

plt.subplot(2,2,2)
mu,sigma = 0.2,0.1
plot_gauss(mu, sigma, size)

mu,sigma = 0,0.5
plt.subplot(2,2,3)
rand_guass = np.random.normal(mu,sigma,size)
plot_gauss(mu, sigma, size)

mu,sigma = 0.2,0.5
plt.subplot(2,2,4)
plot_gauss(mu, sigma, size)

plt.show()