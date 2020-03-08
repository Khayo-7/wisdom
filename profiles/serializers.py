from rest_framework import serializers


class ser(serializers.Serializer):

    name = serializers.CharField(max_length=10)
     