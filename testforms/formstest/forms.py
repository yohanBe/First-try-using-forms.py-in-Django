from django.forms import ModelForm
from . import models


class blogpostcreateview(ModelForm):
    class Meta:
        model = models.blogposts
        fields = ('name', 'post')
