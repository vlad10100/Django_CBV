from django.urls import path 
from dj_auth.api.views import Routes, MyTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView



urlpatterns = [
    path('', Routes.as_view(), name='get-routes'),

    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
