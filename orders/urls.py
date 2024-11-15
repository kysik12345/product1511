from django.urls import path
from .views import new_order


urlpatterns = [
    path('new/', new_order, name="new_order"),
    # path('detail/', update_cart_by_front, name="update_cart_session"),
    # path('user/<int:pk>/', update_cart_by_front, name="update_cart_session"),

]