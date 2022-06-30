'''
This process averages the monthly prices
'''
# pylint: disable=import-outside-toplevel

def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    import pandas as pd

    precios_horarios = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    precios_horarios['Fecha'] = pd.to_datetime(precios_horarios['Fecha'], format='%Y-%m-%d')
    precios_mensuales = precios_horarios.groupby(
        precios_horarios['Fecha'].dt.to_period('M'))['precio'].mean().reset_index()
    precios_mensuales.rename(columns= {'year-month':'Fecha'}, inplace= True)
    precios_mensuales['Fecha'] = pd.to_datetime(
        precios_mensuales['Fecha'].astype(str), format='%Y-%m')

    precios_mensuales.to_csv('data_lake/business/precios-mensuales.csv', index=None)

def test_correct_column_number():
    '''
    This test checks if the output file has the correct number of columns
    '''
    import pandas as pd

    precios_mensuales = pd.read_csv('data_lake/business/precios-mensuales.csv')
    assert 3 == len(precios_mensuales.columns)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_monthly_prices()
    