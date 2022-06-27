def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """

    import pandas as pd 

    precios_horarios = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    precios_diarios = pd.DataFrame(precios_horarios.groupby('Fecha')['precio'].mean()).reset_index()

    precios_diarios.to_csv('data_lake/business/precios-diarios.csv', index=None)

    return
    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_daily_prices()
