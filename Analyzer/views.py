from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import BodyAnalysisForm


class AnalysisView(LoginRequiredMixin, View):

    def get(self, request):
        form = BodyAnalysisForm()

        return render(
            request,
            'analyzer/analysis.html',
            {'form': form}
        )

    def post(self, request):
        form = BodyAnalysisForm(request.POST)

        if form.is_valid():

            analysis = form.save(commit=False)

            analysis.user = request.user

            height = analysis.height / 100

            bmi = analysis.weight / (height ** 2)

            if bmi < 18.5:
                bmi_status = 'Underweight'

            elif bmi < 25:
                bmi_status = 'Normal'

            elif bmi < 30:
                bmi_status = 'Overweight'

            else:
                bmi_status = 'Obesity'

            analysis.bmi = round(bmi, 2)
            analysis.bmi_status = bmi_status

            if analysis.blood_sugar < 100:
                blood_sugar_status = 'Normal'

            elif analysis.blood_sugar < 126:
                blood_sugar_status = 'Prediabetes'

            else:
                blood_sugar_status = 'Diabetes'

            analysis.blood_sugar_status = blood_sugar_status

            if analysis.cholesterol < 200:
                cholesterol_status = 'Normal'

            else:
                cholesterol_status = 'Warning'

            analysis.cholesterol_status = cholesterol_status

            analysis.save()

            result = {
                'bmi': analysis.bmi,
                'bmi_status': analysis.bmi_status,
                'blood_sugar_status': analysis.blood_sugar_status,
                'cholesterol_status': analysis.cholesterol_status,
            }

            return render(
                request,
                'analyzer/result.html',
                {'result': result}
            )

        return render(
            request,
            'analyzer/analysis.html',
            {'form': form}
        )