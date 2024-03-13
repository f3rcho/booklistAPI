from . import views
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('libros', views.books, name='books'),
    # Routing to a class method
    path('orders', views.Orders.listOrders),
    # Routing class-based views
    # path('books/<int:pk>', views.BookView.as_view()),
    # Routing classes that extend viewsets
    path('books', views.BookView.as_view(
        {
            'get': 'list',
            'post': 'create',
        })
    ),
    path('books/<int:pk>', views.BookView.as_view(
        {
            'get': 'retrieve',
            'put': 'update',
            'path': 'partial_update',
            'delete': 'destroy'
        }
    )),
    # debug
    path('__debug__', include('debug_toolbar.urls')),
    path('secret', views.secret),
    path('api-token-auth/', obtain_auth_token),
    path('manager-view/', views.manager_view),
    path('throttle-check', views.throttles_check),
    path('throttle-check-auth', views.throttle_check_auth),
    path('throttle-check-auth-10', views.throttle_check_auth_in_ten),
    path('groups/manager/users', views.managers),
]
