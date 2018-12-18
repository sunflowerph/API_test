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

