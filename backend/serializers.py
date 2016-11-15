from rest_framework import serializers
from backend.models import *

class AccessSerializer(serializers.ModelSerializer):
	class Meta:
		model = Access
		fields = ('id', 'image','user',)





# class AccessSerializer(serializers.Serializer):
#     user_email = serializers.CharField(required=True,max_length=100,allow_blank=False)
#     password = serializers.CharField(required=True,max_length=100,allow_blank=False)
#     creation_date = serializers.DateField()
#     authorised = serializers.IntegerField()
#     email_verify_code = serializers.CharField(required=True,max_length=100,allow_blank=False)
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Access.objects.create(**validated_data)
#
#
#
# from backend.models import Access
# from backend.serializers import AccessSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# access = Access(user_email="hello, world",password="hello, world",creation_date="1993-07-06",authorised="1",email_verify_code="3")
# access.save()
# serializer = AccessSerializer(access)
# serializer.data
# content = JSONRenderer().render(serializer.data)
# content
