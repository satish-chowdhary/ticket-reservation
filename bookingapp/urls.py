from django.urls import path, include
from .views import PassengerView,CoachesView,PortionsView

urlpatterns = [
    path('book/', PassengerView.as_view(), name = 'book_ticket'),
    path('coach/', CoachesView.as_view(), name = 'select_coach'),
    path('seat/', PortionsView.as_view(), name = 'select_seat'),
]