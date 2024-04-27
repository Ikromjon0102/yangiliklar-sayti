from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
from .models import News, Category


def news_list_view(request):
    news_list_slide = News.published.all()
    latest_news_5 = News.published.all()[:5]
    iqtisodiy_news_one = News.published.filter(category__nomi='Iqtisodiy')[0]
    iqtisodiy_news_4 = News.published.filter(category__nomi='Iqtisodiy')[1:5]
    local_news = News.published.filter(category__nomi='Mahalliy')[:5]



    context = {
        'news_list': news_list_slide,
        'latest_news_5': latest_news_5,
        'iqtisodiy_news_one':iqtisodiy_news_one,
        'iqtisodiy_news_4':iqtisodiy_news_4,
        'local_news':local_news
    }




    return render(request, template_name='index.html', context=context)


def news_detail_view(request, slug):

    news_detail = News.objects.get(slug = slug)
    news_detail.views = news_detail.views + 1

    yaqin_news = News.objects.filter(category__nomi=news_detail.category)[:3]

    context = {
        'news_detail': news_detail,
        'yaqin_news': yaqin_news
    }

    return render(request, template_name='single_page.html', context=context)

def texno_news_view(request):

    news_list = News.published.filter(category__nomi='Texnologiya')

    context = {
        'news_list' : news_list
    }

    return render(request, template_name='texno.html', context=context)

def contact_view(request):
    form = ContactForm(request.POST)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return HttpResponse("Xabaringiz yuborildi")
    context = {
        'form' : form
    }

    return render(request, template_name='contact.html', context=context)
