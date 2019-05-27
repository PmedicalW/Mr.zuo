"""
逻辑处理模块
"""
class GameCoreController:
    def __init__(self,map):
        self.map=map


    # 1.将零元素移动到末尾

    def zero_to_end(self,list_target):
        for i in range(len(list_target) - 1, -1, -1):
            if list_target[i] == 0:
                del list_target[i]
                list_target.append(0)

    # 练习２：定义合并函数
    def merge(self,list_target):
        self.zero_to_end(list_target)
        # [2,2,0,0] --> [4,0,0,0]       [4,0,2,0]
        for i in range(len(list_target) - 1):
            # 相邻且相同
            if list_target[i] == list_target[i + 1]:
                list_target[i] +=list_target[i + 1]
                list_target[i + 1] = 0
        self.zero_to_end(list_target)

    # 练习３：将二维列表，以表格的格式显示在控制台中　　
    def print_map(self):
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                print(self.map[r][c], end=" ")
            print()

    # print_map(list01)

    # 练习４.移动函数
    def move_left(self):
        # 获取第行
        for r in range(len(self.map)):
            # 从左往右获取行
            # 交给merge进行合并
            self.merge(self.map[r])

    def move_right(self):
        # 获取第行
        for r in range(len(self.map)):
            # 从右往左获取行
            # 交给merge进行合并
            list_merge = self.map[r][::-1]
            self.merge(list_merge)
            self.map[r][::-1] = list_merge


    def move_up(self):
        for c in range(4):
            list_merge = []
            #  从上往下获取列  形成一维列表
            for r in range(4):  # 0   1  2    3
                list_merge.append(self.map[r][c])
            # 交给合并方法
            self.merge(list_merge)
            # 将合并后的结果list_merge，还原给原二维列表
            for r in range(4):  # 0   1  2    3
                self.map[r][c] = list_merge[r]


    def move_down(self):
        for c in range(4):
            list_merge = []
            #  从上往下获取列  形成一维列表（从左到右）
            for r in range(3, -1, -1):  # 3   2    1   0
                list_merge.append(self.map[r][c])
            # 交给合并方法
            self.merge(list_merge)
            # 将合并后的结果list_merge（从左到右），还原给原二维列表
            for r in range(3, -1, -1):  # 3 2 1 0
                self.map[r][c] = list_merge[3 - r]  # 0 1 2 3


list01 = [
    [2, 0, 4, 2],
    [2, 2, 0, 0],
    [2, 0, 4, 4],
    [4, 0, 0, 2],
]
g01=GameCoreController(list01)
g01.zero_to_end(list01)
g01.print_map()
g01.move_up()
