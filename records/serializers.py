from rest_framework import serializers

from .models import Members, Pledge, Attendance, Campaign


class MembersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Members
        fields = '__all__'


class PledgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pledge
        fields = '__all__'


class AttendanceSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source='member', read_only=True)
    visitor = serializers.BooleanField(source='member.visitor', read_only=True)

    class Meta:
        model = Attendance
        fields = '__all__'


class CampaignSerializer(serializers.ModelSerializer):

    class Meta:
        model = Campaign
        fields = '__all__'
