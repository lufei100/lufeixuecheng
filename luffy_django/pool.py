import redis

POOL = redis.ConnectionPool(host='192.168.2.129',port=6379)



arr = [3,5,8,7,8,10]
d = 2
ret = []
for k1,x in enumerate(arr):   #循环数组的值和索引
	arrl = arr[:]            #拷贝一份数据
	arrl[k1] = "xxx"
	for k2,y in enumerate(arr):
		if str(y).isdigit() and abs(y-x) == d:
			xx = set()
			xx.add(k2)
			xx.add(k1)
			if xx not in ret:
				ret.append(xx)
print(ret)
