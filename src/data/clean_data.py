'''
This process concatenates all files and transforms it into three columns instead of 25
'''

# pylint: disable=import-outside-toplevel

def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo
    data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    import pandas as pd
    import glob

    path = glob.glob(r'data_lake/raw/*.csv')

    #print(enumerate(path))

    for index, file in enumerate(path):
        if index == 0:
            # print(file)
            database = pd.read_csv(file)
            database.columns = ['Fecha']+[('0'+str(i))[-2:] for i in range(24)]
            database_melted = database.melt(
                id_vars= ['Fecha'], var_name='Hora', value_name='precio')
            temp = database_melted.copy()
        else:
            # print(file)
            database = pd.read_csv(file)
            database.columns = ['Fecha']+[('0'+str(i))[-2:] for i in range(24)]
            database_melted = database.melt(
                id_vars= ['Fecha'], var_name='Hora', value_name='precio')
            temp = pd.concat([temp, database_melted])

    #print(temp['Fecha'].unique())
    temp.to_csv('data_lake/cleansed/precios-horarios.csv', index=None)

    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    clean_data()
