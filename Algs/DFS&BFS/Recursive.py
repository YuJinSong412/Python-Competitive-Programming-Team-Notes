# 재귀 함수는 함수가 언제 끝날지, 종료 조건을 꼭 명시해야 한다.
# 재귀 함수는 내부적으로 스택 자료구조와 동일하다. 
# 스택 자료구조를 활용해야 하는 상당수 알고리즘은 재귀 함수를 이용해서 간편하게 구현될 수 있다. DFS가 대표적.


def recFun(i):
    if i == 5: 
        return
    print(i,'번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출한다.')
    recFun(i+1)
    print(i,'번째 재귀 함수를 종료한다.')

recFun(1)