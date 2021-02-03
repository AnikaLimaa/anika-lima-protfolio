from django.urls import path,include
from . import views
app_name='blog'

urlpatterns=[

    path('',views.blog_all,name='blog_all'),

    path('<int:blog_no>/', views.detail, name='detail')

]