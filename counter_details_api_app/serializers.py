from rest_framework import serializers
from .models import CounterDetails


class CounterDetailsSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = CounterDetails
        fields = "__all__"
