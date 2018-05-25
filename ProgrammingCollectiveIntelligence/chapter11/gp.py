#-*- coding:utf-8 -*-

from random import random, randint, choice
from copy import deepcopy
from math import log

## 在Python中表现树
class fwrapper:
    def __init__(self, function, childcount, name):
        self.function = function
        self.childcount = childcount
        self.name = name


class node:
    def __init__(self, fw, children):
        self.function = fw.function
        self.name = fw.name
        self.children = children

    def evaluate(self, inp):
        results = [n.evaluate(inp) for n in self.children]
        return self.function(results)

    def display(self, indent=0):
        print(((' ' * indent) + self.name))
        for c in self.children:
            c.display(indent+1)


class paramnode:
    def __init__(self, idx):
        self.idx = idx

    def evaluate(self, inp):
        return inp[self.idx]

    def display(self, indent=0):
        print(('%sp%d' % (' ' * indent, self.idx)))


class constnode:
    def __init__(self, v):
        self.v = v

    def evaluate(self, inp):
        return self.v

    def display(self, indent=0):
        print(('%s%d' % (' ' * indent, self.v)))


addw = fwrapper(lambda l:l[0] + l[1], 2, 'add')
subw = fwrapper(lambda l:l[0] - l[1], 2, 'subtract')
mulw = fwrapper(lambda l:l[0] * l[1], 2, 'multiply')

def iffunc(l):
    if l[0] > 0:
        return l[1]
    else:
        return l[2]

ifw = fwrapper(iffunc, 3, 'if')

def isgreater(l):
    if l[0] > l[1]:
        return 1
    else:
        return 0

gtw = fwrapper(isgreater, 2, 'isgreater')

flist = [addw, mulw, ifw, gtw, subw]

def exampletree():
    return node(ifw, [
                        node(gtw, [paramnode(0), constnode(3)]),
                        node(addw, [paramnode(1), constnode(5)]),
                        node(subw, [paramnode(1), constnode(2)]),
                        ]
               )


## 构造初始种群
def makerandomtree(pc, maxdepth=4, fpr=0.5, ppr=0.6):
    if random() < fpr and maxdepth > 0:
        f = choice(flist)
        children = [makerandomtree(pc, maxdepth-1, fpr, ppr) for i in range(f.childcount)]
        return node(f, children)
    elif random() < ppr:
        return paramnode(randint(0, pc-1))
    else:
        return constnode(randint(0, 10))

# 一个简单的数学测试
def hiddenfunction(x, y):
    return x ** 2 + 2 * y + 3 * x + 5

def buildhiddenset():
    rows = []
    for i in range(200):
        x = randint(0, 40)
        y = randint(0, 40)
        rows.append([x, y, hiddenfunction(x, y)])
    return rows

# 衡量程序的好坏
def scorefunction(tree, s):
    dif = 0
    for data in s:
        v = tree.evaluate([data[0], data[1]])
        dif += abs(v-data[2])
    return dif

# 对程序进行变异
def mutate(t, pc, probchange=0.1):
    if random() < probchange:
        return makerandomtree(pc)
    else:
        result = deepcopy(t)
        if isinstance(t, node):
            result.children = [mutate(c, pc, probchange) for c in t.children]
        return result

# 交叉
def crossover(t1, t2, probswap=0.7, top=1):
    if random() < probswap and not top:
        return deepcopy(t2)
    else:
        result = deepcopy(t1)
        if isinstance(t1, node) and isinstance(t2, node):
            result.children = [crossover(c, choice(t2.children), probswap, 0)
                                for c in t1.children]
        return result

# 构筑环境
def evolve(pc, popsize, rankfunction, maxgen=500,
        mutationrate=0.1, breedingrate=0.4, pexp=0.7, pnew=0.05):
    # 返回一个随机数，通常是一个较小的数
    # pexp的取值越小，我们得到的随机数就越小
    def selectindex():
        return int(log(random()) / log(pexp))

    # 创建一个随机的初始种群
    population = [makerandomtree(pc) for i in range(popsize)]
    for i in range(maxgen):
        scores = rankfunction(population)
        print((scores[0][0]))
        if scores[0][0] == 0:
            break

        # 总能得到两个最优的程序
        newpop = [scores[0][1], scores[1][1]]

        # 构造下一代
        while len(newpop) < popsize:
            if random() > pnew:
                newpop.append(mutate(
                            crossover(scores[selectindex()][1],
                                scores[selectindex()][1],
                                probswap=breedingrate),
                            pc, probchange=mutationrate))
            else:
                # 加入一个随机节点，以增加种群的多样性
                newpop.append(makerandomtree(pc))

        population = newpop
    scores[0][1].display()
    return scores[0][1]

def getrankfunction(dataset):
    def rankfunction(population):
        scores = [(scorefunction(t, dataset), t) for t in population]
        scores.sort()
        return scores
    return rankfunction

# 一个简单的游戏
def gridgame(p):
    # 游戏区域的大小
    max = (3, 3)

    # 记住每位玩家的上一步
    lastmove = [-1, -1]

    # 记住玩家的位置
    location = [[randint(0, max[0]), randint(0, max[1])]]

    # 将第二位玩家放在离第一位玩家足够远的地方
    location.append([(location[0][0]+2) % 4, (location[0][1]+2) % 4])

    # 打成平局前的最大移动步数为50
    for o in range(50):

        # 针对每位玩家
        for i in range(2):
            locs = location[i][:] + location[1-i][:]
            locs.append(lastmove[i])
            move = p[i].evaluate(locs) % 4

            # 如果在一行中朝同一个方向移动了两次，就判定为输
            if lastmove[i] == move:
                return 1-i
            lastmove[i] = move
            if move == 0:
                location[i][0] -= 1
                # 限制游戏区域
                if location[i][0] < 0:
                    location[i][0] = 0
            if move == 1:
                location[i][0] += 1
                if location[i][0] > max[0]:
                    location[i][0] = max[0]
            if move == 2:
                location[i][1] -= 1
                if location[i][1] < 0:
                    location[i][1] = 0
            if move == 3:
                location[i][1] += 1
                if location[i][1] > max[1]:
                    location[i][1] = max[1]

            # 如果抓住了对方玩家，就判定为赢
            if location[i] == location[1-i]:
                return i
    return -1

# 循环赛
def tournament(pl):
    # 统计失败的次数
    losses = [0 for p in pl]

    # 每位玩家都将和其他玩家一一对抗
    for i in range(len(pl)):
        for j in range(len(pl)):
            if i == j:
                continue

            # 谁是胜利者
            winner = gridgame([pl[i], pl[j]])

            # 失败得2分，打平得1分
            if winner == 0:
                losses[j] += 2
            elif winner == 1:
                losses[i] += 2
            elif winner == -1:
                losses[i] += 1
                losses[i] += 1
                pass

    # 对结果排序并返回
    z = list(zip(losses, pl))
    z.sort()
    return z

# 真人对抗
class humanplayer:
    def evaluate(self, board):

        # 得到自己的位置和其他玩家的位置
        me = tuple(board[0:2])
        others = [tuple(board[x:x+2]) for x in range(2, len(board)-1, 2)]

        # 显示游戏区域
        for i in range(4):
            for j in range(4):
                if (i, j) == me:
                    print('O', end='')
                elif (i, j) in others:
                    print('X', end='')
                else:
                    print('.', end='')
            print()

        # 显示上一步，作为参考
        print('Your last move was %d' % board[len(board)-1])
        print(' 0')
        print('2 3')
        print(' 1')
        print('Enter move: ', end='')

        # 不论用户输入什么内容，均直接返回
        move = int(input())
        return move
