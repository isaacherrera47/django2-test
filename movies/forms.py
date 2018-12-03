from django.forms import ModelForm, Textarea, DateInput

from movies.models import Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        exclude = ['user']
        widgets = {
            'summary': Textarea(),
            'review': Textarea(),
            'release_date': DateInput()
        }
