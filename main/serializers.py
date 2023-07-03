from rest_framework import serializers
from main.models import MyToDo

class MySerializers(serializers.ModelSerializer):
    class Meta:
        model = MyToDo
        fields = "__all__"