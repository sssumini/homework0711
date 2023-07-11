from rest_framework import serializers
from .models import *

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fiedls = '__all__' 

class AlbumSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    created_at = serializers.CharField(read_only=True)
    updated_at = serializers.CharField(read_only=True)

    tracks = serializers.SerializerMethodField(read_only=True)

    def get_tracks(self, instance):
        serializer = TrackSerializer(instance.tracks, many=True)
        return serializer.data
        
    tag = serializers.SerializerMethodField()
    def get_tag(self,instance):
        tags = instance.tag.all()
        return [tag.name for tag in tags]

    class Meta:
        model = Album
        fields = ['id', 'artist', 'title', 'year', 'description', 'created_at', 'updated_at', 'tracks', 'tag']


class TrackSerializer(serializers.ModelSerializer):

    album = serializers.SerializerMethodField()

    def get_album(self, instance):
        return instance.album.title

    class Meta:
        model = Track
        fields = '__all__'
        read_only_fields = ['album']