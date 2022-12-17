# run torrent-stream-server serve in terminal
#------------------------------------------------------------------RUN THIS FILE----------------------------------------------------------------------------
from v1 import x
from urllib.request import Request, urlopen
import re
import webview
f=Request(x, headers={'User-Agent': 'Mozilla/5.0'})
f=urlopen(f).read().decode()
f=re.split('<a href="magnet',f)
magnet=("magnet"+f[1][:f[1].index('"')])
webview.create_window('Download', f'http://127.0.0.1:3000/play?torrent={magnet}',width=1080, height=720)
webview.start(gui='cef')
