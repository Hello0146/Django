from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # 모델의 필드 이름과 일치해야 합니다.

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # 댓글의 내용만 입력받습니다.