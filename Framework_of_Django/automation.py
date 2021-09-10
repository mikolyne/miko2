import subprocess
import os
from stpy import aaa_settings_line
from lines import request,bbb_url_line, bbb_models_line , aaa_url_line, bbb_admin_line, bbb_view_line,templates_list_line
req_lines =[bbb_url_line,bbb_models_line,bbb_view_line,aaa_url_line,aaa_settings_line,bbb_admin_line,templates_list_line]
#このファイルでDjangoの構築を実行する。
#os subprocess の他にlines.py stpy.pyから、操作コマンドと挿入するコードをインポート 
#作成ファイル順にリストにlinesを挿入 

#書き込み関数を定義 
def write (file,lines):
    op = open(file,'w')
    op.writelines(lines + '\n')
    op.close()

command = request.splitlines()
count = 0
line_count = 0

#.py .html .json の場合は書き込み 
#manage.py を検出してsubprocessを実行 
#cd mkdir を検出してshell 操作 
for com in command:
    count +=1
    if 'cd ' in com:
        os.chdir(com.replace('cd ',''))
    elif '.py' in com:
        if 'manage.py' not in com:
            write(com,req_lines[line_count])
            line_count +=1
        else:
            subprocess.run(com.split(),shell=True)
    elif '.html' in com:
        write(com,req_lines[line_count])
        line_count +=1
    elif 'mkdir' in com:
        os.makedirs(com.replace('mkdir ',''))
    else:
        subprocess.run(com.split(),shell=True)
