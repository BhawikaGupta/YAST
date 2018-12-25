from .models import *
from rest_framework import serializers

class ActiveCampaigns(serializers.ModelSerializer):
    class Meta:
        model = active_campaigns
        fields = ("CAMPAIGN_ID", "ZIP" , "ADDRESS" , "CITY" , "STATE" , "COUNTRY" , "LONGITUDE", "LATITUDE", "CHAIN_ID" , "DATE" , "SLOTS")
       
    def create(self, validated_data):
        return active_campaigns.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.CAMPAIGN_ID = validated_data.get('CAMPAIGN_ID', instance.CAMPAIGN_ID)
        instance.ZIP = validated_data.get('ZIP', instance.ZIP)   
        instance.ADDRESS = validated_data.get('ADDRESS', instance.ADDRESS)   
        instance.CITY = validated_data.get('CITY', instance.CITY)  
        instance.STATE = validated_data.get('STATE', instance.STATE)   
        instance.COUNTRY = validated_data.get('COUNTRY', instance.COUNTRY) 
        instance.LONGITUDE = validated_data.get('LONGITUDE', instance.LONGITUDE)  
        instance.LATITUDE = validated_data.get('LATITUDE', instance.LATITUDE) 
        instance.CHAIN_ID = validated_data.get('CHAIN_ID', instance.CHAIN_ID)
        instance.DATE = validated_data.get('DATE', instance.DATE)
        instance.SLOTS = validated_data.get('SLOTS', instance.SLOTS)
        instance.save()
        return instance

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    
class UserSerializer(serializers.Serializer):
    USEREMAIL = serializers.CharField(max_length = 100)
    USERNAME = serializers.CharField(max_length = 100)
    CONTACT = serializers.CharField(max_length = 100)
    BLOOD_GP = serializers.CharField(max_length = 100)
    GENDER = serializers.CharField(max_length = 100)
    AGE = serializers.IntegerField()
    ZIP = serializers.CharField(max_length = 100)
    ADDRESS = serializers.CharField(max_length = 100)
    CITY = serializers.CharField(max_length = 100)
    STATE = serializers.CharField(max_length = 100)
    COUNTRY = serializers.CharField(max_length = 100)
    #DONATE_Bf = serializers.CharField(max_length = 100)
    #LONGITUDE = serializers.CharField(max_length = 100)
    #LATITUDE = serializers.CharField(max_length = 100)
    
    def create(self, validated_data):
        return users_profile.objects.create(**validated_data)
      
    def update(self, instance, validated_data):
        instance.USEREMAIL = validated_data.get('USEREMAIL', instance.USEREMAIL)
        instance.USERNAME = validated_data.get('USERNAME', instance.USERNAME)
        instance.CONTACT = validated_data.get('CONTACT', instance.CONTACT)  
        instance.BLOOD_GP = validated_data.get('BLOOD_GP', instance.BLOOD_GP)   
        instance.GENDER = validated_data.get('GENDER', instance.GENDER)  
        instance.AGE = validated_data.get('AGE', instance.AGE)  
        instance.ZIP = validated_data.get('ZIP', instance.ZIP)   
        instance.ADDRESS = validated_data.get('ADDRESS', instance.ADDRESS)   
        instance.CITY = validated_data.get('CITY', instance.CITY)  
        instance.STATE = validated_data.get('STATE', instance.STATE)   
        instance.COUNTRY = validated_data.get('COUNTRY', instance.COUNTRY)  
        #instance.DONATE_Bf = validated_data.get('DONATE_Bf', instance.DONATE_Bf)
        #instance.LONGITUDE = validated_data.get('LONGITUDE', instance.LONGITUDE)  
        #instance.LATITUDE = validated_data.get('LATITUDE', instance.LATITUDE)  
        instance.save()
        return instance
        