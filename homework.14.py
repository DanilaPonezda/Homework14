import numpy as np
import pandas as pd

a = np.round(np.random.randn(5,1),7)
#rows = ['Z','X','M']
cols = ['A','B','C','D','E']

panda = pd.DataFrame(a,cols)

print(panda)