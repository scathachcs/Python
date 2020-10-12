from urllib import request
from urllib import error
import socket
from bs4 import BeautifulSoup as bs

url = 'http://jwc.scu.edu.cn/'

try:
    resp =request.urlopen(url)
    html_data=resp.read().decode('utf-8')
except error.URLError as ex:
    html_data=None
except socket.timeout as ex:
    html_data = None

if html_data:
    soup = bs(html_data,'html.parser')
    school_div=soup.find_all('div',class_='list-llb-box')
    news_list_s=school_div[0].find_all('span')
    news_list=[]
    for span in news_list_s:
        if span.string:
            news_list.append(span.string)
    time_list_e=school_div[0].find_all('em',class_='fr list-date-a')
    time_list=[]
    for time in time_list_e:
        if time.string:
            time_list.append(time.string)

    news_time_list=zip(news_list,time_list)
    print(list(news_time_list))
    