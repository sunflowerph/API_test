# coding=utf-8
import requests
import unittest


class ceshi(unittest.TestCase):


    def test_get_focus_list(self):#获取首页焦点图列表
        url = "https://qiubo-dev.dongpinbang.com:61501/v1/home-config/get-focus-list"
        search = {'token': '304uTFI8xohdghTwHqtdhcfmAtkuKYfBFLjKZOgvoQbASg0p3w48XBjCs1VcgaqJjKbOeokLj'
                           'kVFf4ahSNnhRk7ldqYwn7DgkOE0c15iscmMI1nAEysP375qHI6JRBAv'}
        response=requests.request('GET',url=url,params=search).json()
        self.assertEqual(response['message'],'ok')

    def test_get_activity_list(self):#获取首页活动列表
        url="https://qiubo-dev.dongpinbang.com:61501/v1/home-config/get-activity-list"
        search = {'token': '304uTFI8xohdghTwHqtdhcfmAtkuKYfBFLjKZOgvoQbASg0p3w48XBjCs1VcgaqJjKbOeokLj'
                           'kVFf4ahSNnhRk7ldqYwn7DgkOE0c15iscmMI1nAEysP375qHI6JRBAv'}
        response=requests.request('GET',url=url,params=search).json()
        self.assertEqual(response['message'],'ok')

    def test_get_icon_list(self):#获取首页icon列表
        url = "https://qiubo-dev.dongpinbang.com:61501/v1/home-config/get-icon-list"
        search = {'token': '304uTFI8xohdghTwHqtdhcfmAtkuKYfBFLjKZOgvoQbASg0p3w48XBjCs1VcgaqJjKbOeokLj'
                           'kVFf4ahSNnhRk7ldqYwn7DgkOE0c15iscmMI1nAEysP375qHI6JRBAv'}
        response = requests.request('GET', url=url, params=search).json()
        self.assertEqual(response['message'], 'ok')

    def test_get_tip_list(self):  # 获取首页i滚动播放tip
        url = "https://qiubo-dev.dongpinbang.com:61501/v1/home-config/get-tip-list"
        search = {'token': '304uTFI8xohdghTwHqtdhcfmAtkuKYfBFLjKZOgvoQbASg0p3w48XBjCs1VcgaqJjKbOeokLj'
                           'kVFf4ahSNnhRk7ldqYwn7DgkOE0c15iscmMI1nAEysP375qHI6JRBAv'}
        response = requests.request('GET', url=url, params=search).json()
        #response=requests.get(url,params=search)
        #print response
        self.assertEqual(response['message'], 'ok')

    def test_change_nickname(self):  # 更改用户昵称
        url = "https://qiubo-dev.dongpinbang.com:61501/v1/account/change-nickname"
        search = {'token': '304uTFI8xohdghTwHqtdhcfmAtkuKYfBFLjKZOgvoQbASg0p3w48XBjCs1VcgaqJjKbOeokLjk'
                           'VFf4ahSNnhRk7ldqYwn7DgkOE0c15iscmMI1nAEysP375qHI6JRBAv',
                  'nickname': u'彭连锁4店'}
        response=requests.request('POST',url=url,data=search).json()
        #response = requests.post(url, data=search).json()
        #print response
       # print response.status_code#返回响应码
        self.assertEqual(response['message'], 'ok')
        

if __name__ == "__main__":

    unittest.main()





