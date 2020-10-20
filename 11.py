import csv
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist
import seaborn as sns

list = []

df = pd.read_csv('csv/cluster_sample_2.csv')
km = KMeans(n_clusters=15).fit(df[['x', 'y']])

df['cluster_id'] = km.labels_

sns.lmplot('x', 'y', data=df, hue='cluster_id', fit_reg=False)
plt.show()
