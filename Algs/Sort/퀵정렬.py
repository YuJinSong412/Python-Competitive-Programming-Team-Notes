#정렬 알고리즘 중에 가장 많이 사용되는 알고리즘
#기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작 
#피벗 = 기준  : 리스트에서 첫 번째 데이터를 피벗으로 정하는 경우가 가장 대표적이다. 
# 평균 : O(NlogN)


# 1. 피벗 설정
# 2. 왼쪽에서부터 피벗보다 더 큰 데이터 찾기
# 3. 오른쪽에서부터 피벗보다 작은 데이터 찾기 
# 4. 큰 데이터와 작은 데이터의 위치를 서로 교환
# 1~4번의 과정을 반복


array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    pivot = start #0
    left = start + 1 #1 ->2
    right = end#9 ->8

    while left <= right:
        #피벗보다 큰 데이터를 찾을 때까지 반복 
        while left <= end and array[pivot] >= array[left]:
            left += 1
        
        #피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[pivot] <= array[right]:
            right -= 1
        if left > right: #엇갈렸다면 작은 데이터와 피벗을 교체 
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

        print("rig", right)
        print("--")
    quick_sort(array, start, right-1)
    quick_sort(array,right+1, end) 


quick_sort(array, 0, len(array)-1)
print(array)



#파이썬의 장점을 살린 퀵 정렬 소스코드
def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트 

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))