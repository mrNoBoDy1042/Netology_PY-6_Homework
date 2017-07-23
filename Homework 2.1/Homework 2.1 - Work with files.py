################################################################################
# Task: Получить список меню из файла, спросить у пользователя количество человек
# и перечень блюд, подсчитать количество необходимых продуктов
################################################################################


################################################################################
# get_menu - получает список продуктов из файла recipes.txt
################################################################################
def get_menu():
    menu = {}
    with open('Recipes.txt', encoding='UTF-8') as f:
        while True:

            ################################################
            # Получаем название блюда
            ################################################
            name = f.readline().strip('\n')
            if name == "":
                break

            ################################################
            # Количество ингредиентов
            ################################################
            number_ingredients = int(f.readline().strip())
            menu[name] = []

            ################################################
            # Перебираем ингредиенты необходимые для блюда
            ################################################
            for count in range(number_ingredients):
                ingredients = {}

                ##################################################
                # Создание списка с информацией об ингредиенте
                #################################################
                ingredient_info = f.readline().strip('\n').split(' | ')

                ##################################################
                # Создание словаря ингредиента
                ##################################################
                ingredients['ingredient_name'] = ingredient_info[0]
                ingredients['quantity'] = ingredient_info[1]
                ingredients['measure'] = ingredient_info[2]

                ##################################################
                # Добавление ингредиентов текущего блюда в меню
                ##################################################
                menu[name].append(ingredients)

            #############################################
            # Чтение разделителя, разделяющий блюда
            #############################################
            f.readline()

    ###########################################
    # Вызов процедуры создания списка покупок
    ###########################################
    create_shop_list(menu)


def get_shop_list_by_dishes(dishes, person_count, menu):
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


def create_shop_list(menu):
    person_count = int(input('Введите количество человек: '))
    print('Блюда: ', *[dish.title()+', ' for dish in menu], end='.')
    print()
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, menu)
    print_shop_list(shop_list)

get_menu()
