from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:id>/', views.detail, name='article_detail'),
	path('<int:id>/leave_comment/', views.leave_comment, name='leave_comment')
]