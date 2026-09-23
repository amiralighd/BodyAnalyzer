from django import forms
from .models import BodyAnalysis


class BodyAnalysisForm(forms.ModelForm):

    class Meta:
        model = BodyAnalysis

        fields = (
            'weight',
            'height',
            'age',
            'gender',
            'blood_sugar',
            'cholesterol',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['blood_sugar'].help_text = (
            'Normal: below 100 mg/dL | '
            'Prediabetes: 100 - 125 mg/dL | '
            'Diabetes: 126+ mg/dL'
        )

        self.fields['cholesterol'].help_text = (
            'Normal: below 200 mg/dL | '
            'Warning: 200+ mg/dL'
        )

    def clean_weight(self):
        weight = self.cleaned_data['weight']

        if weight <= 0:
            raise forms.ValidationError(
                'Weight must be greater than 0.'
            )

        if weight > 300:
            raise forms.ValidationError(
                'Please enter a realistic weight.'
            )

        return weight

    def clean_height(self):
        height = self.cleaned_data['height']

        if height <= 0:
            raise forms.ValidationError(
                'Height must be greater than 0.'
            )

        if height > 250:
            raise forms.ValidationError(
                'Please enter a realistic height.'
            )

        return height

    def clean_age(self):
        age = self.cleaned_data['age']

        if age <= 0:
            raise forms.ValidationError(
                'Age must be greater than 0.'
            )

        if age > 120:
            raise forms.ValidationError(
                'Please enter a realistic age.'
            )

        return age

    def clean_blood_sugar(self):
        blood_sugar = self.cleaned_data['blood_sugar']

        if blood_sugar < 0:
            raise forms.ValidationError(
                'Blood sugar cannot be negative.'
            )

        return blood_sugar

    def clean_cholesterol(self):
        cholesterol = self.cleaned_data['cholesterol']

        if cholesterol < 0:
            raise forms.ValidationError(
                'Cholesterol cannot be negative.'
            )

        return cholesterol