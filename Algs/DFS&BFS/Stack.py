#FILO구조

stack = []
# 삽입(5) - 삽입(2) - 삽입(3) - 삭제() - 삽입(4) - 삭제() 
stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(4)
stack.pop()

print(stack)
#[5,2]