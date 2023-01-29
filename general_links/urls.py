from django.urls import path
from .views import ProductCreateView, ProductView, \
    LinkCreateView, LinkListView, LinkView

urlpatterns = [
    path("product/create/", ProductCreateView.as_view(), name="create_prod"),
    path("product/<pk>/", ProductView.as_view(), name="prod"),

    path("link/create/", LinkCreateView.as_view(), name="create_lnk"),
    path("link/list/", LinkListView.as_view(), name="link_lnk"),
    path("link/<pk>/", LinkView.as_view(), name="lnk"),

]
