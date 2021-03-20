from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader

# Create your views here.

def top(request):
 #   template = loader.get_template('base_app/top.html')
    ctx = {'title': 'Django学習チャンネル（仮）'}
 #   return HttpResponse(template.render(ctx, request))
    return render(request, 'base_app/top.html', ctx)