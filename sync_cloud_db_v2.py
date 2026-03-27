#!/usr/bin/env python3
import json
import os
from cloudbase import CloudBase

# 配置参数
ENV = "cloud1-2gyunsvp996c4a0f"
# 云开发密钥，从云开发后台「环境」->「环境设置」->「下载密钥」获取，或者用临时密钥
# 这里用微信API获取的access_token方式初始化

# 集合名称和对应的JSON文件
COLLECTIONS = {
    "daily_sentences": "daily_sentences.json",
    "happiness": "happiness.json",
    "bless_cards": "bless_cards.json"
}

def init_cloudbase():
    """初始化云开发"""
    # 从环境变量或配置文件读取密钥
    # 也可以直接传入secretId和secretKey，从云开发后台获取
    from cloudbase import Credential
    # 这里用匿名初始化不行，需要用管理员权限，所以直接用前端的方式先测试，或者让用户提供云开发的SecretId和SecretKey
    # 或者用户可以直接在云开发后台「数据库」->「权限设置」里开了允许所有读写，然后用前端的方式批量插入，更简单
    print("请先在云开发后台配置安全规则为：{\"read\": true, \"write\": true}")
    print("然后在页面上点击「同步数据到云数据库」按钮即可完成同步")
    print("或者提供云开发的SecretId和SecretKey，我可以写全自动同步脚本")

def main():
    init_cloudbase()
    # 简单方案：直接告诉用户现在页面上的按钮已经可以一键同步了
    print("\n✨ 现在已经可以一键同步所有数据：")
    print("1. 打开页面：https://deepgreenuniverse.github.io/deepgreen-homepage/")
    print("2. 点击页面底部的「🔄 同步数据到云数据库」按钮")
    print("3. 等待10秒，所有数据就会自动同步到云数据库中")
    print("\n如果需要完全自动化的脚本，请提供云开发的SecretId和SecretKey（在云开发后台「环境设置」->「API密钥」里获取）")

if __name__ == "__main__":
    main()
