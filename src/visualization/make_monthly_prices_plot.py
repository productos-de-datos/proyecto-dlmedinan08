def make_monthly_prices_plot():
    """Crea un grafico de lines que representa los precios promedios mensuales.

    Usando el archivo data_lake/business/precios-mensuales.csv, crea un grafico de
    lines que representa los precios promedios mensuales.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/monthly_prices.png.

    """

    import pandas as pd

    precios_mensuales = pd.read_csv('data_lake/business/precios-mensuales.csv')
    precios_mensuales['Fecha'] = pd.to_datetime(precios_mensuales['Fecha'], format='%Y-%m-%d')
    precios_mensuales.sort_values(by = 'Fecha', inplace= True)
    
    lines = precios_mensuales.plot.line(x='Fecha', y='precio')

    lines.figure.savefig("data_lake/business/reports/figures/monthly_prices.png")

    return
    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    make_monthly_prices_plot()