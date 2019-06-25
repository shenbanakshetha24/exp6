import sys
yer=int(input())
if yer%400==0 or (yer%4==0 and yer%100!=0):
 print('Yes')
else:
 print('No')
