from datetime import datetime
from config import *

schedule_text = f"""\
┌──────┬──────┬──────┬──────┬──────┬──────┐
│            │   星期一   │   星期二   │   星期三   │   星期四   │   星期五   │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第一节   │    {schedule[0][0]}    │    {schedule[1][0]}    │    {schedule[2][0]}    │    {schedule[3][0]}    │    {schedule[4][0]}    │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第二节   │    {schedule[0][1]}    │    {schedule[1][1]}    │    {schedule[2][1]}    │    {schedule[3][1]}    │    {schedule[4][1]}    │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第三节   │    {schedule[0][2]}    │    {schedule[1][2]}    │    {schedule[2][2]}    │    {schedule[3][2]}    │    {schedule[4][2]}    │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第四节   │    {schedule[0][3]}    │    {schedule[1][3]}    │    {schedule[2][3]}    │    {schedule[3][3]}    │    {schedule[4][3]}    │
├──────┴──────┴──────┴──────┴──────┴──────┤
│                                   午餐  大自习                                   │
├──────┬──────┬──────┬──────┬──────┬──────┤
│   第五节   │    {schedule[0][4]}    │    {schedule[1][4]}    │    {schedule[2][4]}    │    {schedule[3][4]}    │    {schedule[4][4]}    │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第六节   │    {schedule[0][5]}    │    {schedule[1][5]}    │    {schedule[2][5]}    │    {schedule[3][5]}    │    {schedule[4][5]}    │
├──────┴──────┴──────┴──────┴──────┴──────┤
│                                      大课间                                      │
├──────┬──────┬──────┬──────┬──────┬──────┤
│   第七节   │    {schedule[0][6]}    │    {schedule[1][6]}    │    {schedule[2][6]}    │    {schedule[3][6]}    │    {schedule[4][6]}    │
├──────┼──────┼──────┼──────┼──────┼──────┤
│   第八节   │    {schedule[0][7]}    │    {schedule[1][7]}    │    {schedule[2][7]}    │    {schedule[3][7]}    │    {schedule[4][7]}    │
└──────┴──────┴──────┴──────┴──────┴──────┘"""

