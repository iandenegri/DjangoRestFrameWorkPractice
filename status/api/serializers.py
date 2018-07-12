from rest_framework import serializers

from status.models import Status

# Converts data to json data and does validations on data
class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]
    # def validate_content(self,value):
    #     if len(value) > 240:
    #         raise serializers.ValidationError('This is too long of a status')
    #     return value

    def validate_all(self, data):
        content = data.get('content', None)
        if content == '':
            content = None
        image = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Content or image is required.')
        return data
