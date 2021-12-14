import csv
import logging
import pandas as pd

from datetime import datetime as dt

from django.db import connection, transaction

from house_prices.models import CsvData

logger = logging.getLogger(__name__)


def load_raw_csv():
    chunk_size = 10000
    with open(r'C:\Users\naked\dev\hp\data\pp-complete.csv') as csvfile:
        cursor = connection.cursor()
        reader = csv.reader(csvfile)
        query = 'INSERT INTO {} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'.format(CsvData._meta.db_table)
        cg = chunk_generator(reader, chunk_size=chunk_size)
        chunk, i = next(cg), 1
        while len(chunk) > 0:
            cursor.executemany(query, chunk)
            transaction.commit()
            logger.info("Loaded {} records from csv ...".format(chunk_size * i))
            chunk = next(cg)
            i += 1


def load_raw_csv_pandas():
    from sqlalchemy import create_engine
    engine = create_engine(r'sqlite:///../db.sqlite3', echo=False)
    header = [f.name for f in CsvData._meta.get_fields()]
    chunk_size = 100000
    i = 0
    for chunk in pd.read_csv(r'C:\Users\naked\dev\hp\data\pp-complete.csv',
                             header=None,
                             chunksize=chunk_size,
                             parse_dates=[2],
                             index_col=False,
                             date_parser=lambda x: dt.strptime(x, '%Y-%m-%d 00:00').date()):
        chunk.columns = header
        logger.info("Loading {}".format(i))
        i += chunk_size
        chunk.to_sql(CsvData._meta.db_table, con=engine, index=False, if_exists="append")


def chunk_generator(reader, chunk_size=10000):
    chunk = []
    for i, row in enumerate(reader):
        chunk.append(tuple(row))
        if i % chunk_size == 0:
            yield chunk
            chunk = []
