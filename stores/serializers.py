from rest_framework import serializers

from stores.models import MenuItem, Store


class MenuItemRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["name", "price"]
        # fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    menu_items = MenuItemRelatedSerializer(many=True)

    class Meta:
        model = Store
        fields = '__all__'

    # Writable nested serializers
    def create(self, validated_data):
        menu_items_data = validated_data.pop("menu_items")
        store = Store.objects.create(**validated_data)
        for menu_item in menu_items_data:
            MenuItem.objects.create(store=store, **menu_item)
        return store
