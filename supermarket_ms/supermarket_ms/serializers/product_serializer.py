from rest_framework import serializers
from supermarket_ms.models.product_model import Product
from supermarket_ms.models.category_model import Category
from supermarket_ms.serializers.category_serializer import CategorySerializer
from supermarket_ms.models.color_model import Color
from supermarket_ms.serializers.color_serializer import ColorSerializer

class ProductSerializer(serializers.ModelSerializer):

    unit_measurement = serializers.ChoiceField(choices={"Units":"UN", "Liters":"LI", "Grams":"GR",})

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'unit_measurement', 'quantity', 'color']

    def create(self, validated_data):

        um_long_to_short={"Units":"UN", "Liters":"LI", "Grams":"GR",}

        product = Product(name = validated_data.get("name"),
                          description = validated_data.get("description"),
                          quantity = validated_data.get("quantity"),
                          unit_measurement = um_long_to_short[validated_data.get("unit_measurement")],
                          category = validated_data.get("category"),
                          color = validated_data.get("color"))
        product.save()
        return product

    def update(self, instance, validated_data):

        um_long_to_short={"Units":"UN", "Liters":"LI", "Grams":"GR",}

        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.quantity = validated_data.get("quantity")
        instance.unit_measurement = um_long_to_short[validated_data.get("unit_measurement")]
        instance.category = validated_data.get("category")
        instance.color = validated_data.get("color")
        instance.save()
        return instance

    def to_representation(self, obj):

        data = super().to_representation(obj)

        um_short_to_long={"UN":"Units", "LI":"Liters", "GR":"Grams",}

        category = Category.objects.get(id = data["category"])
        categorySerializer = CategorySerializer(category)
        data["category"] = categorySerializer.data

        color = Color.objects.get(id = data["color"])
        colorSerializer = ColorSerializer(color)
        data["color"] = colorSerializer.data

        data["unit_measurement"] = um_short_to_long[data["unit_measurement"]]

        return data
