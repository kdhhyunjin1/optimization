from sklearn.datasets import load_boston
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

boston_data = load_boston()

boston = pd.DataFrame(data=boston_data.data, columns=boston_data.feature_names)
boston['target'] = boston_data.target

train = boston.sample(frac=0.8, random_state=200)
test = boston.drop(train.index)

mlr = LinearRegression()
mlr.fit(train[['PTRATIO', 'INDUS', 'NOX', 'B', 'CHAS', 'RAD', 'TAX', 'ZN', 'DIS', 'CRIM', 'RM', 'LSTAT', 'AGE']],
        train['target'])

for i, row in test.iterrows():
    params = result.params
    r_estimate = row['PTRATIO'] * params['PTRATIO'] + row['INDUS'] * params['INDUS'] + row['NOX'] * params['NOX'] + \
                 row['B'] * params['B'] + row['CHAS'] * params['CHAS'] + row['RAD'] * params['RAD'] + \
                 row['TAX'] * params['TAX'] + row['ZN'] * params['ZN'] + row['DIS'] * params['DIS'] + row['CRIM'] * \
                 params['CRIM'] + row['RM'] * params['RM'] + row['LSTAT'] * params['LSTAT'] + params['Intercept']
