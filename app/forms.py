from django import forms

COUNTRY_CHOICES = (
    (1, '日本'),
    (2, 'アメリカ'),
    (3, 'イギリス'),
)


CITY_CHOICES1 = (
    (1, '東京'),
    (2, '京都'),
    (3, '大阪'),
    (4, '沖縄'),
)

CITY_CHOICES2 = (
    (1, 'ワシントン'),
    (2, 'ロサンゼルス'),
)

CITY_CHOICES3 = (
    (1, 'ロンドン'),
)


class Form1_1(forms.Form):
    country = forms.ChoiceField(
        label='国',
        choices=COUNTRY_CHOICES,
    )


class Form1_2(forms.Form):
    city = forms.MultipleChoiceField(
        label='市',
        choices=CITY_CHOICES1,
    )