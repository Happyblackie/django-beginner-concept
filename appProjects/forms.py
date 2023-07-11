from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['vote_total', 'vote_ratio']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(args, kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input'})
        
        for key, value in self.fields.items():
            value.widget.attrs.update({'class':'input'})

