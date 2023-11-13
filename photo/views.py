from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from django.urls import reverse_lazy
from .forms import PhotoPostForm
from .models import PhotoPost
#以下2つはログイン状態でviewを呼び出すためのもの
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class IndexView(ListView):
    
    #index.htmlを指定する
    template_name = 'index.html'

    # PhotoPostモデルのオブジェクトにorder_by()を適応
    # 投稿日時の降順（新しい順）で並べ替える
    queryset=PhotoPost.objects.order_by('-posted_at')
    
    paginate_by=9
#ログイン状態の時のみ以下のviewを使えるようにする
@method_decorator(login_required, name='dispatch')
class CreatePhotoView(CreateView):
    #フォーム（入力項目）の設定
    form_class = PhotoPostForm
    #描画するHTMLファイル
    template_name = 'post_photo.html'
    #データ登録後に移る（リダイレクトされる）ページ
    success_url = reverse_lazy('photo:post_done')
    
    #入力されたデータ（画像含む）をモデルに保存
    def form_valid(self, form):
        #送信されてきた(POSTされた)データを取得
        postdata = form.save(commit=False)
        #投稿(ログインしている)ユーザをpostdataのユーザに代入
        postdata.user = self.request.user
        #データベースに保存
        postdata.save()
        
        return super().form_valid(form)

class PostSuccessView(TemplateView):
    #描画するHTMLファイル
    template_name = 'post_success.html'
    
class CategoryView(ListView):
    template_name='index.html'
    paginate_by=6
    def get_queryset(self):
        category_id=self.kwargs['category']
        records=PhotoPost.objects.filter(
            category=category_id).order_by('-posted_at')
        return records
    
class UserView(ListView):
    template_name='index.html'
    paginate_by=6
    
    def get_queryset(self):
        user_id=self.kwargs['user']
        records=PhotoPost.objects.filter(
            category=user_id).order_by('-posted_at')
        return records
    
class PhotoDetailView(DetailView):
    template_name='detail.html'
    model=PhotoPost
    
class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=6
    def get_queryset(self):
        records=PhotoPost.objects.filter(
            user=self.request.user).order_by('-posted_at')
        return records
    
class PhotoDeleteView(DeleteView):
    template_name='photo_delete.html'
    model=PhotoPost
    success_url=reverse_lazy('photo:mypage')