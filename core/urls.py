from django.urls import path
from core import views as core_views

urlpatterns = [

    # -------------------------USER--------------------#

    path('Users/RegisterUser/', core_views.RegisterUser.as_view()),
    path('Users/GetUser/<int:pk>', core_views.GetUser.as_view()),
    path('Users/EditUser/<int:pk>', core_views.EditUser.as_view()),
    path('Users/UpdatePictures/<int:pk>', core_views.UpdatePictures.as_view()),
    path('Users/UpdatePassword/<int:pk>', core_views.UpdatePassword.as_view()),
]
