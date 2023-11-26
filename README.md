# Sample_app

# 概要
- Djangoの学習の為に作成したプロジェクトです。

# プロジェクト作成

- Djangoプロジェクト作成
```
django-admin startproject [プロジェクト名]
```

- ローカルアクセス
```
cd [プロジェクト名]
python manage.py runserver 
```

- アプリの作成
```
python manage.py startapp [アプリケーション名]
```

- アプリケーションの登録
```
django_app > settings.py

INSTALLED_APPS = [
    ・・・,
	'sqlapp',
]
```

- テンプレートを置く
```
[アプリケーション名] > templates > index.html
```

- views.appを設定
```
from django.shortcuts import render

def index(request):
	params = {
		'title': 'Hell Django',
	}
	return render(request, 'index.html', params)
```

- urs.py(プロジェクト側の設定)
```
from django.contrib import admin
from django.urls import path, include　＊

urlpatterns = [
    ・・・,
	path('[アプリ名]/', include('[アプリ名].urls')),　＊
]
```

- urs.py(アプリ側の設定)
```
from django.urls import path
from . import views

urlpatterns = [
	path('',views.index, name='index'),
]
```
# SQL_app

## データベース準備

- models.pyの作成

- インストール
```
pip install mysql-connector-python
```

- databaseの設定
```
DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',　＃使用しているドライバ
        'NAME': [データーベース],
        'USER': [mySQLのuser]',
        'PASSWORD': [mySQLのパスワード],
		'HOST': 'localhost',
        'PORT': [ローカルポスト番号],
    }
}
```

- マイグレーション
```
python manage.py makemigrations [アプリ名]
python manage.py migrate 
```