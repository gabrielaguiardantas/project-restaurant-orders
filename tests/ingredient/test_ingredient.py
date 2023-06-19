from src.models.ingredient import (
    Ingredient,
    Restriction,
)  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_example = Ingredient("ovo")
    ingredient_example2 = Ingredient("queijo")
    ingredient_example3 = Ingredient("ovo")

    # testando as hashes
    assert hash(ingredient_example) == hash(ingredient_example3)
    assert hash(ingredient_example) != hash(ingredient_example2)

    # testando as igualdades (acionam o método __eq__ automaticamente)
    assert ingredient_example == ingredient_example3
    assert ingredient_example3 != ingredient_example2

    # testando a captura e asserção do atributo name
    assert ingredient_example.name == "ovo"

    # testando o método de reprodução em string do objeto
    assert repr(ingredient_example) == "Ingredient('ovo')"

    # testando se encontra as restrições corretas para o ingrediente passado
    assert ingredient_example.restrictions == {Restriction.ANIMAL_DERIVED}
