import pytest


def python_string_slicer(str):
    if len(str) < 50 or "python" in str:
        return str
    else:
        return str[0:50]


def generate_id(val):
   return "params: {0}".format(str(val))


@pytest.fixture(scope="function", params=[("Короткая строка", "Короткая строка"), ("Длинная строка, не то чтобы прям "
"очень длинная, но достаточно для нашего теста, и в ней нет названия языка", "Длинная строка, не то чтобы прям очень "
"длинная, но"), ("Короткая строка со словом python", "Короткая строка со словом python"), ("Длинная строка, нам "
"достаточно будет для проверки, и в ней есть слово python", "Длинная строка, нам достаточно будет для проверки, и в "
"ней есть слово python")], ids=["len < 50", "len > 50", "len < 50 contains python", "len > 50 contains python"])
def param_fun_generated(request):
    return request.param


def test_python_string_slicer_generated(param_fun_generated):
    (input, expected_output) = param_fun_generated
    result = python_string_slicer(input)
    print("\nВходная строка: {0}\nВыходная строка: {1}\nОжидаемое значение: {2}\n".format(input, result, expected_output))
    assert result == expected_output


@pytest.mark.parametrize("x", [-1, 0, 1], ids=["negative", "zero", "positive"])
@pytest.mark.parametrize("y", [100, 1000], ids=["3 digit", "4 digit"])
def test_multiply_params(x, y):
    print(f"x: {x}, y:{y}")
    assert True
