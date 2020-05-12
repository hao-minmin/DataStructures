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


'''
迷宫:参考LeetCode 1210 题 穿过迷宫的最少移动次数
1.从初始位置尝试向上走一步，从此开始递归
2.如果上面走不通则尝试走下面，再开始递归
3.上下都不通，走左边，再开始递归
4.上下左都不通，走右边，再开始递归


四种基本情况
1，碰到“墙壁”方格被占用无法通行
2，方格被访问过，未避免陷入循环不在此位置继续寻找
3 碰到边缘 表示成功
4 四个方向探索失败游戏失败

turtle 

__init__  用来读取迷宫的数据 初始化迷宫内部  并找到精灵的初始位置

draw_maze 用来在屏幕上绘制迷宫

update_position  用来更新迷宫的状态和游戏精灵的位置

is_exit 用来判断当前位置是否是出口




'''
# 迷宫的地图  从txt 文件中获取  地图是一个只包含：+ 空格的文件

# turtle  GUI 库 绘制地图
# 用到的绘制迷宫的符号: + 空格

class Maze():
    def __init__(self,mazeFileName):
        rowsInMaze = 0
        columnsMaze = 0
        self.mazeList = []

        mazeFile = open(mazeFileName,"r")
        for line in mazeFile:
            rowList = []
            col = 0
            for ch in line[:-1]:
                rowList.append(ch)
                if ch=="Q":
                    self.startRow = rowsInMaze
                    self.starCol = col
                col = col+1
            rowsInMaze = rowsInMaze+1
            self.mazeList.append(rowList)
            columnsMaze = len(rowList)
        self.rowsInMaze = rowsInMaze
        self.columnsInMaze=columnsMaze
        self.xTranslate = columnsMaze
        self.yTranslate = rowsInMaze
        self.t = Turtle()
        setup(with=600,height = 600)
        setworldcoordinates(-(columnsMaze-1)/2-.5,
                            -(rowsInMaze-1)/2-.5,
                            (columnsMaze-1)/2+.5,
                            (columnsMaze-1)/2+.5)
        





