numbers = [1,2,3]

def Sum(numbers):
    if not numbers:
        return "Erreur, vous n'avez pas mis de nombres"  
    
    for i in numbers:
        if type(i) not in [int, float]:
            return "Erreur, vous n'avez pas mis que des nombres"

    if len(numbers) == 1:
        return numbers[0]
    
    return numbers[0] + Sum(numbers[1:])

result = Sum(numbers)

print(result)