def get_time_ranges():
    weekday = get_weekday()
    if 0 <= weekday <= 4:
        return [
            ( 0,  0,  0,  7, 20,  0,  "准备早读 07:20早读 准备工作"),
            ( 7, 20,  0,  7, 50,  0,  f"早读时间 07:50下课 {during_class}"),
            ( 7, 50,  0,  7, 50, ss,  "早读时间 已下课 等待打铃"),
            ( 7, 50, ss,  7, 50, es,  "早读时间 已下课 正在打铃"),
            ( 7, 50, es,  7, 58,  0,  f"课间休息 07:58准备{schedule[weekday][0]} {class_break}"),

            ( 7, 58,  0,  8,  0,  0,  f"{schedule[weekday][0]} 08:00上课 {before_class}"),
            ( 8,  0,  0,  8,  0, ss,  f"{schedule[weekday][0]} 已上课 等待打铃"),
            ( 8,  0, ss,  8,  0, es,  f"{schedule[weekday][0]} 已上课 正在打铃"),
            ( 8,  0, es,  8, 40,  0,  f"{schedule[weekday][0]} 08:40下课 {during_class}"),
            ( 8, 40,  0,  8, 40, ss,  f"{schedule[weekday][0]} 已下课 等待打铃"),
            ( 8, 40, ss,  8, 40, es,  f"{schedule[weekday][0]} 已下课 正在打铃"),
            ( 8, 40, es,  8, 58,  0,  f"课间休息 08:58准备{schedule[weekday][1]} {class_break}"),

            ( 8, 58,  0,  8, 58, ss,  f"{schedule[weekday][1]} 准备上课 等待打铃"),
            ( 8, 58, ss,  8, 58, es,  f"{schedule[weekday][1]} 准备上课 正在打铃"),
            ( 8, 58, es,  9,  0,  0,  f"{schedule[weekday][1]} 09:00上课 {before_class}"),
            ( 9,  0,  0,  9,  0, ss,  f"{schedule[weekday][1]} 已上课 等待打铃"),
            ( 9,  0, ss,  9,  0, es,  f"{schedule[weekday][1]} 已上课 正在打铃"),
            ( 9,  0, es,  9, 40,  0,  f"{schedule[weekday][1]} 09:40下课 {during_class}"),
            ( 9, 40,  0,  9, 40, ss,  f"{schedule[weekday][1]} 已下课 等待打铃"),
            ( 9, 40, ss,  9, 40, es,  f"{schedule[weekday][1]} 已下课 正在打铃"),
            ( 9, 40, es,  9, 48,  0,  f"课间休息 09:48准备{schedule[weekday][2]} {class_break}"),

            ( 9, 48,  0,  9, 48, ss,  f"{schedule[weekday][2]} 准备上课 等待打铃"),
            ( 9, 48, ss,  9, 48, es,  f"{schedule[weekday][2]} 准备上课 正在打铃"),
            ( 9, 48, es,  9, 50,  0,  f"{schedule[weekday][2]} 09:50上课 {before_class}"),
            ( 9, 50,  0,  9, 50, ss,  f"{schedule[weekday][2]} 已上课 等待打铃"),
            ( 9, 50, ss,  9, 50, es,  f"{schedule[weekday][2]} 已上课 正在打铃"),
            ( 9, 50, es, 10, 30,  0,  f"{schedule[weekday][2]} 10:30下课 {during_class}"),
            (10, 30,  0, 10, 30, ss,  f"{schedule[weekday][2]} 已下课 等待打铃"),
            (10, 30, ss, 10, 30, es,  f"{schedule[weekday][2]} 已下课 正在打铃"),
            (10, 30, es, 10, 36, 15,  "眼保健操 10:36:15结束 认真做操"),
            (10, 36, 15, 10, 43,  0,  f"课间休息 10:43准备{schedule[weekday][3]} {class_break}"),

            (10, 43,  0, 10, 43, ss,  f"{schedule[weekday][3]} 准备上课 等待打铃"),
            (10, 43, ss, 10, 43, es,  f"{schedule[weekday][3]} 准备上课 正在打铃"),
            (10, 43, es, 10, 45,  0,  f"{schedule[weekday][3]} 10:45上课 {before_class}"),
            (10, 45,  0, 10, 45, ss,  f"{schedule[weekday][3]} 已上课 等待打铃"),
            (10, 45, ss, 10, 45, es,  f"{schedule[weekday][3]} 已上课 正在打铃"),
            (10, 45, es, 11, 25,  0,  f"{schedule[weekday][3]} 11:25下课 {during_class}"),
            (11, 25,  0, 11, 25, ss,  f"{schedule[weekday][3]} 已下课 等待打铃"),
            (11, 25, ss, 11, 25, es,  f"{schedule[weekday][3]} 已下课 正在打铃"),
            (11, 25, es, 11, 35,  0,  "课间休息 11:35午餐 等着吃饭"),
            (11, 35,  0, 12, 15,  0,  "午餐时间 12:15大自习 ---"),

            (12, 15,  0, 12, 50,  0,  "大自习 12:50下课 安静自习"),
            (12, 50,  0, 12, 50, ss,  "大自习 已下课 等待打铃"),
            (12, 50, ss, 12, 50, es,  "大自习 已下课 正在打铃"),
            (12, 50, es, 12, 58,  0,  f"课间休息 12:58准备{schedule[weekday][4]} {class_break}"),

            (12, 58,  0, 12, 58, ss,  f"{schedule[weekday][4]} 准备上课 等待打铃"),
            (12, 58, ss, 12, 58, es,  f"{schedule[weekday][4]} 准备上课 正在打铃"),
            (12, 58, es, 13,  0,  0,  f"{schedule[weekday][4]} 13:00上课 {before_class}"),
            (13,  0,  0, 13,  0, ss,  f"{schedule[weekday][4]} 已上课 等待打铃"),
            (13,  0, ss, 13,  0, es,  f"{schedule[weekday][4]} 已上课 正在打铃"),
            (13,  0, es, 13, 40,  0,  f"{schedule[weekday][4]} 13:40下课 {during_class}"),
            (13, 40,  0, 13, 40, ss,  f"{schedule[weekday][4]} 已下课 等待打铃"),
            (13, 40, ss, 13, 40, es,  f"{schedule[weekday][4]} 已下课 正在打铃"),
            (13, 40, es, 13, 46, 15,  "眼保健操 13:46:15结束 认真做操"),
            (13, 46, 15, 13, 53,  0,  f"课间休息 13:53准备{schedule[weekday][5]} {class_break}"),

            (13, 53,  0, 13, 53, ss,  f"{schedule[weekday][5]} 准备上课 等待打铃"),
            (13, 53, ss, 13, 53, es,  f"{schedule[weekday][5]} 准备上课 正在打铃"),
            (13, 53, es, 13, 55,  0,  f"{schedule[weekday][5]} 13:55上课 {before_class}"),
            (13, 55,  0, 13, 55, ss,  f"{schedule[weekday][5]} 已上课 等待打铃"),
            (13, 55, ss, 13, 55, es,  f"{schedule[weekday][5]} 已上课 正在打铃"),
            (13, 55, es, 14, 35,  0,  f"{schedule[weekday][5]} 14:35下课 {during_class}"),
            (14, 35,  0, 14, 35, ss,  f"{schedule[weekday][5]} 已下课 等待打铃"),
            (14, 35, ss, 14, 35, es,  f"{schedule[weekday][5]} 已下课 正在打铃"),
            (14, 35, es, 14, 39, 15,  "室内操 14:39:15结束 认真做操"),
            (14, 39, 15, 15,  3,  0,  f"大课间 15:03准备{schedule[weekday][6]} {class_break}"),

            (15,  3,  0, 15,  3, ss,  f"{schedule[weekday][6]} 准备上课 等待打铃"),
            (15,  3, ss, 15,  3, es,  f"{schedule[weekday][6]} 准备上课 正在打铃"),
            (15,  3, es, 15,  5,  0,  f"{schedule[weekday][6]} 15:05上课 {before_class}"),
            (15,  5,  0, 15,  5, ss,  f"{schedule[weekday][6]} 已上课 等待打铃"),
            (15,  5, ss, 15,  5, es,  f"{schedule[weekday][6]} 已上课 正在打铃"),
            (15,  5, es, 15, 45,  0,  f"{schedule[weekday][6]} 15:45下课 {during_class}"),
            (15, 45,  0, 15, 45, ss,  f"{schedule[weekday][6]} 已下课 等待打铃"),
            (15, 45, ss, 15, 45, es,  f"{schedule[weekday][6]} 已下课 正在打铃"),
            (15, 45, es, 15, 53,  0,  f"课间休息 15:53准备{schedule[weekday][7]} {class_break}"),

            (15, 53,  0, 15, 53, ss,  f"{schedule[weekday][7]} 准备上课 等待打铃"),
            (15, 53, ss, 15, 53, es,  f"{schedule[weekday][7]} 准备上课 正在打铃"),
            (15, 53, es, 15, 55,  0,  f"{schedule[weekday][7]} 15:55上课 {before_class}"),
            (15, 55,  0, 15, 55, ss,  f"{schedule[weekday][7]} 已上课 等待打铃"),
            (15, 55, ss, 15, 55, es,  f"{schedule[weekday][7]} 已上课 正在打铃"),
            (15, 55, es, 16, 35,  0,  f"{schedule[weekday][7]} 16:35下课 {during_class}"),
            (16, 35,  0, 16, 35, ss,  f"{schedule[weekday][7]} 已下课 等待打铃"),
            (16, 35, ss, 16, 35, es,  f"{schedule[weekday][7]} 已下课 正在打铃"),
            (16, 35, es, 24,  0,  0,  "放学 --- 回家休息")
        ]
    else:
        return [
            ( 0,  0,  0, 24,  0,  0,  "双休日 --- 好好休息")
        ]