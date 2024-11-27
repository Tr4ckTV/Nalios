def FizzBuzz(a, b, dictionnaire):
    for i in range(a, b):
        result = ""
        for key, value in dictionnaire.items():
            if i % int(key) == 0:
                result += value
        print(result if result else i)

FizzBuzz(1, 101, {'3': 'Fizz', '5': 'Buzz'})