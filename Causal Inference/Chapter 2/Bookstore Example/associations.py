import numpy as np
from scipy import stats
from colors import bcolors as bc

class BookSCM:
  def __init__(self, random_seed=None):
    self.random_seed = random_seed
    self.u_0 = stats.uniform()
    self.u_1 = stats.norm()

  def sample(self, sample_size=100):
    """Samples from the SCM"""
    if self.random_seed:
      np.random.seed(self.random_seed)

    u_0 = self.u_0.rvs(sample_size)
    u_1 = self.u_1.rvs(sample_size)
    a = u_0 > 0.61
    b = (a + 0.5*u_1) > 0.2

    return a, b

scm = BookSCM(random_seed=45) # instantiate SCM
buy_book_a, buy_book_b = scm.sample(100) # sample 100 samples from SCM
buy_book_a.shape, buy_book_b.shape # check whether the shapes are as expected

proba_book_a_given_book_b = buy_book_a[buy_book_b].sum() / buy_book_a[buy_book_b].shape[0]

print(f"🎲📚 P(A|B): "
      f"{bc.OKGREEN}{proba_book_a_given_book_b:0.3f}{bc.ENDC}")

if __name__ == '__main__':
  __init__(self, random_seed=None)
  sample(self, sample_size=100)
