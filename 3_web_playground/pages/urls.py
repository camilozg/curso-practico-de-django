from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.PageListView.as_view(), name='pages'),
    path('<int:pk>/<slug:slug>/', views.PageDetailView.as_view(), name='detail'),
    path('create/', views.PageCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.PageUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.PageDeleteView.as_view(), name='delete')
]
