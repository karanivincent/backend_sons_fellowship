from rest_framework import routers
from . import views
from django.urls import include, path


router = routers.DefaultRouter()
router.register(r'members', views.MembersViewset)
router.register(r'pledges', views.PledgeViewset)
router.register(r'attendance', views.AttendanceViewset)
router.register(r'campaigns', views.CampaignViewset)

urlpatterns = [
    path('', include(router.urls)),

]