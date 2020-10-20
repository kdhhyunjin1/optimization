from sklearn.datasets import fetch_california_housing
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd

CF_data=fetch_california_housing()
CF=pd.DataFrame(data=CF_data.data, columns=CF_data.feature_names)
CF['target']=CF_data.target

scatter_matrix(CF)
plt.show()