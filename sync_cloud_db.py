#!/usr/bin/env python3
import requests
import json
import os

# 配置参数
APPID = "wxe0bc63c45ad39a98"
APPSECRET = "05ea8f31c1104dabb360d90f8d056f9a"
ENV = "cloud1-2gyunsvp996c4a0f"

# 集合名称和对应的JSON文件
COLLECTIONS = {
    "daily_sentences": "daily_sentences.json",
    "happiness": "happiness.json",
    "bless_cards": "bless_cards.json"
}

def get_access_token():
    """获取微信API access_token"""
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={APPSECRET}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    if "errcode" in data and data["errcode"] != 0:
        raise Exception(f"获取access_token失败: {data}")
    return data["access_token"]

def batch_insert(access_token, collection_name, data_list):
    """批量插入数据到云数据库"""
    url = f"https://api.weixin.qq.com/tcb/databasebatchinsert?access_token={access_token}"
    # 每次最多插入20条
    batch_size = 20
    success_count = 0
    for i in range(0, len(data_list), batch_size):
        batch = data_list[i:i+batch_size]
        payload = {
            "env": ENV,
            "collection_name": collection_name,
            "data": [json.dumps(item, ensure_ascii=False) for item in batch]
        }
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        res = resp.json()
        if res["errcode"] != 0:
            print(f"批次插入失败: {res['errmsg']}")
            continue
        success_count += len(res["id_list"])
        print(f"已插入 {success_count}/{len(data_list)} 条数据")
    print(f"{collection_name} 同步完成，共插入 {success_count} 条数据")

def main():
    try:
        # 获取access_token
        print("正在获取access_token...")
        access_token = get_access_token()
        print("access_token获取成功")
        
        # 同步每个集合
        for collection, file_path in COLLECTIONS.items():
            if not os.path.exists(file_path):
                print(f"文件 {file_path} 不存在，跳过")
                continue
            # 读取JSON数据
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            print(f"\n开始同步 {collection}，共 {len(data)} 条数据...")
            batch_insert(access_token, collection, data)
        
        print("\n✅ 所有数据同步完成！")
        
    except Exception as e:
        print(f"❌ 同步失败: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
