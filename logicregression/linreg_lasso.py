import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso, Ridge
from sklearn.model_selection import GridSearchCV


if __name__ == "__main__":
    path = 'ad.csv'
    data = pd.read_csv(path);
    x = data[['TV','Radio', 'Newspaper']]
    y = data['Sales']
    print x
    print y

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
    model = Lasso()
    #model = Ridge()

    alpha_can = np.logspace(-3, 2, 10)
    lasso_model = GridSearchCV(model, param_grid={'alpha': alpha_can}, cv=5)
    lasso_model.fit(x, y)
    print lasso_model.best_params_
