calls = 0

def count_calls(func):
    def wrapper(*args, **kwargs):
        global calls
        calls += 1
        return func(*args, **kwargs)
    return wrapper

@count_calls
def string_info(string):
    long = len(string)
    upper_case = string.upper()
    lower_case = string.lower()

    return long, upper_case, lower_case

@count_calls
def is_contains(string, list_to_search):
    for item in list_to_search:
        if item == string:
            return "Строка найдена в списке"
    return "Строка не найдена в списке"


print("Пример использования:")
test_string = "Hello World!"
list_of_words = ["hello", "world", "python"]
print(string_info(test_string))
print(string_info('oK'))
print(is_contains(test_string, list_of_words))
print(calls)
