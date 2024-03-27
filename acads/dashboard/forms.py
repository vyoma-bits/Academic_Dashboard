from django import forms
from django.forms import ModelForm
from .models import courses,tut2,grading,marks,content1,try1,profs,Department


class courseForm(ModelForm):
    class Meta:
        model=courses
        fields="__all__"

class tutForm(ModelForm):
    course = forms.ModelChoiceField(queryset=courses.objects.all(), to_field_name='course_name')
    class Meta:
        model=tut2
        fields="__all__"
    def __init__(self, *args, **kwargs):
        courses1 = kwargs.pop('courses', None)
        teachers=kwargs.pop('teac', None)
        dep=kwargs.pop('dep', None)
        name1=kwargs.pop('name', None)
        super().__init__(*args, **kwargs)
        if courses1 is not None:
            self.fields['course'].queryset =courses.objects.filter(pk__in=courses1)
        if name1 is not None:
            self.fields['name'].choices=name1
        if teachers is not None:
            self.fields['teacher'].queryset =profs.objects.filter(pk__in=teachers)
        if dep is not None:
            self.fields['department'].queryset =Department.objects.filter(pk__in=dep)


        # Get the username instance (assuming it's pre-populated)

class gradingForm(ModelForm):
    class Meta:
        model=grading
        fields="__all__"
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Get the username instance (assuming it's pre-populated)
        if 'initial' in kwargs and 'course' in kwargs['initial']:
            username_instance = kwargs['initial']['course']
        else:
            # Handle the case where initial value is not provided
            username_instance = None  # Or set a default username instance

        # Make the username field read-only
        self.fields['course'].widget = forms.widgets.Select(choices=[(username_instance.pk, str(username_instance))])
        self.fields['course'].disabled = True  # Disable the field for selection

    # Disable the field for selection
class marksForm(ModelForm):
    class Meta:
        model=marks
        
        fields="__all__"
    
    def __init__(self, *args, **kwargs):
        course1=kwargs.pop('courses', None)
        super().__init__(*args, **kwargs)
        if course1 is not None:
            self.fields['course'].queryset =courses.objects.filter(pk__in=course1)
     

        # Get the username instance (assuming it's pre-populated)
        if 'initial' in kwargs and 'user' in kwargs['initial']:
            username_instance = kwargs['initial']['user']
        else:
            # Handle the case where initial value is not provided
            username_instance = None  # Or set a default username instance

        # Make the username field read-only
        self.fields['user'].widget = forms.widgets.Select(choices=[(username_instance.pk, str(username_instance))])
        self.fields['user'].disabled = True  # Disable the field for selection

class contentForm(ModelForm):
    class Meta:
        model=content1
        fields="__all__"
    def __init__(self, *args, **kwargs):
        
        courses1 = kwargs.pop('courses', None)
        super().__init__(*args, **kwargs)
        if courses1 is not None:
            self.fields['course'].queryset =courses.objects.filter(pk__in=courses1)


        # Get the username instance (assuming it's pre-populated)
        if 'initial' in kwargs and 'user' in kwargs['initial']:
            username_instance = kwargs['initial']['user']
        else:
            # Handle the case where initial value is not provided
            username_instance = None  # Or set a default username instance

        # Make the username field read-only
        self.fields['user'].widget = forms.widgets.Select(choices=[(username_instance.pk, str(username_instance))])
        self.fields['user'].disabled = True  # Disable the field for selection

class try1Form(ModelForm):
    class Meta:
        model=try1
        fields="__all__"
    def __init__(self, *args, **kwargs):
        
        courses1 = kwargs.pop('courses', None)
        super().__init__(*args, **kwargs)
        if courses1 is not None:
            self.fields['course'].queryset =courses.objects.filter(pk__in=courses1)
      