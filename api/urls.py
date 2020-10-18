from django.urls import include, path
from api.views import ApiCarousel, ApiCheckOut, ApiLogin, ApiLogout, ApiMenu, ApiOrder, ApiPay, ApiRegister

urlpatterns = [
    # path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/',ApiMenu.as_view()),
    path('register/',ApiRegister.as_view()),
    path('login/',ApiLogin.as_view()),
    path('logout/',ApiLogout.as_view()),
    path('order/<str:email>',ApiOrder.as_view()),
    path('checkout/',ApiCheckOut.as_view()),
    path('pay/',ApiPay.as_view()),
    path('carousel/',ApiCarousel.as_view()),
]