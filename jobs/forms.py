from django import forms
from .models import JobApplicant


class JobApplicantForm(forms.ModelForm):
    class Meta:
        model = JobApplicant
        fields = ['resume']
        widgets = {
            'resume': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': '.pdf,.doc,.docx',
                'style': 'border-radius: 0.5rem;'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['resume'].help_text = 'Upload your resume (PDF, DOC, DOCX only)'