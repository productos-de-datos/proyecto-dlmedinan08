"""
Construya un pipeline de Luigi que:

* Importe los datos xls
* Transforme los datos xls a csv
* Cree la tabla unica de precios horarios.
* Calcule los precios promedios diarios
* Calcule los precios promedios mensuales

En luigi llame las funciones que ya creo.


"""
import luigi
from luigi import Task, LocalTarget

class data_ingestion(Task):

    def output(self):
        return LocalTarget('data_lake/landing/output.txt')

    def run(self):
        from ingest_data import ingest_data
        with self.output().open('w') as ingested_files:
            ingest_data()

class data_transformation(Task):
    def requires(self):
        return data_ingestion()

    def output(self):
        return LocalTarget('data_lake/raw/output.txt')

    def run(self):
        from transform_data import transform_data
        with self.output().open('w') as transformed_files:
            transform_data()

class cleaning_new_table(Task):
    def requires(self):
        return data_transformation()

    def output(self):
        return LocalTarget('data_lake/cleansed/output.txt')

    def run(self):
        from clean_data import clean_data
        with self.output().open('w') as created_table:
            clean_data()

class mean_daily_prices(Task):
    def requires(self):
        return cleaning_new_table()

    def output(self):
        return LocalTarget('data_lake/business/output.txt')

    def run(self):
        from compute_daily_prices import compute_daily_prices
        with self.output().open('w') as daily_prices:
            compute_daily_prices()

class mean_monthly_prices(Task):
    def requires(self):
        return mean_daily_prices()

    def output(self):
        return LocalTarget('data_lake/business/output.txt')

    def run(self):
        from compute_monthly_prices import compute_monthly_prices
        with self.output().open('w') as monthly_prices:
            compute_monthly_prices()

if __name__ == "__main__":
    
    luigi.run(['mean_monthly_prices', '--local-scheduler'])
    #raise NotImplementedError("Implementar esta función")

if __name__ == "__main__":
    import doctest

    doctest.testmod()
