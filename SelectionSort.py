#Selection Sort Program in Python
import time

def findMinIndex(data, start):  
    min_index = start  
    start += 1  
    while start < len(data):  
        if data[start] < data[min_index]:  
            min_index = start  
        start += 1  
    return min_index  
  
def selectionSort(data, drawData, timeTick):  
    i = 0  
    while i < len(data):  
        min_index = findMinIndex(data, i)  
        if i != min_index:  
            data[i], data[min_index] = data[min_index], data[i]
        drawData(data, ['green' if x == min_index or x== min_index+1 else 'red' for x in range(len(data))])
        i += 1  
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])

#data = [5, 2, 6, 7, 2, 1, 0, 3]  
  
#selectionSort(data)  
  
#for num in data:  
#    print(num, end=' ')