from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('show', views.show, name='show'),
    path('update/edit/<id>', views.edit, name='edit'),
    path('delete/<id>', views.delete, name='del'),
    path('update/<id>', views.update, name='upd'),

]
