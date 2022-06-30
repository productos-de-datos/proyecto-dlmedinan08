'''
This process creates a csv file with a the features to train the model
'''
# pylint: disable=import-outside-toplevel

def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
    import pandas as pd

    precios_diarios = pd.read_csv('data_lake/business/precios-diarios.csv')
    precios_diarios['Fecha'] = pd.to_datetime(precios_diarios['Fecha'], format='%Y-%m-%d')
    precios_diarios.sort_values(by = 'Fecha', inplace= True)
    precios_diarios['precio_lag1'] = precios_diarios['precio'].shift(1)
    precios_diarios['precio_lag30'] = precios_diarios['precio'].shift(30)
    precios_diarios['precio_lag60'] = precios_diarios['precio'].shift(60)
    precios_diarios['precio_lag90'] = precios_diarios['precio'].shift(90)

    precios_diarios.to_csv('data_lake/business/features/precios-diarios.csv', index=None)

    # raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_features()
