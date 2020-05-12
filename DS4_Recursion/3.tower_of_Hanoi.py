'''
leetCode  面试题08.06 汉诺塔问题
在经典汉诺塔问题中，有 3 根柱子及 N 个不同大小的穿孔圆盘，盘子可以滑入任意一根柱子。一开始，所有盘子自上而下按升序依次套在第一根柱子上(即每一个盘子只能放在更大的盘子上面)。移动圆盘时受到以下限制:
(1) 每次只能移动一个盘子;
(2) 盘子只能从柱子顶端滑出移到下一根柱子;
(3) 盘子只能叠在比它大的盘子上。

请编写程序，用栈将所有盘子从第一根柱子移到最后一根柱子。

递归：
1 找出最基础部分
2 无限向着最基础的部分靠近
3 递归函数

第一步：找出最基础的部分;假设 N=5 （1,2,3号杆）最初都在1号杆上

1号5 借助C号移4个到2号  剩1到3号 （A:1   B:4   C:0）
2号4 借助A号移3个到3号  剩1到3号 （A:1   B:0   C:4）
     借助B号移2个到X号
     借助x号移1个到X号


fromPole 从哪个杆
withPole 借助哪个杆
num      移动多少个
toPole   到哪个杆
move(num,fromPloe,withPloe,toPloe)

'''

def move(num,fromPloe,withPloe,toPloe):
    if num>1:
        move(num-1,fromPloe,withPloe,toPloe)
        # 移动盘子
        moveDisk(fromPloe,toPloe)
        move(num-1,withPloe,fromPloe,toPloe)


def moveDisk(fromPloe,toPloe):
    print("移动盘子从",fromPloe,"到",toPloe)

move(5,"A","B","C")