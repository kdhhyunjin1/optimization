import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
import seaborn as sns

df = pd.read_csv('csv/generator.csv')
sns.lmplot('RPM', 'VIBRATION', data=df, hue='STATUS', fit_reg=False)
plt.show()

logistic = LogisticRegression()
logistic.fit(train[['RPM', 'VIBRATION']], train['STATUS'])
score = logistic.score(test[['RPM', 'VIBRATION']], test['STATUS'])

print(score)
