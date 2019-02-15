from django.shortcuts import render
from django.views import View


class FormView(View):

    def get(self, request):
        return render(request, 'forms/form.html', {})

    def post(self, request):
        text = request.POST.get('text')
        grade = request.POST.get('grade')
        image = request.FILES.get('image')
        content = image.read()
        context = {
            'text': text,
            'grade': grade,
            'content': content
        }
        return render(request, 'forms/form.html', context)
