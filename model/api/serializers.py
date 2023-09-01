from rest_framework import serializers


class ModelSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    bmi = serializers.FloatField()
    children = serializers.IntegerField()
    smoker = serializers.CharField(max_length=3)


class CSVFileSerializer(serializers.Serializer):
    file = serializers.FileField()
