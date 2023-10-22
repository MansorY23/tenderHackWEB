from datetime import datetime
from rest_framework import serializers
from api.models import Logs


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = ['id', 'create_date',
                  'log', 'cluster',
                  'cluster_name']