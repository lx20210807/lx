# 九九乘法表
for i in range(1, 10):  #range()函数取前不取后
    print("")  #为了使后面换行
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')  #\t是使其排列整齐
