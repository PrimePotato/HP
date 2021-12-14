# Create your views here.


# Load CSV

# Clear Data

import re

# Grouped Data
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet

from .data import load_raw_csv_pandas, load_raw_csv
from .models import CsvData, Postcode, UniquePostcodes
from .serializers import CsvDataSerializer


class CsvViewSet(ModelViewSet):
    queryset = CsvData.objects.filter(price__gt=30e6)
    serializer_class = CsvDataSerializer


class LoadCsvDataViewSet(ViewSet):
    def list(self, request):
        # try:
        load_raw_csv_pandas()
        return Response({"status": "success"}, status=status.HTTP_200_OK)
    # except Exception as e:
    #     return Response({"status": "failed"}, status=status.HTTP_400_BAD_REQUEST)


class UniquePostcodesViewSet(ViewSet):

    @staticmethod
    def _parse_postcode(value: str):
        m = re.match(r'(^[a-zA-Z]{1,2})(\d{1,2}|\d[a-zA-Z]{0,1})(\s+)(\d)([a-zA-Z]{1,2})', value)
        return Postcode(area=m.group(1),
                        district=m.group(2),
                        sector=m.group(4),
                        unit=m.group(5))

    def list(self, request):
        try:
            qs = UniquePostcodes.objects.all()
            for up in qs.iterator():
                p = self._parse_postcode(up.postcode)
                p.save()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"status": "failed"}, status=status.HTTP_400_BAD_REQUEST)
