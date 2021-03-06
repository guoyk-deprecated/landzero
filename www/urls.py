from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('signed_in', views.signed_in, name='signed_in'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('p/<slug:slug>/', views.view_post, name='view_post')
]
