from django.urls import include, path

urlpatterns = [
    path("", include("blog.urls")),
    path("pages/", include("pages.urls")),
]
