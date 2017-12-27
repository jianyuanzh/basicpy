# 使用任意数量的关键字实参
def build_profile(first, last, **userinfo):
    # 创建一个字段，其中包含我们知道的一切用户信息
    profile = {'first_name': first, 'last_name': last}

    for key, value in userinfo.items():
        profile[key] = value
    return profile

user_profile = build_profile('Vincent', 'Zhang', weight=168, location='Chengdu', gender='male')

print(user_profile)
