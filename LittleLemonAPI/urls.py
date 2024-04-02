from django.urls import path
from . import views

urlpatterns = [
    path('categories', views.CategoryView.as_view(), name='categories'),
    path('categories/<int:pk>', views.SingleCategoryView.as_view(), name='single-category'),
    path('menu-items', views.MenuItemView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    
    #Manager groups
    path('groups/manager/users', views.ManagerView.as_view(), name='manager-users'),
    path('groups/manager/users/<int:pk>', views.SingleManagerView.as_view(), name='single-manager'),
]