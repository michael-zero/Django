from django.urls import path 

urlpatterns = [
    path('endereço', MinhaView.as_view(), name='name-da-url')
]
