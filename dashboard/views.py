from main.models import *
from main.serializers import *
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView





"""  Star CRUD model  """
# Employee model
# read
class GetAllEmployeeItems(ListAPIView):
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializers


# create
class CreateAllEmployeeItems(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers


#  update
class UpdateAllEmployeeItems(UpdateAPIView):
   queryset = Employee.objects.all()
   serializer_class = EmployeeSerializers


#  delete
class DeleteAllEmployeeItems(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers




# Order model
# read
class GetAllOrderItems(ListAPIView):
    queryset = Order.objects.all().order_by('-id')
    serializer_class = OrderSerializers


# create
class CreateAllOrderItems(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers


#  update
class UpdateAllOrderItems(UpdateAPIView):
   queryset = Order.objects.all()
   serializer_class = OrderSerializers


#  delete
class DeleteAllOrderItems(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializers




# Payment model
# read
class GetAllPaymentItems(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers


# create
class CreateAllPaymentItems(ListCreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers


#  update
class UpdateAllPaymentItems(UpdateAPIView):
   queryset = Payment.objects.all()
   serializer_class = PaymentSerializers


#  delete
class DeleteAllPaymentItems(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializers




# Cassa model
# read
class GetAllCassaItems(ListAPIView):
    queryset = Cassa.objects.all().order_by('-id')
    serializer_class = CassaSerializers


# create
class CreateAllCassaItems(ListCreateAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers


#  update
class UpdateAllCassaItems(UpdateAPIView):
   queryset = Cassa.objects.all()
   serializer_class = CassaSerializers


#  delete
class DeleteAllCassaItems(DestroyAPIView):
    queryset = Cassa.objects.all()
    serializer_class = CassaSerializers




# Garaj model
# read
class GetAllGarajItems(ListAPIView):
    queryset = Garaj.objects.all().order_by('-id')
    serializer_class = GarajSerializers


# create
class CreateAllGarajItems(ListCreateAPIView):
    queryset = Garaj.objects.all()
    serializer_class = GarajSerializers


#  update
class UpdateAllGarajItems(UpdateAPIView):
   queryset = Garaj.objects.all()
   serializer_class = GarajSerializers


#  delete
class DeleteAllGarajItems(DestroyAPIView):
    queryset = Garaj.objects.all()
    serializer_class = GarajSerializers




# Report model
# read
class GetAllReportItems(ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers


# create
class CreateAllReportItems(ListCreateAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers


#  update
class UpdateAllReportItems(UpdateAPIView):
   queryset = Report.objects.all()
   serializer_class = ReportSerializers


#  delete
class DeleteAllReportItems(DestroyAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializers




# Profession model
# read
class GetAllProfessionItems(ListAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializers


# create
class CreateAllProfessionItems(ListCreateAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializers


#  update
class UpdateAllProfessionItems(UpdateAPIView):
   queryset = Profession.objects.all()
   serializer_class = ProfessionSerializers


#  delete
class DeleteAllProfessionItems(DestroyAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializers




# Comment model
# read
class GetAllCommentItems(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


# create
class CreateAllCommentItems(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


#  update
class UpdateAllCommentItems(UpdateAPIView):
   queryset = Comment.objects.all()
   serializer_class = CommentSerializers


#  delete
class DeleteAllCommentItems(DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers