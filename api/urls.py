from django.urls import include, path
from api.views import ApiCarousel, ApiCheckOut, ApiLogin, ApiLogout, ApiMenu, ApiOrder, ApiPay, ApiRegister,\
    ApiGallery

urlpatterns = [
    # path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('menu/',ApiMenu.as_view(), name='a-menu'),
    path('register/',ApiRegister.as_view(), name='a-register'),
    path('login/',ApiLogin.as_view(),name='a-login'),
    path('logout/',ApiLogout.as_view(),name='a-logout'),
    path('order/<str:email>/',ApiOrder.as_view(),name='a-order'),
    path('checkout/',ApiCheckOut.as_view(),name='a-checkout'),
    path('pay/',ApiPay.as_view(),name='a-pay'),
    path('carousel/',ApiCarousel.as_view(),name='a-carousel'),
    path('gallery/', ApiGallery.as_view(),name='a-gallery')
]