def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
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
            df = pd.read_csv(file)
            df.columns = ['Fecha']+[('0'+str(i))[-2:] for i in range(24)]
            df_melted = df.melt(id_vars= ['Fecha'], var_name='Hora', value_name='precio')
            temp = df_melted.copy()
        else:
            # print(file)
            df = pd.read_csv(file)
            df.columns = ['Fecha']+[('0'+str(i))[-2:] for i in range(24)]
            df_melted = df.melt(id_vars= ['Fecha'], var_name='Hora', value_name='precio')
            temp = pd.concat([temp, df_melted])
    
    #print(temp['Fecha'].unique())
    temp.to_csv('data_lake/cleansed/precios-horarios.csv', index=None)

    return 
    #raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    clean_data()
