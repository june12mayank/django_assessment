##This will be in APP/serialixers.py

from .models import Document
from rest_framework import serializers

class DocumentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Document
		fields = ("owner","created_time","type","source_type","source_id","input_meta_data")