import numpy as np

data = np.random.rand(2,3)#生成俩行三列的随机多维数组
print（type(data))#类型 <class 'numpy.ndarray'>
print('维度个数', data.ndim)
print('各维度大小: ', data.shape)
print('数据类型: ', data.dtype)
# list转换为 ndarray
l = range(10)
data = np.array(l)
# 嵌套序列转换为ndarray
l2 = [range(10), range(10)]
data = np.array(l2)
zeros_arr = np.zeros((3,4))#生成三行四列全0数组
ones_arr = np.ones((2, 3))#生成俩行三列全1数组
empty_int_arr = np.empty((3, 3), int)#未初始的随机值 可指定数据类型
print(np.arange(10))#类似range()
zeros_float_arr = np.zeros((3, 4), dtype=np.float64)#三行四列全0数组 类型float64
print(zeros_float_arr.dtype)#打印数据类型 float64
zeros_int_arr = zeros_float_arr.astype(np.int32)# astype转换数据类型 float64→int32
arr = np.array([[1, 2, 3],[4, 5, 6]])#矢量与矢量运算
print(arr * arr)
print(arr + arr)
# 矢量与标量运算
print(1. / arr)
print(2. * arr)
#一组数组索引与列表索引相似
arr1 = np.arange(10)
print(arr1)
print(arr1[2:5])
#多组数组索引
arr2 = np.arange(12).reshape(3,4)
arr3 = np.arange(50)
np.reshape(arr3,(5,10))
print(arr2[1])#第二行
print(arr2[0:2, 2:])#前俩行的三四列
print(arr2[:, 1:3])#二三列
#[:]代表某个维度的数据
#条件索引 找出 data_arr 中 2015年后的数据
data_arr = np.random.rand(3,3)
print(data_arr)
year_arr = np.array([[2000, 2001, 2000],[2005, 2002, 2009],[2001, 2003, 2010]])
filtered_arr = data_arr[year_arr >= 2005]
print(filtered_arr)
# 多个条件(使用| &,而不是 or，and)
filtered_arr = data_arr[(year_arr <= 2005) & (year_arr % 2 == 0)]
print(filtered_arr)
#维度转换transpose(axis=0 列，axis=1 行)
arr = np.random.rand(2,3)
print(arr)
print(arr.transpose())#俩行三列转换成三行俩列
arr3d = np.random.rand(2,3,4)
print(arr3d)
print('----------------------')
print(arr3d.transpose((1,0,2))) #初始transpose(0,1,2)→ 3x2x4
#通用函数
np.ceil()#向上最接近的整数
np.floor#向下最接近的整数
np.rint#四舍五入
np.isnan#判断元素是否为NAN(NaN，是Not a Number的缩写)
#矢量版本的三元表达式 x if condition else y [np.where(condition,x,y)]
arr = np.random.randn(3,4)
print(arr)
np.where(arr > 0, 1, -1)
#统计
arr = np.arange(10).reshape(5,2)
print(arr)
print(np.sum(arr))#全部求和
print(np.sum(arr, axis=0))#列求和
print(np.sum(arr, axis=1))#行求和
#np.any np.all
arr = np.random.randn(2,3)
print(arr)
print(np.any(arr > 0))#全部满足条件
print(np.all(arr > 0))#至少有一个元素满足条件
#np.unique
arr = np.array([[1, 2, 1], [2, 3, 4]])
print(arr)
print(np.unique(arr))#找到唯一值并返回排序结果
