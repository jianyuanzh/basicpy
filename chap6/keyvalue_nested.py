
# 字典列表
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 30个外星人
multi_aliens = []
for i in range(0, 30):
    tmp_alien = {
        'index': i,
        'color': 'red',
        'pos_x': 50,
        'pos_y': 10}
    multi_aliens.append(tmp_alien)

for alien in multi_aliens:
    print(alien)
