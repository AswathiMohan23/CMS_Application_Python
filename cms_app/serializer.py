from rest_framework import serializers

from cms_app.models import BlogModel


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = ["title", "description", "content", "created_date", "user"]

    def create(self, validate_data):
        print(validate_data)
        return BlogModel.objects.get_or_create(title=validate_data.get('title'),
                                               description=validate_data.get('description'),
                                               content=validate_data.get('content'),
                                               created_date=validate_data.get('created_date'),
                                               user=validate_data.get('user'))
