import csv
import logging

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from house_prices.models import CsvData

logger = logging.getLogger(__name__)

from django.db import connection, transaction


# engine = create_engine(r'sqlite:///../db.sqlite3', echo=False)
# session = Session(bind=engine)

# @pytest.mark.django_db(transaction=True)
# def test_load_raw_csv():
#     with open(r'C:\Users\naked\dev\hp\data\pp-complete.csv') as csvfile:
#         cursor = connection.cursor()
#         reader = csv.reader(csvfile)
#         query = 'INSERT INTO {} VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'.format(CsvData._meta.db_table)
#         chunk = []
#         i = 0
#         for row in reader:
#
#             chunk.append(tuple(row))
#             if i == 100:
#                 break
#             i += 1
#         cursor.executemany(query, chunk)
#         transaction.commit()

# import logging
# from datetime import datetime as dt
#
# import pandas as pd
#
# from house_prices.models import CsvData
#
# logger = logging.getLogger(__name__)
#
#
# # def parse_postcode(value: str):
# #     m = re.match(r'(^[a-zA-Z]{1,2})(\d{1,2}|\d[a-zA-Z]{0,1})(\s+)(\d)([a-zA-Z]{1,2})', value)
# #     return Postcode(area=m.group(1),
# #                     district=m.group(2),
# #                     sector=m.group(4),
# #                     unit=m.group(5))
#
#
# def test_read_csv():
#     from sqlalchemy import create_engine
#     engine = create_engine(r'sqlite:///../db.sqlite3', echo=False)
#     header = [f.name for f in CsvData._meta.get_fields()]
#     chunk_size = 100000
#     i = 0
#     for chunk in pd.read_csv(r'C:\Users\naked\dev\hp\data\pp-complete.csv',
#                              header=None,
#                              chunksize=chunk_size,
#                              parse_dates=[2],
#                              index_col=False,
#                              date_parser=lambda x: dt.strptime(x, '%Y-%m-%d 00:00').date()):
#         chunk.columns = header
#         logger.info("Loading {}".format(i))
#         i += chunk_size
#         chunk.to_sql(CsvData._meta.db_table, con=engine, index=False, if_exists="append")
