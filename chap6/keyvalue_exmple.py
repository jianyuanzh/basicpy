favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'vincent': 'java',
    'phil': 'python'
}

friends = ['phil', 'sarah', 'vincent']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages.get(name).title())
