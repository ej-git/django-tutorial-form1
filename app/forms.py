from django import forms

COUNTRY_CHOICES = (
    (1, '日本'),
    (2, 'アメリカ'),
    (3, 'イギリス'),
)

AREA_CHOICES = (
    (1, '西'),
    (2, '東'),
)

CITY_CHOICES1_w = (
    (1, '京都'),
    (2, '大阪'),
    (3, '沖縄'),
)
CITY_CHOICES1_e = (
    (1, '東京'),
    (2, '群馬'),
    (3, '横浜'),
    (4, '千葉'),
)

CITY_CHOICES2_w = (
    (1, 'ワシントン'),
    (2, 'オレゴン'),
)
CITY_CHOICES2_e = (
    (1, 'マサチューセッツ'),
    (2, 'ロサンゼルス'),
)

CITY_CHOICES3_w = (
    (1, 'マンチェスター'),
)
CITY_CHOICES3_e = (
    (1, 'ロンドン'),
)

class Form1_1(forms.Form):
    country = forms.ChoiceField(
        label='国',
        choices=COUNTRY_CHOICES,
    )

class Form1_2(forms.Form):
    area = forms.ChoiceField(
        label='エリア',
        choices=AREA_CHOICES,
    )

class Form1_3(forms.Form):
    city = forms.MultipleChoiceField(
        label='市',
        choices=CITY_CHOICES1_w,
    )


class Form2(forms.Form):
    country = forms.ChoiceField(
        label='国',
        choices=COUNTRY_CHOICES,
        widget=forms.RadioSelect(
            attrs={ 
                "class": "form-control", 
            }
        )
    )
    area = forms.ChoiceField(
        label='エリア',
        choices=AREA_CHOICES,
        widget=forms.RadioSelect(
            attrs={ 
                "class": "form-control", 
            }
        )
    )
    city = forms.MultipleChoiceField(
        label='市',
        choices=CITY_CHOICES1_w,
        widget=forms.CheckboxSelectMultiple(
            attrs={ 
                "class": "form-control", 
            }
        )
    )