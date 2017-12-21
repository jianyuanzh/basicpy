
name_email = {'vincent': 'vincent@lm.com', 'jerry': 'jerry@lm.com', 'number': 1234}

print(name_email)
print(name_email['vincent'])
print(name_email['number'])

# add new key-value pairs
name_email['rob'] = 'rob@lm.cc'
name_email['jeff'] = 'jeff@lm.cc'

print(name_email)

# 删除键值对

del name_email['jerry']
print(name_email)
