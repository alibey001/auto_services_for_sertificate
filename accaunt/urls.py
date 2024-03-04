from django.urls import path
from .views import *


urlpatterns = [
    # >>>>>>>>>> CRUD User Model <<<<<<<<<< #
    path('sing-up-user/', sang_up_view),
    path('login-user/', login_view),
    path('logout-user/', logout_view),
    path('edit-user/<int:pk>/', edit_user_view),
    path('delete-user/<int:pk>', delete_user),
]