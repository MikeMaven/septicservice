from django.urls import path
from septicserviceapp.views import SepticInfoView

urlpatterns = [
    path('septic-info/<str:address>/<str:zip_code>/', SepticInfoView.as_view(), name='getSepticInfoByAddress'),
]