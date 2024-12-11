def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1,len(arr)):
    if(arr[i]<smallest):
      smallest = arr[i]
      smallest_index = i
  return smallest_index

def selectionSort(arr):
  newArr=[]
  for i in range(len(arr)): # range():创建一个从0到len(arr)-1的序列
    smallest=findSmallest(arr)
    newArr.append(arr.pop(smallest)) # append():向列表末尾添加元素; pop():删除指定位置的元素，并返回该元素
  return newArr

print(selectionSort([5,3,6,2,10]))