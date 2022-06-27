def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import pandas as pd

    def transform_to_csv(year, header, fil_ext):
        read_file = pd.read_excel("data_lake/landing/{}{}".format(year, fil_ext), header=header).iloc[:,0:25]
        read_file['Fecha'] = pd.to_datetime(read_file['Fecha'], format='%Y-%m-%d')
        read_file.to_csv("data_lake/raw/{}.csv".format(year), index=None)

        return

    for year in range(1995,2022):
        if year in range(1995,2000):
            transform_to_csv(year, 3, '.xlsx')
        elif year in range(2000, 2016):
            transform_to_csv(year, 2, '.xlsx')
        elif year in range(2016, 2018):
            transform_to_csv(year, 2, '.xls')
        else:
            transform_to_csv(year, 0, '.xlsx')

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()