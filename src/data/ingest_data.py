"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""
# pylint: disable=import-outside-toplevel
# pylint: disable=consider-using-f-string

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    import pandas as pd
    #import xlwt

    path = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls'

    years_diff_format = ['2016', '2017']
    years_to_download = [str(year) for year in range(1995, 2022)]
    years_to_download.remove(years_diff_format[0])
    years_to_download.remove(years_diff_format[1])

    def import_data_xlsx(path, file_identifier):

        for year in file_identifier:
            url_path = path + '/' + year + '.xlsx?raw=true'
            #print(url_path)
            file = 'data_lake/landing/{}.xlsx'.format(year)
            download = pd.read_excel(url_path, engine='openpyxl')
            download.to_excel(file, index = None, header = True)

    def import_data_xls(path, file_identifier):

        for year in file_identifier:
            url_path = path + '/' + year + '.xls?raw=true'
            #print(url_path)
            file = 'data_lake/landing/{}.xls'.format(year)
            download = pd.read_excel(url_path)
            download.to_excel(file, index = None, header = True)

    import_data_xlsx(path, years_to_download)
    import_data_xls(path, years_diff_format)

    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    ingest_data()
