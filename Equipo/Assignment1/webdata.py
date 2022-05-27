from bs4 import BeautifulSoup
import requests
from csv import writer


#To get list of code("mcode")
url="https://www.hcpcsdata.com/Codes"
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
tdata=soup.find_all('a')
group=[]
mcodes=[]
for j in tdata:
    data=j.text
    group.append(data)
group.remove('\n\n')
group.remove('Codes')
group.remove('Modifiers')
group.remove('ICD10Data.com')
group.remove('License Data Files')
for k in group:
    c=k[1]
    mcodes.append(c)
# print(mcodes)
c=len(mcodes)
#Sorting datas
# allcodes=[]
# codesonly=[]
# group=[]
# category=[]
# codes=[]
# long=[]
# short=[]
# alldata=[]
with open('HCPCSdata.csv','w',encoding='utf8',newline='') as f:
    thewriter=writer(f)
    header=['Group','Catagory','Code','Long Description','Short Description']
    thewriter.writerow(header)
    for t in range(c-1):
        e=mcodes[t]
        # print(e)
        newurl="https://www.hcpcsdata.com/Codes"+"/"+e
        newpage=requests.get(newurl)
        details=BeautifulSoup(newpage.text,'html.parser')
        newtdata=details.find_all('tr')
        hdata=details.find('h1').text.replace("\r\n","").strip().split(",")
        ddata=details.find('h5')
        atdata=details.find_all('a',class_="identifier")
        for s in newtdata:
            newdata=s.text.strip().replace("\r\n","").split("\n\n                                    ")
            # group.append(hdata)
            # print(hdata)
            if ddata==None:
                # category.append(0)
                dddata=0

            else:
                dddata=ddata.text.replace("\r\n","").strip()
                # category.append(dddata)

            if newdata!=['Code\nDescription']:
                a=newdata[0]
                b=newdata[1]
                # codes.append(a)
                # print(a)
                # long.append(b)
                nnewurl = "https://www.hcpcsdata.com/Codes" + "/" + e+"/"+a
                page1=requests.get(nnewurl)
                soup1=BeautifulSoup(page1.text,'html.parser')
                kdata=soup1.find('tr')
                if kdata==None:
                    # short.append(0)
                    vdata=0
                else:
                    vdata=kdata.text.replace("Short Description","").strip()
                    # short.append(vdata)
                info=[hdata,dddata,a,b,vdata]
                thewriter.writerow(info)
    # for y in atdata:
    #     adata=y.text.strip()
    #     codesonly.append(adata)
# short=[]
# for b in codes:
#     for h in codesonly:
#         anewurl = "https://www.hcpcsdata.com/Codes" + "/" + b+"/"+h
#         nnewpage=requests.get(anewurl)
#         describ=BeautifulSoup(nnewpage.text,'html.parser')
#         shortdes=describ.find_all('td')
#         for w in shortdes:
#             sdata=w.text.strip()
#             short.append(sdata)
# print(short)