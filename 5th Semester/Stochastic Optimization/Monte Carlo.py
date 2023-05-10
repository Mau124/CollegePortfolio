# from scipy.stats import expon
# from scipy.stats import norm
# import numpy
# import random

# # Generate n exponential va
# c = 0.001
# n = 38416
# lamb = 2
# ans = 0

# for i in range(n):
#     tmp = numpy.random.exponential(scale = 1/lamb)
#     ans += norm.pdf(tmp)
# print(ans/n)

# mu = ans/n
# var = 0
# mu_tmp = 0
# mu_array = []
# tmp = random.random()
# mu_array.append(tmp)
# tmp = random.random()
# mu_array.append(tmp)
# for i in range(2, 100):
#     tmp = random.random()
#     mu_array.append(tmp)
    
#     ans = 0 
#     mu_tmp = sum(mu_array)/i
#     for j in range(0, i):
#         ans += (mu_array[j] - mu_tmp)**2
#     var = ans/(i-1)
# print(var)

a = 3
b = 8
b1 = b - 1
a1 = a + 1
r = 156223421
nf = r % (b1 - a1 + 1) + a1
print(nf)