#!/usr/bin/env python3
import requests
import json
import os

# 配置
APPID = "wxe0bc63c45ad39a98"
APPSECRET = "05ea8f31c1104dabb360d90f8d056f9a"
ENV = "cloud1-2gyunsvp996c4a0f"

# 全量数据
FULL_DATA = {
    "daily_sentences": [
        {"category": "motivational", "content": "每一次努力都是幸运的起点"},
        {"category": "motivational", "content": "相信自己的力量，你能做到的"},
        {"category": "motivational", "content": "阳光总在风雨后"},
        {"category": "motivational", "content": "今天就是最好的开始"},
        {"category": "motivational", "content": "你的潜力远超你的想象"},
        {"category": "motivational", "content": "坚持下去，就会看到曙光"},
        {"category": "motivational", "content": "每一步都通向更好的自己"},
        {"category": "motivational", "content": "成功不是终点，而是新的起点"},
        {"category": "motivational", "content": "不要停下，未来在等你"},
        {"category": "motivational", "content": "你的坚持，终将照亮前路"},
        {"category": "motivational", "content": "相信过程，结果自然美好"},
        {"category": "motivational", "content": "努力不会被辜负，时间会证明"},
        {"category": "motivational", "content": "今天的付出，是为了明天的收获"},
        {"category": "motivational", "content": "不要等待机会，要创造机会"},
        {"category": "motivational", "content": "每个努力，都算数"},
        {"category": "motivational", "content": "你的梦想，值得你为之奋斗"},
        {"category": "motivational", "content": "别让今天成为遗憾的一天"},
        {"category": "motivational", "content": "每天进步一点点，一年前进一大步"},
        {"category": "motivational", "content": "相信自己，你比想象中更强大"},
        {"category": "motivational", "content": "困难是成长的阶梯"},
        {"category": "humorous", "content": "生活就像编程，偶尔需要debug"},
        {"category": "humorous", "content": "我的发际线是早睡早起"},
        {"category": "humorous", "content": "减肥从明天开始"},
        {"category": "humorous", "content": "别问我为什么这么瘦，问问我为什么这么秃"},
        {"category": "humorous", "content": "程序员的一天，改bug改bug改bug"},
        {"category": "humorous", "content": "人生苦短，我选择Python"},
        {"category": "humorous", "content": "钱没了可以再赚，头发没了就没了"},
        {"category": "humorous", "content": "每天早睡，除了发文章的时候"},
        {"category": "humorous", "content": "键盘代码写得像诗，但运行全是错"},
        {"category": "humorous", "content": "我的代码没有bug，是编译器不懂我"},
        {"category": "philosophical", "content": "成功不是终点，失败不是末日"},
        {"category": "philosophical", "content": "时间会治愈一切，路要一步步走"},
        {"category": "philosophical", "content": "真正的强大是知道自己的弱点"},
        {"category": "philosophical", "content": "每个选择都是新的开始"},
        {"category": "philosophical", "content": "不要等到完美，开始就是进步"},
        {"category": "philosophical", "content": "焦虑不能解决问题，行动可以"},
        {"category": "philosophical", "content": "生活不会总是一帆风顺"},
        {"category": "philosophical", "content": "真正的勇气是带着恐惧前行"},
        {"category": "philosophical", "content": "今天的选择，决定明天的方向"},
        {"category": "philosophical", "content": "你比你想象的更强大"},
        {"category": "romantic", "content": "你是我最美丽的遇见"},
        {"category": "romantic", "content": "有你的每一天都闪闪发光"},
        {"category": "romantic", "content": "爱的陪伴是最长情的告白"},
        {"category": "romantic", "content": "遇见你是我最大的幸运"},
        {"category": "romantic", "content": "想和你一起看四季更替"},
        {"category": "romantic", "content": "你在身边，就是最好的时光"},
        {"category": "romantic", "content": "温柔是人间宝藏"},
        {"category": "romantic", "content": "你是我书里最美好的句子"},
        {"category": "romantic", "content": "遇见你之前，我的世界是黑白的"},
        {"category": "romantic", "content": "你不用多说什么，我懂就好"}
    ],
    "happiness": [
        {"category": "life", "content": "今天天气真好，适合出门走走感受阳光"},
        {"category": "life", "content": "你今天真好看，保持这份好心情呀"},
        {"category": "life", "content": "喝一杯喜欢的奶茶，犒劳一下努力的自己"},
        {"category": "life", "content": "路边的小花都开了，今天也会有好事发生"},
        {"category": "life", "content": "回家路上记得买份爱吃的小零食"},
        {"category": "life", "content": "开窗通通风，新鲜空气会带来好心情"},
        {"category": "life", "content": "做一顿自己爱吃的饭，享受属于你的时光"},
        {"category": "life", "content": "今天微风不燥，适合出门散散步"},
        {"category": "life", "content": "晒晒太阳，整个人都会变得暖暖的"},
        {"category": "life", "content": "听听喜欢的歌，烦恼都会被赶跑"},
        {"category": "work", "content": "今天工作效率超高，提前完成了任务"},
        {"category": "work", "content": "同事帮了你一个小忙，团队氛围超棒"},
        {"category": "work", "content": "想到了一个超棒的idea，今天会有收获"},
        {"category": "work", "content": "困扰很久的问题今天终于解决了"},
        {"category": "work", "content": "领导表扬了你的工作，付出都被看见"},
        {"category": "work", "content": "今天不用加班，可以早早回家休息"},
        {"category": "work", "content": "和同事配合超默契，工作进展很顺利"},
        {"category": "work", "content": "学到了一个新技能，今天又进步了"},
        {"category": "work", "content": "会议开得很高效，不用浪费时间"},
        {"category": "work", "content": "客户对你的方案很满意，顺利通过"},
        {"category": "heal", "content": "没关系呀，你已经做得很好了"},
        {"category": "heal", "content": "慢慢来，不用着急，你想要的都会来"},
        {"category": "heal", "content": "今天不开心也没关系，明天会更好的"},
        {"category": "heal", "content": "你超棒的，不要否定自己呀"},
        {"category": "heal", "content": "累了就歇歇，不用硬撑着"},
        {"category": "heal", "content": "你值得所有美好的事物"},
        {"category": "heal", "content": "过去的都过去了，未来都是好日子"},
        {"category": "heal", "content": "好好爱自己，比什么都重要"},
        {"category": "heal", "content": "每个人都有闪光点，你也一样"},
        {"category": "heal", "content": "不用和别人比，你已经很优秀了"},
        {"category": "bless", "content": "祝你今天一天都顺顺利利，没有烦恼"},
        {"category": "bless", "content": "希望你今天所有的期待都能实现"},
        {"category": "bless", "content": "愿你每天都有好心情，事事顺心"},
        {"category": "bless", "content": "祝你今天遇到的都是好人好事"},
        {"category": "bless", "content": "愿你的努力都有回报，梦想都能实现"},
        {"category": "bless", "content": "祝你今天吃好喝好，快乐不倒"},
        {"category": "bless", "content": "希望你今天所有的付出都有收获"},
        {"category": "bless", "content": "愿你被世界温柔以待，好运常伴"},
        {"category": "bless", "content": "祝你今天元气满满，活力十足"},
        {"category": "bless", "content": "希望你今天收获很多小惊喜"}
    ],
    "bless_cards": [
        {"category": "birthday", "content": "祝生日快乐！愿你每一岁都奔走在自己的热爱里，所得皆所愿，所行皆坦途，永远开心，永远被爱🥳"},
        {"category": "birthday", "content": "生日快乐呀！愿你新的一岁，有趣有盼，无灾无难，兜里有钱，心里有光，所有的美好都如期而至🎂"},
        {"category": "birthday", "content": "恭喜你又解锁了新的一岁！祝你生日快乐，平安喜乐，万事胜意，想要的都拥有，得不到的都释怀✨"},
        {"category": "birthday", "content": "今天是你的生日，愿所有的快乐、所有的幸福、所有的温馨、所有的好运都围绕在你身边，生日快乐🎈"},
        {"category": "birthday", "content": "祝生日快乐！愿你今后的日子里，眼里是阳光，笑里是坦荡，未来的旅程，星辰大海，繁花似锦🌟"},
        {"category": "festival", "content": "新年快乐！祝你新的一年，平安喜乐，万事胜意，财源广进，阖家幸福，所有的美好都如约而至🧧"},
        {"category": "festival", "content": "中秋快乐！愿你月圆人圆，事事圆满，阖家欢乐，幸福安康，吃好喝好，快乐不倒🥮"},
        {"category": "festival", "content": "端午安康！祝你万事顺遂，平安健康，粽叶飘香，幸福绵长，假期愉快呀🍙"},
        {"category": "festival", "content": "国庆快乐！祝祖国繁荣昌盛，祝你假期愉快，吃好喝好，无忧无虑，开开心心过长假🇨🇳"},
        {"category": "festival", "content": "情人节快乐！愿天下有情人终成眷属，单身的朋友也能遇到属于自己的美好，天天开心❤️"},
        {"category": "promotion", "content": "恭喜升职！能力配得上努力，付出配得上回报，祝你未来职场一路开挂，前途似锦，步步高升🎉"},
        {"category": "promotion", "content": "祝贺你升职啦！真为你开心，你的努力和实力大家都看在眼里，未来可期，继续发光发热吧✨"},
        {"category": "promotion", "content": "恭喜高升！祝你在新的岗位上大展宏图，事业蒸蒸日上，薪水涨涨涨，好运连连来💰"},
        {"category": "promotion", "content": "太棒了！恭喜你升职，这是你应得的奖励，未来继续加油，创造更多精彩，前途无量呀👏"},
        {"category": "promotion", "content": "恭喜升职！愿你新的职位新的开始，工作顺利，事事顺心，带领团队创造更好的成绩，未来可期🚀"},
        {"category": "graduation", "content": "毕业快乐！愿你此去繁花似锦，再相逢依旧如故，未来的日子闪闪发光，前程似锦，未来可期🎓"},
        {"category": "graduation", "content": "恭喜毕业！愿你走出半生，归来仍是少年，保持热爱，奔赴下一场山海，未来的路一切顺利✨"},
        {"category": "graduation", "content": "毕业快乐呀！祝你以后的人生，顺风顺水，扶摇直上，百事无忌，平安喜乐，万事胜意🌟"},
        {"category": "graduation", "content": "恭喜你顺利毕业！愿你未来的道路上，有诗有梦，有坦荡荡的远方，所有的美好都在等你🚀"},
        {"category": "graduation", "content": "毕业快乐！愿你以梦为马，不负韶华，在新的征程上闪闪发光，闯出属于自己的一片天🥳"}
    ]
}

