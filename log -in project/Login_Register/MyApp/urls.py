from django.urls import path
from . import views


urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('register/',views.register.as_view(),name='register'),
    path('dashboard/',views.dashboard.as_view(),name='dashboard'),
    path('signout/',views.signout.as_view(),name='signout'),
    path('blogs/',views.blogs.as_view(),name='blogs'),
    path('add_blog/',views.add_blog.as_view(),name='add_blog'),
    path('delete_blog/<int:pk>',views.delete_blog.as_view(),name='delete_blog'),
    path('edit_blog/<int:pk>',views.edit_blog.as_view(),name='edit_blog'),

]