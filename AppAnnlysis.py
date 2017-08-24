import MyExcelUtil
import matplotlib.pyplot as plt
#获取数据的所有列并转为数组
def get_all_col_val_as_array(colnum):
	fatherArray=[]
	i=0
	while i<colnum:
		array = MyExcelUtil.get_colvalue(i)
		fatherArray.append(array)
		i += 1
	return fatherArray

#获取到当天为止用过的用户数
def get_everyday_user(fatherArray):
	#获取天数
	cols=len(fatherArray)
	everyDayUserArray=[]
	everyDayUserArrayCount=[]
	#第一天的数据其实就为第一列
	everyDayUserArray.append(fatherArray[0])
	i=0
	while i<cols-1:

		tempArray=everyDayUserArray[i]
		#print(len(tempArray))
		everyDayUserArrayCount.append(len(tempArray))
		#拿后一天的数据与前面几天的用户做比较
		for val in fatherArray[i+1]:
			if val not in tempArray:
				tempArray.append(val)
		everyDayUserArray.append(tempArray)
		i+=1
	return  everyDayUserArrayCount

#获取每天新加入的用户数
def get_everyday_increase(countArray):
	increaseArray=[]
	increaseArray.append(0)
	i=0
	while i<len(countArray)-1:
		increaseArray.append(countArray[i+1]-countArray[i])
		i+=1
	return increaseArray



def main():
	group_labels = []
	x_val = []
	colnum = MyExcelUtil.get_colnum(0)
	father = get_all_col_val_as_array(colnum)
	#print(len(father))
	count=get_everyday_user(father)
	everyday_all_count=count
	everday_increase=get_everyday_increase(count)
	print(everyday_all_count)
	print(everday_increase)
	for num in everday_increase:
		print(num)
	j=0
	while j<155:
		temp=j+1
		group_labels.append(str(temp))
		x_val.append(temp)
		j+=1
	plt.title("exp_count".encode("utf8"))
	plt.xlabel("date")
	plt.ylabel("usercount".encode("utf8"))
	plt.plot(x_val, everyday_all_count, 'r', label="至今用户总量")
	plt.plot(x_val, everday_increase, 'b', label="new_user_for_one_day")
	plt.grid()
	plt.show()

if __name__=="__main__":
    main()