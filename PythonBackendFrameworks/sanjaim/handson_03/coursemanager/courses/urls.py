from django.urls import include, path
from rest_framework.routers import DefaultRouter

# from .views import CourseListView,CourseDetailView
from .views import CourseViewset

route = DefaultRouter()
route.register(r"", CourseViewset)
urlpatterns = [
    # path('',CourseListView.as_view(),name='course_list'),
    # path('<int:pk>/',CourseDetailView.as_view(),name='course_detail')
    #
    path("", include(route.urls))
]
