import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

if __name__ == "__main__":
    path = 'ad.csv'
    data = pd.read_csv(path);
    x = data[['TV','Radio', 'Newspaper']]
    y = data['Sales']
    print x
    print y

    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)
    linreg = LinearRegression()
    model = linreg.fit(x_train, y_train)
    print model
    print linreg.coef_
    print linreg.intercept_
