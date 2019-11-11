from fdfs_client.client import Fdfs_client
from rest_framework import serializers

from apps.goods.models import Brand


class Brandserilizer(serializers.ModelSerializer):


    class Meta:

        model = Brand

        fields = ('name','logo','first_letter')

    def create(self, validated_data):


        logo = validated_data['logo']
        print(validated_data)
        client = Fdfs_client('utils/fastdfs/client.conf')
        res = client.upload_by_buffer(logo.read())
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError('上传失败')
        path = res.get('Remote file_id')

        brand = Brand.objects.create(logo=path,name=validated_data['name'],first_letter=validated_data['first_letter'])
        return brand
    def update(self, instance, validated_data):

        name = validated_data['name']
        first_letter = validated_data['first_letter']
        logo = validated_data['logo']
        print(validated_data)
        client = Fdfs_client('utils/fastdfs/client.conf')
        res = client.upload_by_buffer(logo.read())
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError('上传失败')
        path = res.get('Remote file_id')
        instance.name = name
        instance.first_letter = first_letter
        instance.logo = path
        instance.save()
        return instance