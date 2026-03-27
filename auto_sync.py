#!/usr/bin/env python3
import requests
import json
import os

# 配置
APPID = "wxe0bc63c45ad39a98"
APPSECRET = "05ea8f31c1104dabb360d90f8d056f9a"
ENV = "cloud1-2gyunsvp996c4a0f"

# 数据
DATA = {
    "daily_sentences": [
        {"category": "motivational", "content": "每一次努力都是幸运的起点"},
        {"category": "motivational", "content": "相信自己的力量，你能做到的"},
        {"category": "motivational", "content": "阳光总在风雨后"},
        {"category": "motivational", "content": "今天就是最好的开始"},
        {"category": "motivational", "content": "你的潜力远超你的想象"},
        {"category": "humorous", "content": "生活就像编程，偶尔需要debug"},
        {"category": "humorous", "content": "我的发际线是早睡早起"},
        {"category": "humorous", "content": "减肥从明天开始"},
        {"category": "philosophical", "content": "成功不是终点，失败不是末日"},
        {"category": "philosophical", "content": "时间会治愈一切，路要一步步走"},
        {"category": "romantic", "content": "你是我最美丽的遇见"},
        {"category": "romantic", "content": "有你的每一天都闪闪发光"}
    ],
    "happiness": [
        {"category": "life", "content": "今天天气真好，适合出门走走感受阳光"},
        {"category": "life", "content": "你今天真好看，保持这份好心情呀"},
        {"category": "work", "content": "今天工作效率超高，提前完成了任务"},
        {"category": "heal", "content": "没关系呀，你已经做得很好了"},
        {"category": "bless", "content": "祝你今天一天都顺顺利利，没有烦恼"}
    ],
    "bless_cards": [
        {"category": "birthday", "content": "祝生日快乐！愿你每一岁都奔走在自己的热爱里"},
        {"category": "festival", "content": "新年快乐！祝你新的一年，平安喜乐，万事胜意"},
        {"category": "promotion", "content": "恭喜升职！能力配得上努力，付出配得上回报"},
        {"category": "graduation", "content": "毕业快乐！愿你此去繁花似锦，再相逢依旧如故"}
    ]
}

def get_access_token():
    """获取access_token"""
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={APPSECRET}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    return data["access_token"]

def insert_data(access_token, collection, data_list):
    """插入数据"""
    url = f"https://api.weixin.qq.com/tcb/databaseadd?access_token={access_token}"
    success = 0
    for item in data_list:
        # 正确的query格式
        query = f"db.collection(\"{collection}\").add({{data: {json.dumps(item, ensure_ascii=False)}}})"
        payload = {
            "env": ENV,
            "query": query
        }
        resp = requests.post(url, json=payload)
        res = resp.json()
        if res["errcode"] == 0:
            success += 1
        else:
            print(f"插入失败: {res['errmsg']}")
    print(f"{collection} 成功插入 {success}/{len(data_list)} 条")
    return success

def main():
    try:
        token = get_access_token()
        print(f"access_token获取成功")
        total = 0
        for collection, data in DATA.items():
            cnt = insert_data(token, collection, data)
            total += cnt
        print(f"\n✅ 总共插入 {total} 条数据，同步完成！")
    except Exception as e:
        print(f"❌ 同步失败: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
