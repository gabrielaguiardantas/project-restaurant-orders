import csv

from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str):
        self.dishes = set()
        with open(file=source_path, encoding="utf-8") as file:
            menu_reader = csv.DictReader(file, delimiter=",", quotechar='"')

            # converto em lista para achar o primeiro prato
            list_menu_reader = [line for line in menu_reader]

            # adiciono o primeiro prato e seu primeiro ingrediente
            current_dish = Dish(
                list_menu_reader[0]["dish"],
                float(list_menu_reader[0]["price"]),
            )
            current_dish.add_ingredient_dependency(
                Ingredient(list_menu_reader[0]["ingredient"]),
                int(list_menu_reader[0]["recipe_amount"]),
            )
            self.dishes.add(current_dish)

            # agora itero sobre os demais,
            # adicionando ingrediente caso seja o mesmo prato do primeiro
            # caso contrário, crio um novo prato, adiciono ingredientes
            # e modifico o atual para o novo
            for line in list_menu_reader[1:]:
                if current_dish.name == line["dish"]:
                    current_dish.add_ingredient_dependency(
                        Ingredient(line["ingredient"]),
                        int(line["recipe_amount"]),
                    )
                else:
                    new_dish = Dish(line["dish"], float(line["price"]))
                    new_dish.add_ingredient_dependency(
                        Ingredient(line["ingredient"]),
                        int(line["recipe_amount"]),
                    )
                    self.dishes.add(new_dish)
                    current_dish = new_dish
