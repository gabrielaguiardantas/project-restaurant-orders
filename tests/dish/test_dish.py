from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Restriction, Ingredient
import pytest


# Req 2
def test_dish():
    dish_example = Dish("baião de dois", 59.90)
    dish_example2 = Dish("filé à Osvaldo Aranha", 89.99)
    dish_example3 = Dish("baião de dois", 59.90)

    # testando o método de hashes
    assert hash(dish_example) == hash(dish_example3)
    assert hash(dish_example) != hash(dish_example2)

    # testando as igualdades (acionam o método __eq__ automaticamente)
    assert dish_example == dish_example3
    assert dish_example != dish_example2

    # testando a captura e asserção do atributo name
    assert dish_example.name == "baião de dois"

    # testando o método de reprodução em string do objeto
    assert repr(dish_example) == "Dish('baião de dois', R$59.90)"

    # testando erro ao instanciar com 2º atributo de tipo ou valor inválido
    with pytest.raises(TypeError):
        Dish("filé ao tornedor", "50")
    with pytest.raises(ValueError):
        Dish("filé ao tornedor", -34)

    # testando se o método abaixo adiciona um ingrediente a receita
    dish_example2.add_ingredient_dependency(Ingredient("carne"), 2)
    assert dish_example2.recipe.get(Ingredient("carne")) == 2

    # testando se retorna um dicionário com todos os ingredientes
    assert dish_example2.get_ingredients() == {Ingredient("carne")}

    # testando se ele linka corretamente o ingrediente com suas restrições
    assert dish_example2.get_restrictions() == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }
