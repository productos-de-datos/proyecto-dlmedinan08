'''
This process trains a linear regression model
'''
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with

def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    import pandas as pd
    from sklearn import linear_model
    from sklearn.metrics import r2_score
    import pickle

    precios_diarios = pd.read_csv('data_lake/business/features/precios-diarios.csv', index_col=None)
    precios_diarios['Fecha'] = pd.to_datetime(precios_diarios['Fecha'], format= '%Y-%m-%d')
    precios_diarios['year'] = precios_diarios['Fecha'].dt.year
    precios_diarios['month'] = precios_diarios['Fecha'].dt.month
    precios_diarios['day'] = precios_diarios['Fecha'].dt.day

    precios_diarios.dropna(inplace=True)

    x_complete = precios_diarios.copy().drop(columns = 'Fecha')
    y_complete = x_complete.pop('precio')

    x_train = x_complete[:round(x_complete.shape[0]*0.75)]
    x_test = x_complete[round(x_complete.shape[0]*0.75):]
    y_train = y_complete[:round(y_complete.shape[0]*0.75)]
    y_test = y_complete[round(y_complete.shape[0]*0.75):]

    regression = linear_model.LinearRegression()
    regression.fit(x_train, y_train)

    r2_score(y_test,regression.predict(x_test))

    pickle.dump(regression, open('src/models/precios-diarios.pkl', 'wb'))

    # raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    train_daily_model()
