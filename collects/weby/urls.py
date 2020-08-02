from django.urls import path
from . import views


urlpatterns=[

    path('aboutus', views.aboutus, name="aboutus"),
    path('', views.show_home_page, name="show_home_page"),
    path('category/<int:cid>', views.show_category_page, name="show_category_page"),
]
