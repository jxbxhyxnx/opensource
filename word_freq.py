import sys
import re
from collections import defaultdict
from collections import OrderedDict

file_name = sys.argv[1]
param_num = int(sys.argv[2])

with open(file_name, 'r') as file:
    temp = file.readlines() #한줄씩 자르기

