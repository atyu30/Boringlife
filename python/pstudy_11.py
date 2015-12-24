#!/usr/bin/env python
# encoding: utf-8

'''
【程序11】
题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
　　　后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
1.程序分析：　兔子的规律为数列1,1,2,3,5,8,13,21....
2.程序源代码：
main()
{
long f1,f2;
int i;
f1=f2=1;
for(i=1;i<=20;i++)
　{ printf("%12ld %12ld",f1,f2);
　　　if(i%2==0) printf("\n");/*控制输出，每行四个*/
　　　f1=f1+f2; /*前两个月加起来赋值给第三个月*/
　　　f2=f1+f2; /*前两个月加起来赋值给第三个月*/
　}
}
'''
f1 = 1
f2 = 1
for i in range(1,21):
    print '%12d %12d' % (f1,f2)
    if (i % 2) == 0:
        print ''
    f1 = f1 + f2
    f2 = f1 + f2
    
