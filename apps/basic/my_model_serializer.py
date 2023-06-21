import inflection
from rest_framework import serializers


class MyModelSerializer(serializers.ModelSerializer):
    """
    在使用 Django Rest Framework 时，我们可以使用序列化器在 JSON 和 Django 模型实例之间转换数据。
    为了解决接口字段和数据库字段之间命名约定不同的问题，我们可以定义一个自定义的序列化器类来覆盖 to_representation 和 to_internal_value 方法。
    to_representation 方法在将 Django 模型实例序列化为 JSON 响应时被调用。
    使用 inflection.camelize 函数将 Django 模型实例中字段名的下划线格式转换为驼峰格式。
    当将 JSON 请求反序列化到 Django 模型实例时，将调用 to_internal_value 方法。
    我们需要做相反的转换，即将JSON请求中字段名的驼峰格式转换为下划线格式。
    我们可以使用 inflection.underscore 函数来进行转换。
    """

    def to_representation(self, instance):
        # 将下划线转化成驼峰格式（接口传出去的数据）
        ret = super().to_representation(instance)
        return {
            inflection.camelize(
                key,
                False): value for key,
            value in ret.items()}

    def to_internal_value(self, data):
        # 将驼峰格式转化成下划线格式（接口传递过来的数据）
        data = {
            inflection.underscore(key): value for key,
            value in data.items()}
        return super().to_internal_value(data)


class MySerializer(serializers.Serializer):
    def to_representation(self, instance):
        ret = super().to_representation(instance)
        return {
            inflection.camelize(
                key,
                False): value for key,
            value in ret.items()}

    def to_internal_value(self, data):
        data = {
            inflection.underscore(key): value for key,
            value in data.items()}
        return super().to_internal_value(data)
