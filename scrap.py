from bs4 import BeautifulSoup as bs
f=open("c:/users/dell/desktop/se2.html")
d=bs(f,'html.parser')
n=1
font=d.findAll("font",{"color":"#FFFFFF"})
img=d.findAll("img",{"alt":"Click on the Serie image to view the images of LAICHE AHMED ILYES"})
a=d.findAll("a",{"title":"Series"})
for i in font:
 i.string=f"PAT-204635 - LAICHE MOHAMED ISLAM - Number {n}"
 n=n+1

for i in img:
 i["alt"]="Click on the Serie image to view the images of LAICHE MOHAMED ISLAM"

for i in a:
 a.string="LAICHE MOHAMED ISLAM MR"

with open ("c:/users/dell/desktop/se2.html","wb") as ff:
   ff.write(d.prettify("utf-8"))
input()