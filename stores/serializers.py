from rest_framework import serializers

from stores.models import MenuItem, Store


class MenuItemRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ["id", "name", "price"]
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

    def update(self, instance, validated_data):
        menu_items_data = validated_data.pop("menu_items")
        menu_items = instance.menu_items

        instance.name = validated_data.get("name", instance.name)
        instance.notes = validated_data.get("notes", instance.notes)
        instance.save()

                # for menu_item in menu_items_data:
        #     menu_items.name = menu_item.get("name", "")
        #     menu_items.price = menu_item.get("price", 0)
        #     menu_items.save()

        return instance
