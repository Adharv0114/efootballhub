from django import forms
from .models import Player

class PlayerForm(forms.ModelForm):
    skills = forms.CharField(widget=forms.Textarea, help_text="Enter up to 10 skills, separated by commas.")

    class Meta:
        model = Player
        fields = '__all__' # Include all fields from the model

    def clean_skills(self):
        skills_list = [skill.strip() for skill in self.cleaned_data['skills'].split(',')]
        if len(skills_list) > 10:
            raise forms.ValidationError("You can add up to 10 skills only.")
        return skills_list