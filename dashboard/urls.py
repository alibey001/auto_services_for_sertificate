from django.urls import path
from .views import *


urlpatterns = [
    # >>>>>>>>>> CRUD Employee Model <<<<<<<<<< #
    path('get-employee-items/', GetAllEmployeeItems.as_view()),
    path('create-employee-items/', CreateAllEmployeeItems.as_view()),
    path('update-employee-items/<int:pk>/', UpdateAllEmployeeItems.as_view()),
    path('delete-employee-items/<int:pk>/', DeleteAllEmployeeItems.as_view()),


    # >>>>>>>>>> CRUD Payment Model <<<<<<<<<< #
    path('get-payment-items/', GetAllPaymentItems.as_view()),
    path('create-payment-items/', CreateAllPaymentItems.as_view()),
    path('update-payment-items/<int:pk>/', UpdateAllPaymentItems.as_view()),
    path('delete-payment-items/<int:pk>/', DeleteAllPaymentItems.as_view()),


    # >>>>>>>>>> CRUD Cassa Model <<<<<<<<<< #
    path('get-cassa-items/', GetAllCassaItems.as_view()),
    path('create-cassa-items/', CreateAllCassaItems.as_view()),
    path('update-cassa-items/<int:pk>/', UpdateAllCassaItems.as_view()),
    path('delete-cassa-items/<int:pk>/', DeleteAllCassaItems.as_view()),


    # >>>>>>>>>> CRUD Garaj Model <<<<<<<<<< #
    path('get-garaj-items/', GetAllGarajItems.as_view()),
    path('create-garaj-items/', CreateAllGarajItems.as_view()),
    path('update-garaj-items/<int:pk>/', UpdateAllGarajItems.as_view()),
    path('delete-garaj-items/<int:pk>/', DeleteAllGarajItems.as_view()),


    # >>>>>>>>>> CRUD Report Model <<<<<<<<<< #
    path('get-report-items/', GetAllReportItems.as_view()),
    path('create-report-items/', CreateAllReportItems.as_view()),
    path('update-report-items/<int:pk>/', UpdateAllReportItems.as_view()),
    path('delete-report-items/<int:pk>/', DeleteAllReportItems.as_view()),


    # >>>>>>>>>> CRUD Profession Model <<<<<<<<<< #
    path('get-profession-items/', GetAllProfessionItems.as_view()),
    path('create-profession-items/', CreateAllProfessionItems.as_view()),
    path('update-profession-items/<int:pk>/', UpdateAllProfessionItems.as_view()),
    path('delete-profession-items/<int:pk>/', DeleteAllProfessionItems.as_view()),


    # >>>>>>>>>> CRUD Comment Model <<<<<<<<<< #
    path('get-comment-items/', GetAllCommentItems.as_view()),
    path('create-comment-items/', CreateAllCommentItems.as_view()),
    path('update-comment-items/<int:pk>/', UpdateAllCommentItems.as_view()),
    path('delete-comment-items/<int:pk>/', DeleteAllCommentItems.as_view()),
]