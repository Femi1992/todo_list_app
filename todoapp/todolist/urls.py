from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="TodoList"),
    url(r'addCategory/$', views.CreateCategoryView.as_view(),name='createCategory'),
]