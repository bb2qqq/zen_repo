# coding: utf-8
import random
import datetime
import sys

if len(sys.argv) >= 2:
    remaining_games = int(sys.argv[1])
else:
    remaining_games = 25

your_game_record = []
record_counter = 0


def go_legend_need_games(winning_rate, test_num=10, need_win=25):
    """
    :param winning_rate: float, 胜率, 0.65表示百分之65的胜率
    :returns: int, 获胜所需盘数
    """
    all_test_results = []
    for i in range(test_num):
        current_win = total_play_num = 0
        while current_win < need_win:
            if random.random() < winning_rate:
                current_win += 1
            else:
                current_win -= 1
            total_play_num += 1
        all_test_results.append(total_play_num)

    result = sum(all_test_results)/len(all_test_results)
    print result
    return result

def active_recorder(last_game_result):
    """
    :param last_game_result: Bool, True表示获胜，False表示失败
        当你在5至传说的分段内，每赢一局或输一局，用这个记录下
    :returns: None
    """
    global record_counter, your_game_record, remaining_games
    log_file = open('play_record', 'a')
    record_counter += 1
    your_game_record.append(last_game_result)
    if last_game_result:
        remaining_games -= 1
    else:
        remaining_games += 1
    last_10_record = your_game_record[-10:]
    last_10_win_rate = last_10_record.count(True)/float(len(last_10_record))
    if last_10_win_rate > 0.5:
        need_games_for_10_rate = go_legend_need_games(last_10_win_rate, need_win=remaining_games)
    else:
        need_games_for_10_rate = 99999
    print "Your last 10 games win rate is %f, you need to play %d games to go to legend." \
          % (last_10_win_rate, need_games_for_10_rate)

    total_win_rate = your_game_record.count(True)/float(len(your_game_record))
    if total_win_rate > 0.5:
        need_games_for_total_rate = go_legend_need_games(total_win_rate, need_win=remaining_games)
    else:
        need_games_for_total_rate = 99999
    print "Your total win rate is %f, you need to play %d games to go to legend." \
          % (total_win_rate, need_games_for_total_rate)
    print "You need to win %d more stars to go to legend" % remaining_games

    if record_counter % 10 == 0:
        date_time = str(datetime.datetime.now())[:19]
        log_info = str(your_game_record) + '\t' + date_time + '\n'
        log_file.write(log_info)


