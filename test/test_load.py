from django.test import TestCase
from house_prices.models import Transaction

import pandas as pd
from datetime import datetime as dt

from house_prices.models import Transaction


def read_csv():
    header = [f.name for f in Transaction._meta.get_fields()]
    for chunk in pd.read_csv(r'C:\Users\naked\dev\hp\data\pp-complete.csv',
                             header=None,
                             chunksize=100,
                             parse_dates=[2],
                             date_parser=lambda x: dt.strptime(x, '%Y-%m-%d 00:00').date()):
        chunk.columns = header
        chunk.set_index(header[0])



read_csv()
