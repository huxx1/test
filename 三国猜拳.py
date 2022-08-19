# coding:utf-8
# 题目3
# 关羽 和张飞 正在玩 剪刀石头布 的游戏。
#
# 写一个函数calculate_score， 参数是列表， 里面包含了n个元素也是列表。
#
# 比如 像这样 [[“剪刀”, “石头”], [“布”, “剪刀”], [“剪刀”, “剪刀”]]
#
# n 个元素代表 n局 比赛，用列表表示，比如 [“剪刀”, “石头”]
#
# 其中第1个元素表示关羽打出的手势，第2个元素是张飞打出的手势。
#
# 函数要计算出谁赢得次数多，输出比赛结果。
#
# 如果他们打成平手，输出“平局”。
#
# 比如：

# calculate_score([["剪刀", "石头"], ["布", "剪刀"], ["剪刀", "剪刀"]])
# 输出应该是： 张飞 3局赢了2局，平手一局，张飞胜出
#
#
# calculate_score([["布", "石头"], ["石头", "剪刀"], ["石头", "剪刀"]])
# 输出应该是： 关羽 3局赢了3局，关羽胜出
def calculate_score(rounds):
    guan_win_round=0
    zhang_win_round=0
    ping_round=0
    for round in rounds:
        guan=round[0]
        zhang=round[1]
    #判断谁赢
        win=None
        if guan=='剪刀':
            if zhang=='石头':
                win='z'
            elif zhang=='剪刀':
                win='='
            else:
                win='g'
        elif guan=='石头':
            if zhang=='石头':
                win='='
            elif zhang=='剪刀':
                win='g'
            else:
                win='z'
        elif guan=='布':
            if zhang=='石头':
                win='g'
            elif zhang=='剪刀':
                win='z'
            else:
                win='='
        if win=='g':
            print('关羽赢')
            guan_win_round+=1
        elif win=='z':
            print('张飞赢')
            zhang_win_round+=1
        elif win=='=':
            print('平局')
            ping_round+=1
    print('\n-------------\n')
    print(f'关羽赢{guan_win_round}次')
    print(f'张飞赢{zhang_win_round}次')
    print(f'平局{ping_round}次')
    if guan_win_round>zhang_win_round:
        print('关羽赢')
    elif guan_win_round<zhang_win_round:
        print('张飞赢')
    else:
        print('平局')


calculate_score([["剪刀", "石头"], ["布", "剪刀"], ["剪刀", "剪刀"]])



