# condition이 True 동안 동작
# while true: 
    # pass
# 풀기 : 5 구구단 결과 매번 출력
# num_virtual = 0
# while True : 
#     pass
#     num_virtual = num_virtual + 1
#     print("{} = num_virtual + 1".format(num_virtual))
#     if num_virtual >= 5:
#         pass
#     pass
# while 정지 1case with break 문 사용
# num_virtual = 0
# while True : 
#     pass
#     num_virtual = num_virtual + 1
#     print("{} = num_virtual + 1".format(num_virtual))
#     if num_virtual >= 5:
#         pass
#         break
#     pass
# 풀기 : 5 구구단 결과 매번 출력

# while 정지 2 case without break문 사용
num_virtual = 0
while num_virtual < 5 : 
    pass
    num_virtual = num_virtual + 1
    print("{} = num_virtual + 1".format(num_virtual))
    if num_virtual >= 5:
        pass
    pass
print("End Program!")