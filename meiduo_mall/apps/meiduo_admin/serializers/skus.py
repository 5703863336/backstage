from django.db import transaction
from rest_framework import serializers

from apps.goods.models import SKU, GoodsCategory, SPUSpecification, SpecificationOption, SKUSpecification


class SKUSpecificationSerializer(serializers.ModelSerializer):
    """
           SKU具体规格序列化器
    """
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        model = SKUSpecification
        fields = ('spec_id', 'option_id')


class SKUSerializer(serializers.ModelSerializer):
    """
        SKU商品序列化器
    """
    ## spu和category不需要参与保存和更新
    spu = serializers.StringRelatedField(read_only=True)
    category = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()
    category_id = serializers.IntegerField()

    # 关联sku具体规格表
    specs = SKUSpecificationSerializer(many=True)

    class Meta:
        model = SKU
        fields = '__all__'

    # 重写父类保存方法完成sku表和sku具体规格表两张表
    def create(self, validated_data):
        # 1、获取specs数据
        specs = validated_data.get('specs')
        # 2、将specs数据从validated_data删除
        del validated_data['specs']
        # 保存sku表数据
        sku = super().create(validated_data)
        # 保存sku具体规格表数据
        for spec in specs:
            SKUSpecification.objects.create(sku=sku, spec_id=spec['spec_id'], option_id=spec['option_id'])

        return sku

    def update(self, instance, validated_data):
        specs = validated_data.get('specs')
        del validated_data['specs']

        with transaction.atomic():
            save_point = transaction.savepoint()

            try:
                sku = super().update(instance,validated_data)
                for spec in specs:
                    SKUSpecification.objects.create(sku=instance,specs_id=spec['spec_id']).update(option_id=spec['option_id'])
            except:
                transaction.savepoint_rollback(save_point)
                raise serializers.ValidationError('保存失败')
            else:
                transaction.savepoint_commit(save_point)
                return sku

class GoodsCategorySerializer(serializers.ModelSerializer):
    """
        商品分类序列化器
    """

    class Meta:
        model = GoodsCategory
        fields = '__all__'


class SpecificationOptionSerializer(serializers.ModelSerializer):
    """
     商品规格选项序列化器
    """

    class Meta:
        model = SpecificationOption
        fields = ('id', 'value')


class SPUSpecificationSerializer(serializers.ModelSerializer):
    """
        商品规格序列化器
    """
    # 关联嵌套返回，返回规格时将规格选项一块返回 父表嵌套子表返回
    options = SpecificationOptionSerializer(many=True)

    # 将关联的spu数据返回 子表嵌套父表
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification
        fields = '__all__'
