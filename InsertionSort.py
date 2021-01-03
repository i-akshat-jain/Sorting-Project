#Insertion sort Implementation in Python:
# Function to do insertion sort
import time
def insertionSort(data, drawData, timeTick):
    for i in range(1, len(data)): # Traverse through 1 to len(data)
        key = data[i]
        j = i-1                     
        while j >= 0 and key < data[j] :
            data[j+1] = data[j]
            j -= 1
            drawData(data, ['green' if x == j or x== j+1 else 'red' for x in range(len(data))])
        data[j+1] = key 
        time.sleep(timeTick)
    drawData(data, ['green' for x in range(len(data))])


""" Driver code to test above
data = [12, 11, 13, 5, 6] 
insertionSort(data) 
for i in range(len(data)): 
    print (data[i]) """