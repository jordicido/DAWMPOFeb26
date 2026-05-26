# Un programa que dada una lista de numeros, devuelva su máximo y mínimo

def maxmin(nums):
    """
    Función que devuelve el máximo y mínimo de una lista

    Args:
        nums: Lista de números desordenada
    
    Returns:
        Máximo y minimo de la lista
    """
    x = nums[0]
    for i in range(len(nums)):
        if nums[i] > x:
            x = nums[i]
    
    y = nums[0]
    for i in range(len(nums)):
        if nums[i] < y:
            y = nums[i]
    
    return x, y

lista = [10, 3, 24, 1, 25, 52, -10]
x, y = maxmin(lista)
print(f"Maximo es {x} y minimo es {y}")