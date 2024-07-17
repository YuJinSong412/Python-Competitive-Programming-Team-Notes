#특정한 데이터를 적절한 위치에 삽입한다는 뜻
#2번째 데이터부터 시작한다. 첫 번째 데이터는 그 자체로 정렬되어 있다고 판단하기 때문이다.
# # O(N^2) 

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)