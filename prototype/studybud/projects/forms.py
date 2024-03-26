from django.forms import ModelForm
from .models import Project
from django import forms

#model that cretates a form with inputing all the attributes of Project
class ProjectForm(ModelForm):
    class Meta:
        model = Project # model that the form is based on
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags' ] # exact field names
        widgets = { 'tags': forms.CheckboxSelectMultiple(),
                   }
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        


        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


        '''self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Title'})
        self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Description'})'''