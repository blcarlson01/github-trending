# coding:utf-8

import datetime
import codecs
from pyquery import PyQuery as pq
import json
from security import safe_requests

def createMarkdown(date, filename):
    with open(filename, 'w') as f:
        f.write("## " + date + "\n")

def create_json(data, title, url, description):
    data['site'].append({  
    'title': title,
    'url': url,
    'description': description
    })

def write_json(data, filename):
    with open(filename, 'w') as outfile:  
        json.dump(data, outfile)    

def scrape(language, filename, json_filename):

    HEADERS = {
        'User-Agent'		: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
        'Accept'			: 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding'	: 'gzip,deflate,sdch',
        'Accept-Language'	: 'zh-CN,zh;q=0.8'
    }

    url = 'https://github.com/trending/{language}'.format(language=language)
    r = safe_requests.get(url, headers=HEADERS, timeout=60)
    assert r.status_code == 200

    # print(r.encoding)

    d = pq(r.content)
    items = d('ol.repo-list li')
    json_data = {}
    json_data['site'] = [] 

    # codecs to solve the problem utf-8 codec like chinese
    with codecs.open(filename, "a", "utf-8") as f:
        f.write('\n#### {language}\n'.format(language=language))

        for item in items:            
            i = pq(item)
            title = i("h3 a").text()
            owner = i("span.prefix").text()
            description = i("p.col-9").text()
            url = i("h3 a").attr("href")
            url = "https://github.com" + url
            # ownerImg = i("p.repo-list-meta a img").attr("src")
            # print(ownerImg)
            create_json(json_data, title, url, description)
            f.write(u"* [{title}]({url}):{description}\n".format(title=title, url=url, description=description))

    write_json(json_data, json_filename)
    
def job():

    strdate = datetime.datetime.now().strftime('%Y-%m-%d')
    filename = '{date}.md'.format(date=strdate)
    json_filename = '{date}.json'.format(date=strdate)

    # create markdown file
    createMarkdown(strdate, filename)

    # write markdown
    scrape('java', filename, json_filename)

if __name__ == '__main__':
        job()
