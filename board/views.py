from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, CommentForm



def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'board/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # pk에 해당하는 게시글을 가져옵니다.
    post = get_object_or_404(Post, pk=pk)

    # 댓글 제출 처리
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post  # 이 댓글이 해당 게시글에 달리도록 연결합니다.
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'board/post_detail.html', {'post': post, 'form': comment_form})


def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # 새 게시글 저장
            return redirect('post_list')  # 저장 후 게시글 목록 페이지로 이동
    else:
        form = PostForm()
    return render(request, 'board/post_create.html', {'form': form})