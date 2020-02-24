from rest_framework import serializers
from dual_rocks.user_profile.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            'id',
            'user',
            'at',
            'name',
            'pronoun',
            'year_of_birth',
            'month_of_birth',
            'picture_url',
            'status',
            'bio',
        ]

    picture_url = serializers.SerializerMethodField()

    def get_picture_url(self, instance):
        request = self.context.get('request')
        if request:
            return instance.get_picture_url(user=request.user)
        return instance.picture_url
