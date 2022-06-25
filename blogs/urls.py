from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new', views.CreateView.as_view(), name='create'),
    path('filter', views.FilterView.as_view(), name='Filter'),
    path('order', views.OrderView.as_view(), name='Order'),
    path('filterorder', views.FilterOrderView.as_view(), name='FOrder'),
    path('post/<int:pk>/', views.ViewPostView, name='view'),
    path('post/<int:pk>/update', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
]
