﻿# -*- coding: utf-8 -*-

from django.http import HttpResponse

def first_page(request):
    return HttpResponse("<p>Western-style 中国food</p>")