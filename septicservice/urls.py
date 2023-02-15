from django.urls import path
from septicserviceapp.views import getSepticInfoByAddress

urlpatterns = [
    path('septic-info/<str:address>/<str:zip_code>/', getSepticInfoByAddress, name='septic-info'),
]


