from rest_framework import serializers
from backend.models import *

class AccessSerializer(serializers.ModelSerializer):
	class Meta:
		model = Access
		fields = ('id', 'image','user',)
