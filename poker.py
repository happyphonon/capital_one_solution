'''
2个poker各有自己的deck, 两个deck里面的牌一样多, 从最上面开始抽, 
数字比较大的牌可以拿走两人的牌放回自己的deck bottom, 直到有人的deck空了,
 return总共玩了几回合
'''
def solution(deck_one, deck_two):
    num_rounds = 0
    while deck_one and deck_two:
        player_one, player_two = deck_one.pop(0), deck_two.pop(0)
        # if tie (player_one == player_two, do not place into any dec)
        if player_one > player_two:
            deck_one.append(player_one)
            deck_one.append(player_two)
        elif player_one < player_two:
            deck_two.append(player_one)
            deck_two.append(player_two)
        print(deck_one, deck_two)
        num_rounds += 1
    return num_rounds

print(solution([2, 1, 4, 5], [1, 10, 4, 7]))