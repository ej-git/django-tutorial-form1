from django.views import generic
from django.shortcuts import render
from app import  forms


class Pattern1_1(generic.FormView):
    """/ """
    template_name = 'app/pattern1_1.html'
    form_class = forms.Form1_1

class Pattern1_2(generic.FormView):
    """/pattern1_2 """
    template_name = 'app/pattern1_2.html'
    form_class = forms.Form1_1

    def form_valid(self, form):
        """countryの値をセッションに保存"""
        self.request.session['country'] = form.cleaned_data['country']
        # 新しいフォームを生成
        new_form = forms.Form1_2()
        return self.render_to_response(self.get_context_data(form=new_form))

class Pattern1_3(generic.FormView):
    """/pattern1_2 """
    template_name = 'app/pattern1_3.html'
    form_class = forms.Form1_2

    def form_valid(self, form):
        """countryとareaの値によって、フォームのchoicesを変える"""
        request_data = self.request.session.get('country', "")
        if request_data:
            country = request_data
            self.request.session.pop("country", "")
        area = form.cleaned_data['area']
        if country == '1':
            if area == '1':
                choices = forms.CITY_CHOICES1_w
            elif area == '2':
                choices = forms.CITY_CHOICES1_e
        elif country == '2':
            if area == '1':
                choices = forms.CITY_CHOICES2_w
            elif area == '2':
                choices = forms.CITY_CHOICES2_e
        elif country == '3':
            if area == '1':
                choices = forms.CITY_CHOICES3_w
            elif area == '2':
                choices = forms.CITY_CHOICES3_e

        # 新しいフォームを生成
        new_form = forms.Form1_3()
        new_form.fields['city'].choices = choices
        return self.render_to_response(self.get_context_data(form=new_form))


class Pattern2(generic.FormView):
    """/pattern2 1ページ内で選択肢を切り替える"""
    template_name = 'app/pattern2.html'
    form_class = forms.Form2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['CITY_CHOICES1_w'] = forms.CITY_CHOICES1_w
        context['CITY_CHOICES1_e'] = forms.CITY_CHOICES1_e
        context['CITY_CHOICES2_w'] = forms.CITY_CHOICES2_w
        context['CITY_CHOICES2_e'] = forms.CITY_CHOICES2_e
        context['CITY_CHOICES3_w'] = forms.CITY_CHOICES3_w
        context['CITY_CHOICES3_e'] = forms.CITY_CHOICES3_e
        return context