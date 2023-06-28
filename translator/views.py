from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from . import morse

@csrf_exempt
def home(request):
    return render(request, 'translator/home.html')

@csrf_exempt
def translate_morse(request):
    if request.method == 'POST':
        text = request.POST.get('text', '')
        translated_text = morse.translate(text)
        return render(request, 'translator/translate.html', {'translated_text': translated_text})
    return render(request, 'translator/translate.html')
