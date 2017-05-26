from django.views import generic
from django.shortcuts import render
from .forms import Form1_1, Form1_2, CITY_CHOICES1, CITY_CHOICES2, CITY_CHOICES3


class Pattern1_1(generic.FormView):
    """/ """
    template_name = 'app/pattern1_1.html'
    form_class = Form1_1


class Pattern1_2(generic.FormView):
    """/pattern1_2 """
    template_name = 'app/pattern1_2.html'
    form_class = Form1_1

    def form_valid(self, form):
        """countryの値によって、フォームのchoicesを変える"""
        country = form.cleaned_data['country']
        if country == '1':
            choices = CITY_CHOICES1
        elif country == '2':
            choices = CITY_CHOICES2
        elif country == '3':
            choices = CITY_CHOICES3
        # 新しいフォームを生成
        new_form = Form1_2()
        new_form.fields['city'].choices = choices
        return self.render_to_response(self.get_context_data(form=new_form))