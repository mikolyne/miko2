
'''操作コマンドを記述。ファイル書き込み以外は通常のshell 操作と同じ。
ただし、ディレクトリ作成は絶対パスで行う事。ファイル作成時は、該当ディレクトリにファイル名を記述する。'''

request = '''django-admin startproject aaa
cd aaa
python manage.py startapp bbb
cd bbb
urls.py
models.py
views.py
cd ../aaa
urls.py
settings.py
cd ../
python manage.py makemigrations
python manage.py migrate
cd bbb
admin.py
mkdir C:\\Users\\fmiko\\mcode\\aaa\\templates
cd ../templates
list.html
'''
#ファイルに記述するコードを書く。
bbb_url_line = '''from django.urls import path
from .views import BlogList
urlpatterns=[
    path('list/',BlogList.as_view()),
]'''

bbb_models_line = '''from django.db import models
class Blogmodel (models.Model):
    urls = models.CharField(max_length=100)
    jikyu = models.CharField(max_length=100)
    station = models.CharField(max_length=100)
    wk_times = models.CharField(max_length=100)
    working_num = models.CharField(max_length=100)
    nikkyu = models.CharField(max_length=100)
    def __init__(self):
        return self.title'''

bbb_view_line = '''from .models import Blogmodel
from django.shortcuts import render
from django.views.generic import ListView
class BlogList(ListView):
    template_name = 'list.html'
    model = Blogmodel'''
 
aaa_url_line = '''from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('bbb.urls'))
]
'''

#settings_line

bbb_admin_line ='''from django.contrib import admin
from .models import Blogmodel
admin.site.register(Blogmodel)
'''

templates_list_line = '''<table>
    <tr>
        <td>URL</td>
        <td>jikyu</td>
        <td>station</td>
        <td>working time</td>
        <td>amount of working time</td>
        <td>income per one day (predict)</td>
    </tr>
    {% for item in object_list %}
    <tr>
        <td>{{ item.urls }}</td>
        <td>{{ item.jikyu }}</td>
        <td>{{ item.station }}</td>
        <td>{{ item.wk_times }}</td>
        <td>{{ item.working_num }}</td>
        <td>{{ item.nikkyu }}</td> 
    </tr>
    {% endfor %}
</table>'''