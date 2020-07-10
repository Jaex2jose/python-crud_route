from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('login', views.login),
    path('success', views.success),
    path('logout', views.logout),
    path('quotes', views.dashboard),
    path('createq', views.quotes),
    path('users/<int:id>', views.quote_info),
    path('delete/<int:quote_id>', views.delete),
    path('edit/<int:quote_id>', views.edit),
    path('edit_quote/<int:id>', views.edit_quote)
]



