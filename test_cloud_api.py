#!/usr/bin/env python3
import requests
import json

# 配置
APPID = "wxe0bc63c45ad39a98"
APPSECRET = "05ea8f31c1104dabb360d90f8d056f9a"
ENV = "cloud1-2gyunsvp996c4a0f"

def get_access_token():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={APPSECRET}"
    resp = requests.get(url)
    print(f"获取access_token响应: {resp.text}")
    resp.raise_for_status()
    data = resp.json()
    return data["access_token"]

def test_env(access_token):
    """测试环境是否连通"""
    url = f"https://api.weixin.qq.com/tcb/getappinfo?access_token={access_token}"
    payload = {"env": ENV}
    resp = requests.post(url, json=payload)
    print(f"测试环境响应: {resp.text}")
    return resp.json()

def add_test_data(access_token):
    """插入测试数据"""
    url = f"https://api.weixin.qq.com/tcb/database/add?access_token={access_token}"
    payload = {
        "env": ENV,
        "query": "db.collection(\"daily_sentences\").add({data: {category: \"motivational\", content: \"测试数据\"}})"
    }
    resp = requests.post(url, json=payload)
    print(f"插入测试数据响应: {resp.text}")
    return resp.json()

if __name__ == "__main__":
    try:
        token = get_access_token()
        print(f"access_token: {token[:50]}...")
        test_env(token)
        add_test_data(token)
    except Exception as e:
        print(f"错误: {e}")
