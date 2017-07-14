menu = {}
with open('Recipes.txt', encoding='UTF-8') as f:
    while True:
        try:
            # Название блюда
            name = f.readline().strip('\n')

            # Количесво блюд
            number_ingredients = int(f.readline().strip('/n'))
            menu[name] = []
            # Итерирование по ингредиентам
            for count in range(number_ingredients):
                ingredients = {}
                # Создание словаря ингредиента
                exec("ingredients['ingredient_name'] = '{0}'\n\
ingredients['quantity']  = '{1}'\n\
ingredients['measure']  = '{2}'".format(*f.readline().strip('\n').split(' | ')))
                # Добавление ингредиента в меню
                menu[name].append(ingredients)
            f.readline()
        except ValueError:
            break


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in menu[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] = int(new_shop_list_item['quantity']) * person_count
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}\n'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'],
                                  shop_list_item['measure']))


def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    print('Блюда: ', *[dish.title()+', ' for dish in menu], end='.')
    print()
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()
