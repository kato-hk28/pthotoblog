import requests
import time
from pathlib import Path
from bs4 import BeautifulSoup
import os

def main():
    create_folder()
    urls = get_new_blog_urls()
    for url in urls:
        execute(url)

def create_folder():
    path = os.getcwd() + "\\hinata_blog\\"
    if not os.path.isdir(path):
        os.makedirs(path)

def get_new_blog_urls():
    urls = []
    blog_top_url = "https://www.hinatazaka46.com/s/official/diary/member?ima=0000"
    html = requests.get(blog_top_url).text
    soup = BeautifulSoup(html,'html.parser')
    a_list = soup.select('body > div > main > section > div > div.l-contents > div.l-maincontents.l-maincontents--100 > div.p-blog-top__contents > ul > li > a')
    for a in a_list:
        url = "https://www.hinatazaka46.com" + a.attrs['href']
        urls.append(url)
    return urls

def execute(url):
    html  = requests.get(url).text
    soup  = BeautifulSoup(html,'html.parser')
    title = soup.find(class_ = 'c-blog-article__title').text
    name  = soup.find(class_ = 'c-blog-page__subtitle').text
    img_list = soup.select('img')

    print(name.strip())

    for img in img_list:
        img_url  = img.attrs['src']
        if not "/diary/official/" in img_url:
            continue
        time.sleep(1.0)
        image    = requests.get(img_url)
        filename = os.path.basename(img_url)
        path     = os.getcwd() + "\\hinata_blog\\"
        img_path = path + filename
        if not os.path.isfile(img_path):
            save_photo(img_path,image)
            send_photo(img_path,name,title)
        else:
            print('alredy exist')
            exit()

def save_photo(img_path,image):
    with open(img_path,'wb') as f:
        f.write(image.content)
    print("saved")

def send_photo(img_path,name,title):
    line_url = "https://notify-api.line.me/api/notify"
    access_token = 'your line access_token' #LINE APIから自分のアクセストークンを取得して置換する
    headers = {'Authorization':'Bearer ' + access_token}
    message = '\n[' + name.strip() + ']\n' + title.strip()
    payload = {'message':message}
    photo = {'imageFile':open(img_path,'rb')}
    requests.post(line_url,headers=headers,params=payload,files=photo,)
    print('sent')

if __name__ == "__main__":
    main()