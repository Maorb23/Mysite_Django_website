# Maor_proj/cv/forms.py

from django import forms
from .models import CV

class CVUploadForm(forms.ModelForm):
    class Meta:
        model = CV
        fields = ['cv_file']

    def clean_cv_file(self):
        cv_file = self.cleaned_data.get('cv_file', False)
        if cv_file:
            # Validate file type
            if cv_file.content_type not in [
                'application/pdf', 
                'application/msword', 
                'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            ]:
                raise forms.ValidationError("Unsupported file type. Please upload a PDF or DOC/DOCX file.")
            # Validate file size (max 4MB)
            if cv_file.size > 4 * 1024 * 1024:
                raise forms.ValidationError("File too large. Size should not exceed 4 MB.")
            return cv_file
        else:
            raise forms.ValidationError("Couldn't read uploaded file.")