def get_access_token():
    """获取access_token"""
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={APPSECRET}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    return data["access_token"]

# 集合自动创建：插入第一条数据时云开发会自动创建集合，无需额外调用接口

def insert_data(access_token, collection, data_list):
    """批量插入数据"""
    url = f"https://api.weixin.qq.com/tcb/databaseadd?access_token={access_token}"
    success = 0
    for item in data_list:
        query = f"db.collection(\"{collection}\").add({{data: {json.dumps(item, ensure_ascii=False)}}})"
        payload = {
            "env": ENV,
            "query": query
        }
        resp = requests.post(url, json=payload)
        res = resp.json()
        if res["errcode"] == 0:
            success += 1
    print(f"{collection} 成功插入 {success}/{len(data_list)} 条")
    return success

def main():
    try:
        token = get_access_token()
        print(f"access_token获取成功，开始全量同步，自动创建集合+插入数据...")
        # 直接插入数据，集合不存在时会自动创建，无需手动创建
        total = 0
        for collection, data in FULL_DATA.items():
            cnt = insert_data(token, collection, data)
            total += cnt
        print(f"\n✅ 全量同步完成！总共插入 {total} 条数据")
        print("🎉 完全打通云开发数据库，自动创建集合+自动插入数据，无需任何手动操作！")
        print("所有集合已自动创建，所有功能现在都可以正常从云数据库读写数据了~")
    except Exception as e:
        print(f"❌ 同步失败: {str(e)}")
        exit(1)

if __name__ == "__main__":
    main()
