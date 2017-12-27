def describe_pet(animal_type, pet_name='laoda'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# 根据位置信息传递实参的时候，必须保证顺序的正确性
describe_pet("hamster", "harry")
describe_pet("dog", 'EdWard')

# 使用关键字参数，必须使用正确的形参名字
describe_pet(pet_name='potter', animal_type='dog')
describe_pet(animal_type='Cat', pet_name='BigOne')
describe_pet('pig')
describe_pet('pig', 'bigpig')