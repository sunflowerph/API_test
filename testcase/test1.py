# coding=utf-8
import requests
import unittest


class ceshi(unittest.TestCase):
    base_url='https://qiubo-dev.dongpinbang.com:61501/v1'
    token='S73jLFPX5gYG0WY9WIglqehqEsd-w9XVIG0hPcdvOHyibm-gqDB1' \
          'BeNqaCv1td4-tVcIyrqw6JNE54lEbljOvrMLec2qnJG1N6CcQHsgwQ24iCLg6AQ63uFPvN4U4vvN'

    def test_get_focus_list(self):#获取首页焦点图列表

        url = self.base_url+'/home-config/get-focus-list'
        search = {'token': self.token}
        response1=requests.request('GET',url=url,params=search)
        response=response1.json()
        try:
            self.assertEqual(response1.status_code, 200)
            print ('test_get_focus_list pass')
        except Exception as e:
            print (e)
            print ('test_get_focus_list faild')

    def test_get_all_location_list(self):#获取首页活动列表

        url=self.base_url+'/home-config/get-activity-list'
        search = {'token': self.token}
        response=requests.request('GET',url=url,params=search).json()
        try:
            self.assertEqual(response['message'], 'ok')
            print ('test_get_activity_list pass')
        except Exception as e:
            print (e)
            print ('test_get_activity_list faild')

    def test_get_icon_list(self):#获取首页icon列表
        url =self.base_url+'/home-config/get-icon-list'
        search = {'token': self.token}
        response = requests.request('GET', url=url, params=search).json()
        try:
            self.assertEqual(response['message'], 'ok')
            print ('test_get_icon_list pass')
        except Exception as e:
            print e
            print ('test_get_icon_list faild')

    def test_get_tip_list(self):  # 获取首页i滚动播放tip
        url = self.base_url+'/home-config/get-tip-list'
        search = {'token': self.token}
        response = requests.request('GET', url=url, params=search).json()
        #response=requests.get(url,params=search)
        #print response
        try:
            self.assertEqual(response['message'], 'ok')
            print ('test_get_tip_list pass')
        except:
            print ('test_get_tip_list faild')

    def test_change_nickname(self):  # 更改用户昵称
        url = self.base_url+'/account/change-nickname'
        search = {'token': self.token,
                  'nickname': u'彭连锁4店'}
        response=requests.request('POST',url=url,data=search).json()
        #response = requests.post(url, data=search).json()
        #print response
        try:
            self.assertEqual(response['message'], 'ok')
            print ('test_change_nickname pass')
        except:
            print ('test_change_nickname faild')

    def test_get_all_location_list(self): #获取地址信息列表
        url=self.base_url+'/config/get-all-location-list'
        search={'token':self.token}
        response=requests.request('GET',url=url,params=search).json()
        try:
            self.assertEqual(response['message'], 'ok')
            print ('test_get_all_location_list pass')
        except:
            print ('test_get_all_location_list faild')


if __name__ == "__main__":

    unittest.main()





