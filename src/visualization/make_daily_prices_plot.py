def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """

    import pandas as pd

    precios_diarios = pd.read_csv('data_lake/business/precios-diarios.csv')
    precios_diarios['Fecha'] = pd.to_datetime(precios_diarios['Fecha'], format='%Y-%m-%d')
    precios_diarios.sort_values(by = 'Fecha', inplace= True)
    
    lines = precios_diarios.plot.line(x='Fecha', y='precio')

    lines.figure.savefig("data_lake/business/reports/figures/daily_prices.png")

    return
    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_daily_prices_plot()
