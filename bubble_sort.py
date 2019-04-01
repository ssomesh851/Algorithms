#bubbule sort algorithm

def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
list = [25,0,1,35,5,6]
bubble_sort(list)
print(list)
