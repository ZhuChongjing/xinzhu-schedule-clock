from config import *

schedule_text = f"""\
┌──────┬──────┬──────┬──────┬──────┬──────┐
│            │   星期一   │   星期二   │   星期三   │   星期四   │   星期五   │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第一节   │    {SCHEDULE[0][0]}    │    {SCHEDULE[1][0]}    │    {SCHEDULE[2][0]}    │    {SCHEDULE[3][0]}    │    {SCHEDULE[4][0]}    │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第二节   │    {SCHEDULE[0][1]}    │    {SCHEDULE[1][1]}    │    {SCHEDULE[2][1]}    │    {SCHEDULE[3][1]}    │    {SCHEDULE[4][1]}    │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第三节   │    {SCHEDULE[0][2]}    │    {SCHEDULE[1][2]}    │    {SCHEDULE[2][2]}    │    {SCHEDULE[3][2]}    │    {SCHEDULE[4][2]}    │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第四节   │    {SCHEDULE[0][3]}    │    {SCHEDULE[1][3]}    │    {SCHEDULE[2][3]}    │    {SCHEDULE[3][3]}    │    {SCHEDULE[4][3]}    │
├──────┴──────┴──────┴──────┴──────┴──────┤
│                                   午餐  大自习                                   │
├──────┬──────┬──────┬──────┬──────┬──────┤
│   第五节   │    {SCHEDULE[0][4]}    │    {SCHEDULE[1][4]}    │    {SCHEDULE[2][4]}    │    {SCHEDULE[3][4]}    │    {SCHEDULE[4][4]}    │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第六节   │    {SCHEDULE[0][5]}    │    {SCHEDULE[1][5]}    │    {SCHEDULE[2][5]}    │    {SCHEDULE[3][5]}    │    {SCHEDULE[4][5]}    │
├──────┴──────┴──────┴──────┴──────┴──────┤
│                                      大课间                                      │
├──────┬──────┬──────┬──────┬──────┬──────┤
│   第七节   │    {SCHEDULE[0][6]}    │    {SCHEDULE[1][6]}    │    {SCHEDULE[2][6]}    │    {SCHEDULE[3][6]}    │    {SCHEDULE[4][6]}    │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第八节   │    {SCHEDULE[0][7]}    │    {SCHEDULE[1][7]}    │    {SCHEDULE[2][7]}    │    {SCHEDULE[3][7]}    │    {SCHEDULE[4][7]}    │
└──────┴──────┴──────┴──────┴──────┴──────┘"""

