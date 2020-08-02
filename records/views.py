
from rest_framework import viewsets

from .models import Members, Pledge, Attendance, Campaign
from .serializers import MembersSerializer, PledgeSerializer, AttendanceSerializer, CampaignSerializer


class MembersViewset(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

class PledgeViewset(viewsets.ModelViewSet):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer

class AttendanceViewset(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class CampaignViewset(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer