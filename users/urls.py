from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_specialities, name='add-specialities'),

    # ********************************* ADDRESSES BEGIN ****************************************
    path("specialities/", views.Speciality.as_view()),
    path("speciality/", views.AddressCreate.as_view()),
    path("speciality/<str:pk>", views.AddressDetail.as_view()),
    # ********************************* ADDRESSES END *******************************************

    # ********************************* ADDRESSES BEGIN ****************************************
    path("addresses/", views.AddressList.as_view()),
    path("address/", views.AddressCreate.as_view()),
    path("address/<str:pk>", views.AddressDetail.as_view()),
    # ********************************* ADDRESSES END *******************************************

    # ********************************* LANGUAGE BEGIN *****************************************
    path("languages/", views.LanguageList.as_view()),
    path("language/", views.LanguageCreate.as_view()),
    path("language/<str:pk>", views.LanguageDetail.as_view()),
    # ********************************* LANGUAGE END *******************************************

]