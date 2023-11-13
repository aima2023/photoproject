from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from .forms  import CustomUserCreationForm
from django.urls import reverse_lazy

class SignUpView(CreateView):
    #入力項目を設定したフォームの指定
    form_class = CustomUserCreationForm
    #描画（レンダリング）するHTMLファイルの指定
    template_name = 'signup.html'
    #サインアップ完了後に移る（遷移する）先の指定
    success_url = reverse_lazy('accounts:signup_success')
    #フォームに入力された情報をデータベース（モデル）に保存する
    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)

class SignUpSuccessView(TemplateView):
    #描画（レンダリング）するHTMLファイルの指定
    template_name = 'signup_success.html'
    

