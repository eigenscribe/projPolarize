import numpy as np
from scipy import stats
from colors import bcolors as bc

SAMPLE_SIZE = 100
np.random.seed(45)

u_0 = np.random.randn(SAMPLE_SIZE)
u_1 = np.random.randn(SAMPLE_SIZE)

a = u_0
b = 5 * a + u_1

r, p = stats.pearsonr(a,b)

print(f"Correlation between A and B:\t{bc.OKCYAN}r = {r:0.3f}{bc.ENDC}; {bc.OKGREEN}p = {p:0.3f}{bc.ENDC}\n\n")

print(f"✨✨ Mean and Variance of B before vs. after Intervention on A ✨✨\n")

print(f"Mean of B before any intervention: {bc.PURPLE}{b.mean():0.3f}{bc.ENDC}")
print(f"Variance of B before any intervention: {bc.BLUE}{b.var():0.3f}{bc.ENDC}\n")

# Intervene on A by fixing its value to 1.5
a = np.array([1.5] * SAMPLE_SIZE)
b = 5 * a + u_1

print(f"Mean of B after intervention on A: {bc.PURPLE}{b.mean():0.3f}{bc.ENDC}")
print(f"Variance of B after intervention on A: {bc.BLUE}{b.var():03f}{bc.ENDC}\n")
