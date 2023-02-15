from django.urls import path
from septicserviceapp.views import SepticInfoView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('septicinfo/<str:address>/<str:zip_code>/', SepticInfoView.as_view(), name='getSepticInfoByAddress'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]