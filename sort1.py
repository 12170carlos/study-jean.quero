def list(array):
    length = len(array) - 1
    #bucle para los recorridos
    for i in range(0, length):
        #bucle para hacer las comparaciones
        for j in range(0, length):
            
            if array[j] > array[j + 1]:
                aux = array[j]
                array[j] = array[j + 1]
                array[j + 1] = aux
    return array
num = [2 ,7, 2, 1, 6, 3]
num1 =[2,4,3,2,1,0]
print("Antes de ordenar")
print(num, num1)
print("Después de ordenar")
print(list(num))
print(list(num1))
