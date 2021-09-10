from django.urls import path
from .views import add_two_numbers,add_two_numbers_in_rest, info_view
from .class_views import InfoClassBasedViews
from .generic_views import InfoModelCreateAPIView, InfoModelListAPIView,InfoModelDestroyAPIView,InfoModelUpdateAPIView,InfoModelRetrieveAPIView
urlpatterns = [
    path('add/', add_two_numbers),
    path('v2/add/', add_two_numbers_in_rest),

    #rest/info/class-based/
    path('info/class-based',InfoClassBasedViews.as_view()),
    path('info/',info_view),
    path('info/<int:pk>/',info_view),

    path('info/generic/create/',InfoModelCreateAPIView.as_view()),
    path('info/generic/list/',InfoModelListAPIView.as_view()),
    path('info/generic/delete/<int:pk>/',InfoModelDestroyAPIView.as_view()),
    path('info/generic/update/<int:pk>/',InfoModelUpdateAPIView.as_view()),
    path('info/generic/detail/<int:pk>/',InfoModelRetrieveAPIView.as_view()),






    
]
