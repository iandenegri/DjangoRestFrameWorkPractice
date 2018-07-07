import json
from django.db import models
from django.conf import settings
from django.core.serializers import serialize


def upload_update_image(instance, filename):
    return"updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):
    # def serialize_set(self):
    #     queryset = self
    #     return serialize('json', queryset, fields=('user', 'content', 'image'))

    def serialize_set(self):
        queryset = list(self.values('user', 'content', 'image', 'id'))

#  Code below is the long way of doing what the values method does.

        # final_array = []
        # for object in queryset:
        #     final_array.append(object.serialize_single())
        return json.dumps(queryset)


class UpdateManager(models.Manager):
    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated     = models.DateTimeField(auto_now_add=True)
    timestamp   = models.DateTimeField(auto_now_add=True)


    objects = UpdateManager()

    def __str__(self):
        return self.content or ''

    def serialize_single(self):
        # json_data = serialize('json', [self], fields=('user', 'content', 'image'))
        # struct = json.loads(json_data) # Looks like: [{}]
        # data = json.dumps(struct[0]['fields'])

        try:
            image = self.image.url
        except:
            image = ''
        data = {
            'id': self.id,
            'content': self.content,
            'user': self.user.id,
            'image': image
        }
        data = json.dumps(data)
        return data
