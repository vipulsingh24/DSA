

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'selectStock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER saving
#  2. INTEGER_ARRAY currentValue
#  3. INTEGER_ARRAY futureValue
#

def selectStock(saving, currentValue, futureValue):
    # Write your code here
    result = list(zip(currentValue, futureValue))
    result.sort(key = lambda x: x[1] / x[0], reverse=True)
    
    final = 0
    for c_val, f_val in result:
        if saving - c_val >= 0:
            final += f_val - c_val
            saving -= c_val
        else:
            break
    
    if final > 0:
        return final
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    saving = int(input().strip())

    currentValue_count = int(input().strip())

    currentValue = []

    for _ in range(currentValue_count):
        currentValue_item = int(input().strip())
        currentValue.append(currentValue_item)

    futureValue_count = int(input().strip())

    futureValue = []

    for _ in range(futureValue_count):
        futureValue_item = int(input().strip())
        futureValue.append(futureValue_item)

    result = selectStock(saving, currentValue, futureValue)

    fptr.write(str(result) + '\n')

    fptr.close()




""""


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'selectStock' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER saving
#  2. INTEGER_ARRAY currentValue
#  3. INTEGER_ARRAY futureValue
#

def selectStock(saving, currentValue, futureValue):
    # Write your code here
    dp = [0] * (saving + 1)
    n = len(currentValue)
    
    for i in range(1, n+1):
        weight = currentValue[i - 1]
        value = futureValue[i-1] + currentValue[i-1]
        
        j = saving
        while j >= weight:
            dp[j] = max(dp[j], dp[j-w] + value)
            j -= 1
        
        return dp[saving]
    
if __name__ == '__main__':

"""

