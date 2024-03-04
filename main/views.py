from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *



"""  Star EMPLOYEE model  """
@api_view(['GET'])
def filter_employee_profession(request):
    profession = request.GET.get('profession')
    users = Employee.objects.filter(profession__icontains=profession).order_by('-id')
    ser = EmployeeSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_address(request):
    address = request.GET.get('address')
    users = Employee.objects.filter(address__icontains=address).order_by('-id')
    ser = EmployeeSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_experience(request):
    experience = request.GET.get('experience')
    users = Employee.objects.filter(experience__icontains=experience).order_by('-id')
    ser = EmployeeSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_work_time(request):
    work_time = request.GET.get('work_time')
    users = Employee.objects.filter(work_time__icontains=work_time).order_by('-id')
    ser = EmployeeSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_rating(request):
    rating = request.GET.get('rating')
    users = Employee.objects.filter(rating__icontains=rating).order_by('-id')
    ser = EmployeeSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_employee_garaj(request):
    garaj = request.GET.get('garaj')
    users = Employee.objects.filter(garaj__icontains=garaj).order_by('-id')
    ser = EmployeeSerializers(users, many=True)
    return Response(ser.data)

"""  Finished EMPLOYEE model  """





"""  Star ORDER model  """

@api_view(['GET'])
def filter_order_owner_name(request):
    owner_name = request.GET.get('owner_name')
    users = Order.objects.filter(owner_name__icontains=owner_name).order_by('-id')
    ser = OrderSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_owner_phone_number(request):
    owner_phone_number = request.GET.get('owner_phone_number')
    users = Order.objects.filter(owner_phone_number__icontains=owner_phone_number).order_by('-id')
    ser = OrderSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_address(request):
    address = request.GET.get('address')
    users = Order.objects.filter(address__icontains=address).order_by('-id')
    ser = OrderSerializers(users, many=True)
    return Response(ser.data)

@api_view(['GET'])
def filter_order_car_name(request):
    car_name = request.GET.get('car_name')
    users = Order.objects.filter(car_name__icontains=car_name).order_by('-id')
    ser = OrderSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_car_number(request):
    car_number = request.GET.get('profecar_numberssion')
    users = Order.objects.filter(car_number__icontains=car_number).order_by('-id')
    ser = OrderSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_problem(request):
    problem = request.GET.get('problem')
    users = Order.objects.filter(problem__icontains=problem).order_by('-id')
    ser = OrderSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_start_day(request):
    start_day = request.GET.get('start_day')
    users = Order.objects.filter(start_day__icontains=start_day).order_by('-id')
    ser = OrderSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_order_employee(request):
    employee = request.GET.get('employee')
    users = Order.objects.filter(employee__icontains=employee).order_by('-id')
    ser = OrderSerializers(users, many=True)
    return Response(ser.data)

"""  Finished ORDER model  """





"""  Start PAYMENT model  """

@api_view(['GET'])
def filter_payment_order(request):
    order = request.GET.get('order')
    users = Payment.objects.filter(order__icontains=order).order_by('-id')
    ser = PaymentSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_code(request):
    code = request.GET.get('code')
    users = Payment.objects.filter(code__icontains=code).order_by('-id')
    ser = PaymentSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payemnt_created_at(request):
    created_at = request.GET.get('created_at')
    users = Payment.objects.filter(created_at__icontains=created_at).order_by('-id')
    ser = PaymentSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_date(request):
    date = request.GET.get('date')
    users = Payment.objects.filter(date__icontains=date).order_by('-id')
    ser = PaymentSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_payment_type(request):
    payment_type = request.GET.get('payment_type')
    users = Payment.objects.filter(payment_type__icontains=payment_type).order_by('-id')
    ser = PaymentSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_payment_admin(request):
    admin = request.GET.get('admin')
    users = Payment.objects.filter(admin__icontains=admin).order_by('-id')
    ser = PaymentSerializers(users, many=True)
    return Response(ser.data)

"""  Finished PAYMENT model  """





"""  Start Report model  """

@api_view(['GET'])
def filter_report_start_date(request):
    start_date = request.GET.get('start_date')
    users = Report.objects.filter(start_date__icontains=start_date).order_by('-id')
    ser = ReportSerializers(users, many=True)
    return Response(ser.data)



@api_view(['GET'])
def filter_report_end_date(request):
    end_date = request.GET.get('end_date')
    users = Report.objects.filter(end_date__icontains=end_date).order_by('-id')
    ser = ReportSerializers(users, many=True)
    return Response(ser.data)


@api_view(['GET'])
def filter_report_employee(request):
    employee = request.GET.get('employee')
    users = Report.objects.filter(employee__icontains=employee).order_by('-id')
    ser = ReportSerializers(users, many=True)
    return Response(ser.data)

"""  Finished Report model  """





"""  Start GARAJ model  """

@api_view(['GET'])
def filter_garaj_name(request):
    name = request.GET.get('name')
    users = Garaj.objects.filter(name__icontains=name).order_by('-id')
    ser = GarajSerializers(users, many=True)
    return Response(ser.data)

"""  Finished Garaj model  """


