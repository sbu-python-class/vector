import vector


def test_add():
    v1 = vector.Vector(1, 2)
    v2 = vector.Vector(2, 3)

    assert v1 + v2 == vector.Vector(3, 5)
