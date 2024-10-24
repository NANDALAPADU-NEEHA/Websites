from django.urls import path
from page import views

urlpatterns=[
    path('home',views.home,name='homepage'),
    path('about',views.about,name='aboutpage'),
    path('contact',views.contact,name='contactpage'),
    path('help',views.help,name='helppage'),
    path('ispalin/<str:sname>',views.func1,name='palindromepage'),
    path('isnum/<int:name1>',views.func2,name='evenoddpage'),
]

