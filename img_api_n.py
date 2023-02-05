from bs4 import BeautifulSoup
from fastapi import FastAPI,File,UploadFile
import requests

app = FastAPI()
@app.post("/image/{keyword}")
async def image(keyword):

        headers = {
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
        }

        params = {
            "q": keyword,
            "cc": "us" # language/country of the search
        }

        html = requests.get('https://www.bing.com/images/search', params=params, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        data=[]
        for result in soup.select('.iusc'):
               try:

                    img = str(result).split(",")
                    temp =[]
                    for i in img[4:11]:
                        if '"t"' in i:
                                i = i.replace('"t":"',"")
                                temp.append(i.replace('"',""))                
                        if '"purl"' in i:
                                i = i.replace('"purl":"',"")
                                temp.append(i.replace('"',""))
                        if '"murl"' in i:
                                i = i.replace('"murl":"',"")
                                temp.append(i.replace('"',""))
                        if '"turl"' in i:
                                i = i.replace('"turl":"',"")
                                temp.append(i.replace('"',""))
                    if temp!=[]:
                            data.append(temp)
                   
               except:
                    print()
        return {"images":data}
