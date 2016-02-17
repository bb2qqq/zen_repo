#! coding: utf-8

# A和B各出一枚硬币，如果都是正面，B给A三元，如果都是反面，B给A 一元，其他情况A给B 两元。
# 如果双方随机出硬币，大量的重复后是什么结果, 在初始资金足够大的情况下，A和B是否有相应的必胜（接近必胜）的策略?
import random
import itertools


class CoinRecorder(object):

    record = {}

    def result_decider(self, coin1, coin2):
        # 正面为True, 反面为False
        if coin1 == coin2:
            if coin1 == True:
                result = 3
            else:
                result = 1
        else:
            result = -2
        return result


    def record_result(self, key, game_num, result):
        print key, '\t'*2, game_num, '\t', result
        if key in self.record:
            self.record[key]['game_num'] += game_num
            self.record[key]['result'] += result
            self.record[key]['average_result'] = round(result/float(game_num), 8)
            self.record[key]['history'].append((game_num, result))
        else:
            self.record[key] = {
                'game_num': game_num,
                'result': result,
                'average_result': round(result/float(game_num), 8),
                'history': [(game_num, result)]
            }

    def short_memory_game(self, game_num=1):
        total_result = 0
        coin1 = None
        for i in xrange(game_num):
            previous_coin1 = coin1
            if previous_coin1:
                coin1 = not previous_coin1
            else:
                coin1 = random.choice([True, False])
            if previous_coin1:
                coin2 = not previous_coin1
            else:
                coin2 = random.choice([True, False])
            one_game_result = result_decider(coin1, coin2)
            total_result += one_game_result
        print game_num, total_result

    def vary_best_strategy_game(self, game_num=1, rival_true_num=1, rival_false_num=1, p2_strategy=[]):
        """玩家二使用最佳策略, 玩家1的概率策略由传入参数决定，默认50% True, 50% False. """
        total_result = 0
        L1 = list(itertools.repeat(True, rival_true_num))
        L2 = list(itertools.repeat(False, rival_false_num))
        player1_strategy_pool = L1 + L2
        player2_strategy_pool = p2_strategy or [True, True, True, False, False, False, False, False]
        for i in xrange(game_num):
            coin1 = random.choice(player1_strategy_pool)
            coin2 = random.choice(player2_strategy_pool)
            one_game_result = self.result_decider(coin1, coin2)
            total_result += one_game_result
        stats_key = '_'.join(map(str, [game_num, rival_true_num, rival_false_num, p2_strategy]))
        self.record_result(stats_key, game_num, total_result)

    def show_stats(self):
        for key, val in self.record.iteritems():
            print key, val['game_num'], val['result'], val['average_result']
