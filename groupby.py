import pandas as pd 
import numpy as np

df = pd.DataFrame({
       "A":["verdadeiro", "falso", "verdadeiro", "falso", "verdadeiro", "falso", "verdadeiro", "falso"],
       "B":["um", "dois", "tres", "um", "dois", "tres", "um", "dois"],
       "C":np.random.randn(8),
       "D":np.random.randn(8)
})
#df = df.groupby(['A']).sum
df = df.groupby(['A','B']).sum()
