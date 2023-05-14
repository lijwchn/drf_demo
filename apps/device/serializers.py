from .models import Device
from apps.basic.my_model_serializer import MyModelSerializer


class DeviceSerializer(MyModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'
