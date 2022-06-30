"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
# pylint: disable=import-outside-toplevel

import luigi
from luigi import Task, LocalTarget

class DataIngestion(Task):
    '''
    This class ingests all the data
    '''
    def output(self):
        return LocalTarget('data_lake/landing/output.txt')

    def run(self):
        from ingest_data import ingest_data
        with self.output().open('w') as dummy_ingested_files:
            ingest_data()

class DataTransformation(Task):
    '''
    This class ingests all the data
    '''
    def requires(self):
        return DataIngestion()

    def output(self):
        return LocalTarget('data_lake/raw/output.txt')

    def run(self):
        from transform_data import transform_data
        with self.output().open('w') as dummy_transformed_files:
            transform_data()

class CleaningNewTable(Task):
    '''
    This class cleans all the data
    '''
    def requires(self):
        return DataTransformation()

    def output(self):
        return LocalTarget('data_lake/cleansed/output.txt')

    def run(self):
        from clean_data import clean_data
        with self.output().open('w') as dummy_created_table:
            clean_data()

class MeanDailyPrices(Task):
    '''
    This class calculates the average of daily prices
    '''
    def requires(self):
        return CleaningNewTable()

    def output(self):
        return LocalTarget('data_lake/business/output.txt')

    def run(self):
        from compute_daily_prices import compute_daily_prices
        with self.output().open('w') as dummy_daily_prices:
            compute_daily_prices()

class MeanMonthlyPrices(Task):
    '''
    This class calculates the average of monthly prices
    '''
    def requires(self):
        return MeanDailyPrices()

    def output(self):
        return LocalTarget('data_lake/business/output.txt')

    def run(self):
        from compute_monthly_prices import compute_monthly_prices
        with self.output().open('w') as dummy_monthly_prices:
            compute_monthly_prices()

if __name__ == "__main__":

    luigi.run(['MeanMonthlyPrices', '--local-scheduler'])
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
