from rest_framework import serializers

from ad.models import Poster


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = [
            'id',
            'name',
            'description',
            'link',
            'wallpaper',
            'created_at',
        ]
