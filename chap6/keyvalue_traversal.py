favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

# 使用sorted()保证遍历key-value的顺序
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the pll.")

# 遍历值，但是这种方法未考虑重复问题
for val in favorite_languages.values():
    print(val + ' is mentioned')

# 遍历值，保证不重复
for val in set(favorite_languages.values()):
    print(val + ' is mentioned')
