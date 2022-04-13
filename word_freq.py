import sys
import re
from collections import defaultdict
from collections import OrderedDict

file_name = sys.argv[1]
param_num = int(sys.argv[2])
word_count = defaultdict(lambda: 0)

with open(file_name, 'r') as file:
    temp = file.readlines() #한줄씩 자르기


for i in temp: #각 줄의 index[0]부터 끝까지 돌리기 위해 for문 선언
    delete_text = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', i)
    str = delete_text.split()
    ct = 0
    for j in str:
        word_count[j] += 1

count_sorted = OrderedDict(sorted(word_count.items(), key = lambda t : t[1], reverse = True))
for a, b in count_sorted.items():
    print(a, b)

ct = 0
print("---------------------")
for k,v in count_sorted.items():
    if(ct != param_num):
        print(k, v)
        ct += 1
    else:
        break