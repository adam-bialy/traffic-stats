from django.urls import path

from .views import SiteVisitGroupView
from .views import SiteVisitListCreateView

urlpatterns = [
    path("visits/", SiteVisitListCreateView.as_view(), name="sitevisit-list"),
    path("visits_group/", SiteVisitGroupView.as_view(), name="sitevisit-group"),
]
