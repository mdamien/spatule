from django.shortcuts import get_object_or_404, render
from pages.models import Page,HomePage,SliderImage,Article

def index(request):
	pages = Page.objects.all()
	homepage = HomePage.objects.all()[:1].get()
	return render(request, 'pages/index.html', {'page': homepage,'pages':pages})

def page(request,url):
	pages = Page.objects.all()
	page = get_object_or_404(Page, url=url)
	articles = Article.objects.order_by('position').filter(page=page)
	return render(request, 'pages/page.html', {'page': page,'pages':pages,'articles':articles})