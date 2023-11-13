from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    #表示する項目をidとusernameにする
    list_display = ('id', 'username')
    #表示する項目にリンクを設定する
    list_display_links = ('id', 'username')

#管理サイトにCustomUserクラスと
#CustomUserAdminクラスを登録
admin.site.register(CustomUser, CustomUserAdmin)

