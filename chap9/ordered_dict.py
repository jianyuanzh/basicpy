from collections import OrderedDict

favorite_languages = OrderedDict()


favorite_languages['jen'] = 'java'
favorite_languages['ben'] = 'python'
favorite_languages['jianyuan'] = 'c'


for name, lang in favorite_languages.items():
    print(name.title() + "'s favorite language is " + lang.title())