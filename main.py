# Author: Autumnhui
import requests
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import jieba


# 页面刷新时，变化的是接口中start的参数，为从0-200的间隔20的数字。⬇️获取所有请求数据。
for i in range(0,200,20):
    # 开发者工具-网络中items..的文件为数据，查看Headers获取网页请求的Requests Url
    url = 'https://m.douban.com/rexxar/api/v2/gallery/topic/20737/items?' \
          'sort=hot&start=0&count=20&status_full_text=1&guest_only=0&ck=null'.format(i)

    # 豆瓣反爬虫机制，需带上请求头。
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0".3809.100 Safari/537.36',
               'Referer': 'https://www.douban.com/gallery/topic/20737/?from=gallery_hot_post'}

    # 发送请求，获取响应
    reponse = requests.get(url, headers=headers)
    html = reponse.json()

    # 解析数据，并保存到本地
    for j in range(19):
        abs = html['items'][j]['abstract']
        with open("data.txt", "a", encoding='utf-8') as f:
            f.write(abs)
            print(abs)

# 获得wordcloud 需要的文本格式
with open("data.txt", "r", encoding='utf-8') as f:
     text = ' '.join(jieba.cut(f.read(),cut_all=False))
     # print(text)

backgroud_Image = plt.imread('背景图.png')  # 背景图，生成图片的大小为背景图的大小

# 词云的一些参数设置
wc = WordCloud(
      background_color='white',
      mask=backgroud_Image,
      font_path='pixel.ttf',
      max_words=400,
      max_font_size=200,
      min_font_size=8,
      random_state=50,
      )

# 生成词云
word_cloud = wc.generate_from_text(text)

plt.imshow(word_cloud)
plt.axis('off')

wc.to_file('输出结果.jpg')


# # 看看词频高的有哪些
# process_word = WordCloud.process_text(wc, text)
# sort = sorted(process_word.items(), key=lambda e: e[1], reverse=True)
# sort_after = sort[:50]
# print(sort_after)
#
# # 把数据存成csv文件
# df = pd.DataFrame(sort_after)
# # 保证不乱码
# df.to_csv('sort_after.csv', encoding='utf_8_sig')
