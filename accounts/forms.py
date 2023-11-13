#UserCreationFormクラスをインポート
from django.contrib.auth.forms import UserCreationForm
#models.pyファイルで定義したCustomUserクラス（モデル）をインポート
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        #UserモデルからCustomUserモデルへ変更
        model = CustomUser
        #フォームで入力する項目を
        #ユーザー名、メアド、PW、PW（確認用）
        fields = ('username', 'email', 'password1', 'password2')
        
    

