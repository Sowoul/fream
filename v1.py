from urllib.request import Request, urlopen
import re
import webview
game=input()
game=game.replace(' ','+')
g=Request(f"https://fitgirl-repacks.site/?s={game}", headers={'User-Agent': 'Mozilla/5.0'})
f=urlopen(g).read().decode()
f=(re.split('<h1 class="entry-title"><a href="',f))[:4]
x=[]
for i in range(1,4):
    try:
        title=re.split('" rel="bookmark">',f[i])
        print(f"{i}. "+title[1][:title[1].index("&")])
        x.append((f[i])[:f[i].index('"')])
    except:
        pass
select=int(input("Make a choice from the above options."))
x=x[select-1]