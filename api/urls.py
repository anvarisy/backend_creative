from django.urls import include, path
from api.views import ApiStyle

urlpatterns = [
    # path('', include(router.urls)),
    # path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('category/',ApiStyle.as_view()),
]