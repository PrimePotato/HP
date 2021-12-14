from rest_framework import serializers

from house_prices.models import CsvData


class CsvDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CsvData
        fields = [f.name for f in CsvData._meta._get_fields()]
