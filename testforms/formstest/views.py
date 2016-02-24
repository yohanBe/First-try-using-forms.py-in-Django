from django.shortcuts import render
from . import forms
from . import models
from django.views import generic

class blogpostcreateviews(generic.FormView):
    template_name = 'blogpost.html'
    form_class = forms.blogpostcreateview

    def forms_valid(self, form):
        form.save()
        return super(blogpostcreateview, self).forms_valid(forms)

    def get_context_data(self, **kwargs):
        ctx = super(blogpostcreateviews, self).get_context_data(**kwargs)
        ctx.update({'my_post': models.blogposts.objects.all()})
        return ctx

    def get_success(self):
        return '/admin/'
# Create your views here.
