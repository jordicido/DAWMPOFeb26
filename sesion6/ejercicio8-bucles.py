'''
5
*****
** **
* * *
** **
*****

7
*******
**   **
* * * *
*  *  *
* * * *
**   **
*******

9
*********
**     **
* *   * *
*  * *  *
*   *   *
*  * *  *
* *   * *
**     **
*********
'''
numero = int(input("Introduce un número impar positivo\n"))

print("*"*numero)
for i in range(1, numero-1): 
    # i = 5
    fila = "*"
    # fila = "*"
    for j in range(1,numero-1):
        # j = 1
        if i == j or numero-1-i == j:
            fila += "*"
            # fila = "* "
        else:
            fila += " "
            # fila = "* "
    
    fila += "*"
    # fila = "*  *  *"
    print(fila)
    '''
    *******
    **   **
    * * * *
    *  *  *
    * * * *
    **   **
    '''
print("*"*numero)
'''
*******
**   **
* * * *
*  *  *
* * * *
**   **
*******
'''