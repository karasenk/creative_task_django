from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):

    template_name = "info/home.html"

    def get(self, request, *args, **kwargs):
        context = {'city': 'Казань',
                   'fio': 'Тарасенко Надежда Александровна',
                   'hobbies': ["рисование (в основном диджитал)",
                               "аниме и книги (обычно фэнтези)",
                               "программирование"],
                   'experience': 'проекты (один индивидуальный и два групповых) '
                                 'на втором курсе Лицея Академии Яндекса\n'
                                 '(в том числе сайт на Flask)'
                   }
        return render(request, "info/home.html", context=context)
