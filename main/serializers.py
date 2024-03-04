from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'address' )


class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'


class CassaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cassa
        fields = '__all__'


class GarajSerializers(serializers.ModelSerializer):
    class Meta:
        model = Garaj
        fields = '__all__'


class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProfessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'