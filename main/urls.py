from django.urls import path
from .views import *


urlpatterns = [
    # >>>>>>>>>> FILTER Employee <<<<<<<<<< #
    path('filter-employee-profession/',  filter_employee_profession),
    path('filter-employee-address/', filter_employee_address),
    path('filter-employee-experience/', filter_employee_experience),
    path('filter-employee-work-time/', filter_employee_work_time),
    path('filter-employee-rating/', filter_employee_rating),
    path('filter-employee-garaj/', filter_employee_garaj),


    # >>>>>>>>>> FILTER Order <<<<<<<<<< #
    path('filter-order-owner-name/', filter_order_owner_name),
    path('filter-order-owner-phone-number/', filter_order_owner_phone_number),
    path('filter-order-address/', filter_order_address),
    path('filter-order-car-name/', filter_order_car_name),
    path('filter-order-car-number/', filter_order_car_number),
    path('filter-order-problem/', filter_order_problem),
    path('filter-order-start-day/', filter_order_start_day),
    path('filter-order-employee/', filter_order_employee),


    # >>>>>>>>>> FILTER Payment <<<<<<<<<< #
    path('filter-payment-order/', filter_payment_order),
    path('filter-payment-code/', filter_payment_code),
    path('filter-payemnt-created-at/', filter_payemnt_created_at),
    path('filter-payment-date/', filter_payment_date),
    path('filter-payment-payment-type/', filter_payment_payment_type),
    path('filter-payment-admin/', filter_payment_admin),


    # >>>>>>>>>> FILTER Garaj <<<<<<<<<< #
    path('filter-garaj-name/', filter_garaj_name),


    # >>>>>>>>>> FILTER Report <<<<<<<<<< #
    path('filter_report_start_date/', filter_report_start_date),
    path('filter_report_end_date/', filter_report_end_date),
    path('filter_report_employee/', filter_report_employee),

]
