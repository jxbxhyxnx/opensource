import sys
import re
from collections import defaultdict
from collections import OrderedDict

file_name = sys.argv[1]
param_num = int(sys.argv[2])

with open(file_name, 'r') as file:
    temp = file.readlines() #한줄씩 자르기

for i in temp: #각 줄의 index[0]부터 끝까지 돌리기 위해 for문 선언
    delete_text = re.sub('[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`\'…》\”\“\’·]', ' ', i)
    str = delete_text.split()