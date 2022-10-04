# 抓取 PTT 電影版的網頁原始碼 (HTML)
import urllib.request as req
import bs4
def get_data(url, how_list, pu_list, fu_list):
    # 建立一個 Request 物件，附加 Request Headers 的資訊
    request=req.Request(url, headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"})
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    # print(data)
    # 解析原始碼，取得每篇文章的標題
    root=bs4.BeautifulSoup(data, "html.parser") # 讓 BeautifulSoup 協助我們解析 HTML 格式文件
    titles=root.find_all("div", class_="title") # 尋找所有 class="title" 的 div 標籤
    for title in titles:
        if title.a != None: # 如果標題包含 a 標籤 (沒有被刪除)，印出來
            # print(title.a.string)
            if title.a.string[:4]==f'[好雷]':
                how_list.append(title.a.string)
            elif title.a.string[:4]==f'[普雷]':
                pu_list.append(title.a.string)
            elif title.a.string[:4]==f'[負雷]':
                fu_list.append(title.a.string)
            else:
                pass
    # 抓取上一頁的連結
    next_link=root.find("a", string="‹ 上頁") # 找到內文是 ‹ 上頁 的 a 標籤
    return next_link["href"]
# input
page_url="https://www.ptt.cc/bbs/movie/index.html"
how_list=[]
pu_list=[]
fu_list=[]
count=0
#  get data
while count<10:
    page_url="https://www.ptt.cc"+get_data(page_url, how_list, pu_list, fu_list)
    count+=1
# output file
with open("movie.txt", "w", encoding= "utf-8") as file:
    for item in how_list:
        file.write(item+"\n")
    for item in pu_list:
        file.write(item+"\n")
    for item in fu_list:
        file.write(item+"\n")
    print("File completed!!")