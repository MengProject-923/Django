from django.urls import path
from .views import *

urlpatterns = [
    path('users/', users_list, name='users_list'),
    path('users/<int:user_id>/', user_detail, name='user_detail'),
    path('serverhosts/', serverhosts_list, name='serverhosts_list'),
    path('serverhosts/<int:serverhost_id>/', serverhost_detail, name='serverhost_detail'),
    path('fixedassets/', fixedassets_list, name='fixedassets_list'),
    path('fixedassets/<int:fixed_asset_id>/', fixedassets_detail, name='fixedassets_detail'),
]
