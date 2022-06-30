'''
This process forecasts a linear regression model
'''
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-with

def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    import pandas as pd
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

    regression = pickle.load(open('src/models/precios-diarios.pkl', 'rb'))
    prediction = regression.predict(x_complete)

    r2_score(y_complete,regression.predict(x_complete))

    precios_diarios['Prediction'] = prediction

    precios_diarios[['Fecha', 'precio', 'Prediction']].to_csv(
        'data_lake/business/forecasts/precios-diarios.csv', index=None)

    # raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_forecasts()
