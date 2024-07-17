#파이썬의 zip(), enumerate() 내장 함수로 for 루프 돌리기
nums = [1,4,9,10]
op = ['-', '*', '+']
for o, n in zip(op, nums[1:]):
    if o == "-" : print("o")

# 인덱스와 원소를 동시에 접근
for i, letter in enumerate(['A', 'B', 'C']):
    print(i, letter)
# ...
# 0 A
# 1 B
# 2 C

for i, h in enumerate(height,1):
    print(i,h)