def get_time_ranges():
    weekday = get_weekday() - 1
    if 0 <= weekday <= 4:
        return [
            ( 0,  0,            0,  7, 20,            0,  f"准备早读 07:20早读 准备工作"),
            ( 7, 20,            0,  7, 50,            0,  f"早读时间 07:50下课 {DURING_CLASS}"),
            ( 7, 50,            0,  7, 50, START_SECOND,  f"早读时间 已下课 等待打铃"),
            ( 7, 50, START_SECOND,  7, 50,   END_SECOND,  f"早读时间 已下课 正在打铃"),
            ( 7, 50,   END_SECOND,  7, 58,            0,  f"课间休息 07:58准备{SCHEDULE[weekday][0]} {CLASS_BREAK}"),

            ( 7, 58,            0,  8,  0,            0,  f"{SCHEDULE[weekday][0]} 08:00上课 {BEFORE_CLASS}"),
            ( 8,  0,            0,  8,  0, START_SECOND,  f"{SCHEDULE[weekday][0]} 已上课 等待打铃"),
            ( 8,  0, START_SECOND,  8,  0,   END_SECOND,  f"{SCHEDULE[weekday][0]} 已上课 正在打铃"),
            ( 8,  0,   END_SECOND,  8, 40,            0,  f"{SCHEDULE[weekday][0]} 08:40下课 {DURING_CLASS}"),
            ( 8, 40,            0,  8, 40, START_SECOND,  f"{SCHEDULE[weekday][0]} 已下课 等待打铃"),
            ( 8, 40, START_SECOND,  8, 40,   END_SECOND,  f"{SCHEDULE[weekday][0]} 已下课 正在打铃"),
            ( 8, 40,   END_SECOND,  8, 58,            0,  f"课间休息 08:58准备{SCHEDULE[weekday][1]} {CLASS_BREAK}"),

            ( 8, 58,            0,  8, 58, START_SECOND,  f"{SCHEDULE[weekday][1]} 准备上课 等待打铃"),
            ( 8, 58,   END_SECOND,  8, 58,   END_SECOND,  f"{SCHEDULE[weekday][1]} 准备上课 正在打铃"),
            ( 8, 58,   END_SECOND,  9,  0,            0,  f"{SCHEDULE[weekday][1]} 09:00上课 {BEFORE_CLASS}"),
            ( 9,  0,            0,  9,  0, START_SECOND,  f"{SCHEDULE[weekday][1]} 已上课 等待打铃"),
            ( 9,  0, START_SECOND,  9,  0,   END_SECOND,  f"{SCHEDULE[weekday][1]} 已上课 正在打铃"),
            ( 9,  0,   END_SECOND,  9, 40,            0,  f"{SCHEDULE[weekday][1]} 09:40下课 {DURING_CLASS}"),
            ( 9, 40,            0,  9, 40, START_SECOND,  f"{SCHEDULE[weekday][1]} 已下课 等待打铃"),
            ( 9, 40, START_SECOND,  9, 40,   END_SECOND,  f"{SCHEDULE[weekday][1]} 已下课 正在打铃"),
            ( 9, 40,   END_SECOND,  9, 48,            0,  f"课间休息 09:48准备{SCHEDULE[weekday][2]} {CLASS_BREAK}"),

            ( 9, 48,            0,  9, 48, START_SECOND,  f"{SCHEDULE[weekday][2]} 准备上课 等待打铃"),
            ( 9, 48, START_SECOND,  9, 48,   END_SECOND,  f"{SCHEDULE[weekday][2]} 准备上课 正在打铃"),
            ( 9, 48,   END_SECOND,  9, 50,            0,  f"{SCHEDULE[weekday][2]} 09:50上课 {BEFORE_CLASS}"),
            ( 9, 50,            0,  9, 50, START_SECOND,  f"{SCHEDULE[weekday][2]} 已上课 等待打铃"),
            ( 9, 50, START_SECOND,  9, 50,   END_SECOND,  f"{SCHEDULE[weekday][2]} 已上课 正在打铃"),
            ( 9, 50,   END_SECOND, 10, 30,            0,  f"{SCHEDULE[weekday][2]} 10:30下课 {DURING_CLASS}"),
            (10, 30,            0, 10, 30, START_SECOND,  f"{SCHEDULE[weekday][2]} 已下课 等待打铃"),
            (10, 30, START_SECOND, 10, 30,   END_SECOND,  f"{SCHEDULE[weekday][2]} 已下课 正在打铃"),
            (10, 30,   END_SECOND, 10, 36,           15,  f"眼保健操 10:36:15结束 认真做操"),
            (10, 36,           15, 10, 43,            0,  f"课间休息 10:43准备{SCHEDULE[weekday][3]} {CLASS_BREAK}"),

            (10, 43,            0, 10, 43, START_SECOND,  f"{SCHEDULE[weekday][3]} 准备上课 等待打铃"),
            (10, 43, START_SECOND, 10, 43,   END_SECOND,  f"{SCHEDULE[weekday][3]} 准备上课 正在打铃"),
            (10, 43,   END_SECOND, 10, 45,            0,  f"{SCHEDULE[weekday][3]} 10:45上课 {BEFORE_CLASS}"),
            (10, 45,            0, 10, 45, START_SECOND,  f"{SCHEDULE[weekday][3]} 已上课 等待打铃"),
            (10, 45, START_SECOND, 10, 45,   END_SECOND,  f"{SCHEDULE[weekday][3]} 已上课 正在打铃"),
            (10, 45,   END_SECOND, 11, 25,            0,  f"{SCHEDULE[weekday][3]} 11:25下课 {DURING_CLASS}"),
            (11, 25,            0, 11, 25, START_SECOND,  f"{SCHEDULE[weekday][3]} 已下课 等待打铃"),
            (11, 25, START_SECOND, 11, 25,   END_SECOND,  f"{SCHEDULE[weekday][3]} 已下课 正在打铃"),
            (11, 25,   END_SECOND, 11, 35,            0,  f"课间休息 11:35午餐 等着吃饭"),
            (11, 35,            0, 12, 15,            0,  f"午餐时间 12:15大自习 ---"),

            (12, 15,            0, 12, 50,            0,  f"大自习 12:50下课 安静自习"),
            (12, 50,            0, 12, 50, START_SECOND,  f"大自习 已下课 等待打铃"),
            (12, 50, START_SECOND, 12, 50,   END_SECOND,  f"大自习 已下课 正在打铃"),
            (12, 50,   END_SECOND, 12, 58,            0,  f"课间休息 12:58准备{SCHEDULE[weekday][4]} {CLASS_BREAK}"),

            (12, 58,            0, 12, 58, START_SECOND,  f"{SCHEDULE[weekday][4]} 准备上课 等待打铃"),
            (12, 58, START_SECOND, 12, 58,   END_SECOND,  f"{SCHEDULE[weekday][4]} 准备上课 正在打铃"),
            (12, 58,   END_SECOND, 13,  0,            0,  f"{SCHEDULE[weekday][4]} 13:00上课 {BEFORE_CLASS}"),
            (13,  0,            0, 13,  0, START_SECOND,  f"{SCHEDULE[weekday][4]} 已上课 等待打铃"),
            (13,  0, START_SECOND, 13,  0,   END_SECOND,  f"{SCHEDULE[weekday][4]} 已上课 正在打铃"),
            (13,  0,   END_SECOND, 13, 40,            0,  f"{SCHEDULE[weekday][4]} 13:40下课 {DURING_CLASS}"),
            (13, 40,            0, 13, 40, START_SECOND,  f"{SCHEDULE[weekday][4]} 已下课 等待打铃"),
            (13, 40, START_SECOND, 13, 40,   END_SECOND,  f"{SCHEDULE[weekday][4]} 已下课 正在打铃"),
            (13, 40,   END_SECOND, 13, 46,           15,  f"眼保健操 13:46:15结束 认真做操"),    
            (13, 46,           15, 13, 53,            0,  f"课间休息 13:53准备{SCHEDULE[weekday][5]} {CLASS_BREAK}"),

            (13, 53,            0, 13, 53, START_SECOND,  f"{SCHEDULE[weekday][5]} 准备上课 等待打铃"),
            (13, 53, START_SECOND, 13, 53,   END_SECOND,  f"{SCHEDULE[weekday][5]} 准备上课 正在打铃"),
            (13, 53,   END_SECOND, 13, 55,            0,  f"{SCHEDULE[weekday][5]} 13:55上课 {BEFORE_CLASS}"),  
            (13, 55,            0, 13, 55, START_SECOND,  f"{SCHEDULE[weekday][5]} 已上课 等待打铃"),
            (13, 55, START_SECOND, 13, 55,   END_SECOND,  f"{SCHEDULE[weekday][5]} 已上课 正在打铃"),
            (13, 55,   END_SECOND, 14, 35,            0,  f"{SCHEDULE[weekday][5]} 14:35下课 {DURING_CLASS}"),
            (14, 35,            0, 14, 35, START_SECOND,  f"{SCHEDULE[weekday][5]} 已下课 等待打铃"),
            (14, 35, START_SECOND, 14, 35,   END_SECOND,  f"{SCHEDULE[weekday][5]} 已下课 正在打铃"),
            (14, 35,   END_SECOND, 14, 39,           15,  f"室内操 14:39:15结束 认真做操"),
            (14, 39,           15, 15,  3,            0,  f"大课间 15:03准备{SCHEDULE[weekday][6]} {CLASS_BREAK}"),

            (15,  3,            0, 15,  3, START_SECOND,  f"{SCHEDULE[weekday][6]} 准备上课 等待打铃"),
            (15,  3, START_SECOND, 15,  3,   END_SECOND,  f"{SCHEDULE[weekday][6]} 准备上课 正在打铃"),
            (15,  3,   END_SECOND, 15,  5,            0,  f"{SCHEDULE[weekday][6]} 15:05上课 {BEFORE_CLASS}"),
            (15,  5,            0, 15,  5, START_SECOND,  f"{SCHEDULE[weekday][6]} 已上课 等待打铃"),
            (15,  5, START_SECOND, 15,  5,   END_SECOND,  f"{SCHEDULE[weekday][6]} 已上课 正在打铃"),
            (15,  5,   END_SECOND, 15, 45,            0,  f"{SCHEDULE[weekday][6]} 15:45下课 {DURING_CLASS}"),
            (15, 45,            0, 15, 45, START_SECOND,  f"{SCHEDULE[weekday][6]} 已下课 等待打铃"),
            (15, 45, START_SECOND, 15, 45,   END_SECOND,  f"{SCHEDULE[weekday][6]} 已下课 正在打铃"),
            (15, 45,   END_SECOND, 15, 53,            0,  f"课间休息 15:53准备{SCHEDULE[weekday][7]} {CLASS_BREAK}"),

            (15, 53,            0, 15, 53, START_SECOND,  f"{SCHEDULE[weekday][7]} 准备上课 等待打铃"),
            (15, 53, START_SECOND, 15, 53,   END_SECOND,  f"{SCHEDULE[weekday][7]} 准备上课 正在打铃"),
            (15, 53,   END_SECOND, 15, 55,            0,  f"{SCHEDULE[weekday][7]} 15:55上课 {BEFORE_CLASS}"),
            (15, 55,            0, 15, 55, START_SECOND,  f"{SCHEDULE[weekday][7]} 已上课 等待打铃"),
            (15, 55, START_SECOND, 15, 55,   END_SECOND,  f"{SCHEDULE[weekday][7]} 已上课 正在打铃"),
            (15, 55,   END_SECOND, 16, 35,            0,  f"{SCHEDULE[weekday][7]} 16:35下课 {DURING_CLASS}"),
            (16, 35,            0, 16, 35, START_SECOND,  f"{SCHEDULE[weekday][7]} 已下课 等待打铃"),
            (16, 35, START_SECOND, 16, 35,   END_SECOND,  f"{SCHEDULE[weekday][7]} 已下课 正在打铃"),
            (16, 35,   END_SECOND, 24,  0,            0,  f"放学 --- 回家休息")
        ]
    else:
        return [
            ( 0,  0,  0, 24,  0,  0,  f"双休日 --- 好好休息")
        ]