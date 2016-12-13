# _*_coding: utf-8_*_

from django.http import HttpResponse

def first_page(request):
	return HttpResponse("<p>Hello 中国world!</p>")