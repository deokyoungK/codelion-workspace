from django import forms
from .models import Post,Comment,freePost,freeComment

class Postform(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Postform, self).__init__(*args,**kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "내용을 입력해주세요",
            'rows': 20,
            'cols': 100
        }

class Commentform(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['comment_body']

    def __init__(self, *args, **kwargs):
        super(Commentform, self).__init__(*args,**kwargs)

        self.fields['comment_body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }

class freePostform(forms.ModelForm):
    class Meta:
        model = freePost
        fields = ['title','body']

    def __init__(self, *args, **kwargs):
        super(freePostform, self).__init__(*args,**kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "글 제목을 입력해주세요",
            'rows': 20
        }

        self.fields['body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "내용을 입력해주세요",
            'rows': 20,
            'cols': 100
        }

class freeCommentform(forms.ModelForm):
    class Meta: 
        model = freeComment
        fields = ['comment_body']

    def __init__(self, *args, **kwargs):
        super(freeCommentform, self).__init__(*args,**kwargs)

        self.fields['comment_body'].widget.attrs = {
            'class': 'form-control',
            'placeholder': "댓글을 입력해주세요",
            'rows': 10
        }


