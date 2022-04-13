import sys #프롬프트 파라미터를 받기 위해서 sys 선언
import re #특수문자를 제거하기위해 re선언
from collections import defaultdict #dict 선언하기 위함
from collections import OrderedDict #dict를 정렬하기 위함

file_name = sys.argv[1] #file 이름 받기
param_num = int(sys.argv[2]) #parameter number를 string에서 int로 바꾸기
word_count = defaultdict(lambda: 0)

with open(file_name, 'r') as file: #파일을 읽기 전용으로 open
    temp = file.readlines() #한줄씩 자르기


for i in temp: #각 줄의 index[0]부터 끝까지 돌리기 위해 for문 선언
    delete_text = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', i) # 특수문자 제가
    temp = delete_text.split() # white space 를 기준으로 list만들기
    for j in temp:
        word_count[j] += 1

count_sorted = OrderedDict(sorted(word_count.items(), key = lambda t : t[1], reverse = True)) #reverse = true를 통해 내림차순 정렬
#for a, b in count_sorted.items():
 #   print(a, b)

ct = 0 #param_num만큼 반복문 돌았는지 확인하기 위해 선언
print(sys.argv[0],sys.argv[1],sys.argv[2])
for k, v in count_sorted.items(): #dict의 key , value 값을 받기위해 k ,v선언
    if(ct != param_num):
        print(k.ljust(10), str(v).rjust(10)) #ljust rjust 정렬 출력
        ct += 1
    else:
        break