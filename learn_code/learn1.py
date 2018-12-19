# coding=utf-8
import requests

token='S73jLFPX5gYG0WY9WIglqehqEsd-w9XVIG0hPcdvOHyibm-gqDB1BeNqa' \
      'Cv1td4-tVcIyrqw6JNE54lEbljOvrMLec2qnJG1N6CcQHsgwQ24iCLg6AQ63uFPvN4U4vvN'

# get 请求  requests.get()方法
url='https://qiubo-dev.dongpinbang.com:61501/v1/home-config/get-focus-list'
response1=requests.get(url)
print response1.status_code #返回状态码


#post 请求  requests.post()方法
url1='https://qiubo-dev.dongpinbang.com:61501/v1/account/change-nickname'
data={'token': token,
      'nickname': '无店铺'}
response2=requests.post(url1,data=data)
print response2.status_code
print response2.text


#requests.request()方法

#get 请求
params={'token':token}
response3=requests.request('GET',url=url,params=params)
response5=response3.json()
print response5
print response3.headers #获得字典形式展示的服务器响应头
try:
    assert response5['message'] == 'ok'
    print 'yes'
except Exception as e:
    print e
    print 'no'

#post请求
response4=requests.request('POST',url=url1,data=data)
print response4.status_code
print response4.text


#request 请求中传入一个文件
# file=open('/Users/ph/desktop/1.txt','rb')
# response6=requests.get(url=url,file=file)


#设置请求超时时间
requests.get('https://baidu.com',timeout=0.4) #timeout 仅对连接过程有效，与响应体的下载无关。 timeout 并不
# 是整个下载响应的时间#限制，而是如果服务器在 timeout 秒内没有应答，将会引发一个异常（更精确地说，是在 timeout 秒
# 内没有从基础套接字上接收到任何字节的数据时)。


