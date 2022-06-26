from django import forms

class searchForm(forms.Form):
    searchword = forms.CharField(label='', max_length=100)

    def __init__(self, *args, **kwargs):
        super(searchForm, self).__init__(*args, **kwargs)

        self.fields['searchword'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "영화 제목을 검색하세요",
            'rows': 20
        }

