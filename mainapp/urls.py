from unicodedata import name
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('booking', views.booking, name='booking'),
    path('rooms_info', views.rooms_info, name='rooms_info'),
    path('edit_room/<str:room_no>', views.edit_room, name='edit_room'),
    path('remove_room/<str:room_no>', views.remove_room, name='remove_room'),
    path('book_room/<str:room_no>', views.book_room, name='book_room'),
    path('payment/<str:room_no>', views.payment, name='payment'),
    path('restro', views.restro, name='restro'),
]