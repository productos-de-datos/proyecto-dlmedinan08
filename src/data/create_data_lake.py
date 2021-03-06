'''
This function creates all data lake files
'''
# pylint: disable=import-outside-toplevel
def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    ___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         ___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
    import os

    os.mkdir("./data_lake")

    parent_dir = 'data_lake/'
    directories = ['landing', 'raw', 'cleansed', 'business']

    parent_dir_business = 'data_lake/business/'
    subdir_business = ['reports', 'features', 'forecasts']

    parent_dir_reports = 'data_lake/business/reports/'
    subdir_reports = ['figures']
    dummy_a = [os.mkdir(os.path.join(parent_dir, dirs)) for dirs in directories]
    dummy_b = [os.mkdir(os.path.join(parent_dir_business, dirs)) for dirs in subdir_business]
    dummy_c = [os.mkdir(os.path.join(parent_dir_reports, dirs)) for dirs in subdir_reports]

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    create_data_lake()
