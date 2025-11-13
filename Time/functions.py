from datetime import datetime
import subprocess

from config import SCHEDULE, SATURDAY, SUNDAY, START_SECOND, END_SECOND

# 课程 --------------------------------------------------------------------------------------------
def get_weekday():
    weekday = datetime.now().isoweekday()
    if 1 <= weekday <= 5:
        return weekday
    elif weekday == 6:
        return SATURDAY
    elif weekday == 7:
        return SUNDAY

def get_current_week_num(start_date_str, date_format):
    start_date = datetime.strptime(start_date_str, date_format).date()
    current_date = datetime.now().date()
    day_diff = (current_date - start_date).days
    current_week = (day_diff // 7) + 1
    return current_week

def to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds

def get_time_ranges():
    weekday = get_weekday() - 1
    if 0 <= weekday <= 4:
        return [
            ( 0,  0,            0,  7, 20,            0,  "准备早读",            "07:20早读"),
            ( 7, 20,            0,  7, 50,            0,  "早读时间",            "07:50下课"),
            ( 7, 50,            0,  7, 50, START_SECOND,  "已下课",              "等待打铃"),
            ( 7, 50, START_SECOND,  7, 50,   END_SECOND,  "已下课",              "正在打铃"),
            ( 7, 50,   END_SECOND,  7, 58,            0,  "课间休息",            f"07:58准备{SCHEDULE[weekday][0]}"),

            ( 7, 58,            0,  8,  0,            0,  SCHEDULE[weekday][0], "08:00上课"),
            ( 8,  0,            0,  8,  0, START_SECOND,  "已上课",              "等待打铃"),
            ( 8,  0, START_SECOND,  8,  0,   END_SECOND,  "已上课",              "正在打铃"),
            ( 8,  0,   END_SECOND,  8, 40,            0,  SCHEDULE[weekday][0], "08:40下课"),
            ( 8, 40,            0,  8, 40, START_SECOND,  "已下课",              "等待打铃"),
            ( 8, 40, START_SECOND,  8, 40,   END_SECOND,  "已下课",              "正在打铃"),
            ( 8, 40,   END_SECOND,  8, 58,            0,  "课间休息",            f"08:58准备{SCHEDULE[weekday][1]}"),

            ( 8, 58,            0,  8, 58, START_SECOND,  "准备上课",            "等待打铃"),
            ( 8, 58, START_SECOND,  8, 58,   END_SECOND,  "准备上课",            "正在打铃"),
            ( 8, 58,   END_SECOND,  9,  0,            0,  SCHEDULE[weekday][1], "09:00上课"),
            ( 9,  0,            0,  9,  0, START_SECOND,  "已上课",              "等待打铃"),
            ( 9,  0, START_SECOND,  9,  0,   END_SECOND,  "已上课",              "正在打铃"),
            ( 9,  0,   END_SECOND,  9, 40,            0,  SCHEDULE[weekday][1], "09:40下课"),
            ( 9, 40,            0,  9, 40, START_SECOND,  "已下课",              "等待打铃"),
            ( 9, 40, START_SECOND,  9, 40,   END_SECOND,  "已下课",              "正在打铃"),
            ( 9, 40,   END_SECOND,  9, 48,            0,  "课间休息",            f"09:48准备{SCHEDULE[weekday][2]}"),

            ( 9, 48,            0,  9, 48, START_SECOND,  "准备上课",            "等待打铃"),
            ( 9, 48, START_SECOND,  9, 48,   END_SECOND,  "准备上课",            "正在打铃"),
            ( 9, 48,   END_SECOND,  9, 50,            0,  SCHEDULE[weekday][2], "09:50上课"),
            ( 9, 50,            0,  9, 50, START_SECOND,  "已上课",              "等待打铃"),
            ( 9, 50, START_SECOND,  9, 50,   END_SECOND,  "已上课",              "正在打铃"),
            ( 9, 50,   END_SECOND, 10, 30,            0,  SCHEDULE[weekday][2], "10:30下课"),
            (10, 30,            0, 10, 30, START_SECOND,  "已下课",              "等待打铃"),
            (10, 30, START_SECOND, 10, 30,   END_SECOND,  "已下课",              "正在打铃"),
            (10, 30,   END_SECOND, 10, 36,           15,  "眼保健操",            "10:36:15结束"),
            (10, 36,           15, 10, 43,            0,  "课间休息",            f"10:43准备{SCHEDULE[weekday][3]}"),

            (10, 43,            0, 10, 43, START_SECOND,  "准备上课",            "等待打铃"),
            (10, 43, START_SECOND, 10, 43,   END_SECOND,  "准备上课",            "正在打铃"),
            (10, 43,   END_SECOND, 10, 45,            0,  SCHEDULE[weekday][3], "10:45上课"),
            (10, 45,            0, 10, 45, START_SECOND,  "已上课",              "等待打铃"),
            (10, 45, START_SECOND, 10, 45,   END_SECOND,  "已上课",              "正在打铃"),   
            (10, 45,   END_SECOND, 11, 25,            0,  SCHEDULE[weekday][3], "11:25下课"),
            (11, 25,            0, 11, 25, START_SECOND,  "已下课",              "等待打铃"),
            (11, 25, START_SECOND, 11, 25,   END_SECOND,  "已下课",              "正在打铃"),
            (11, 25,   END_SECOND, 11, 35,            0,  "课间休息",            "11:35午餐"),
            (11, 35,            0, 12, 15,            0,  "午餐时间",            "12:15大自习"),
            (12, 15,            0, 12, 50,            0,  SCHEDULE[weekday][4], "12:50下课"),

            (12, 15,            0, 12, 50,            0,  "大自习",              "12:50下课"),
            (12, 50,            0, 12, 50, START_SECOND,  "已下课",              "等待打铃"),
            (12, 50, START_SECOND, 12, 50,   END_SECOND,  "已下课",              "正在打铃"),
            (12, 50,   END_SECOND, 12, 58,            0,  "课间休息",            f"12:58准备{SCHEDULE[weekday][4]}"),

            (12, 58,            0, 12, 58, START_SECOND,  "准备上课",            "等待打铃"),
            (12, 58, START_SECOND, 12, 58,   END_SECOND,  "准备上课",            "正在打铃"),
            (12, 58,   END_SECOND, 13,  0,            0,  SCHEDULE[weekday][4], "13:00上课"),
            (13,  0,            0, 13,  0, START_SECOND,  "已上课",              "等待打铃"),
            (13,  0, START_SECOND, 13,  0,   END_SECOND,  "已上课",              "正在打铃"),
            (13,  0,   END_SECOND, 13, 40,            0,  SCHEDULE[weekday][4], "13:40下课"),
            (13, 40,            0, 13, 40, START_SECOND,  "已下课",              "等待打铃"),
            (13, 40, START_SECOND, 13, 40,   END_SECOND,  "已下课",              "正在打铃"),
            (13, 40,   END_SECOND, 13, 46,           15,  "眼保健操",            "13:46:15结束"),    
            (13, 46,           15, 13, 53,            0,  "课间休息",            f"13:53准备{SCHEDULE[weekday][5]}"),

            (13, 53,            0, 13, 53, START_SECOND,  "准备上课",            "等待打铃"),
            (13, 53, START_SECOND, 13, 53,   END_SECOND,  "准备上课",            "正在打铃"),
            (13, 53,   END_SECOND, 13, 55,            0,  SCHEDULE[weekday][5], "13:55上课"),  
            (13, 55,            0, 13, 55, START_SECOND,  "已上课",              "等待打铃"),
            (13, 55, START_SECOND, 13, 55,   END_SECOND,  "已上课",              "正在打铃"),
            (13, 55,   END_SECOND, 14, 35,            0,  SCHEDULE[weekday][5], "14:35下课"),
            (14, 35,            0, 14, 35, START_SECOND,  "已下课",              "等待打铃"),
            (14, 35, START_SECOND, 14, 35,   END_SECOND,  "已下课",              "正在打铃"),
            (14, 35,   END_SECOND, 14, 39,           15,  "室内操",              "14:39:15结束"),
            (14, 39,           15, 15,  3,            0,  "大课间",              f"15:03准备{SCHEDULE[weekday][6]}"),

            (15,  3,            0, 15,  3, START_SECOND,  "准备上课",            "等待打铃"),
            (15,  3, START_SECOND, 15,  3,   END_SECOND,  "准备上课",            "正在打铃"),
            (15,  3,   END_SECOND, 15,  5,            0,  SCHEDULE[weekday][6], "15:05上课"),
            (15,  5,            0, 15,  5, START_SECOND,  "已上课",              "等待打铃"),
            (15,  5, START_SECOND, 15,  5,   END_SECOND,  "已上课",              "正在打铃"),
            (15,  5,   END_SECOND, 15, 45,            0,  SCHEDULE[weekday][6], "15:45下课"),
            (15, 45,            0, 15, 45, START_SECOND,  "已下课",              "等待打铃"),
            (15, 45, START_SECOND, 15, 45,   END_SECOND,  "已下课",              "正在打铃"),
            (15, 45,   END_SECOND, 15, 53,            0,  "课间休息",            f"15:53准备{SCHEDULE[weekday][7]}"),

            (15, 53,            0, 15, 53, START_SECOND,  "准备上课",            "等待打铃"),
            (15, 53, START_SECOND, 15, 53,   END_SECOND,  "准备上课",            "正在打铃"),
            (15, 53,   END_SECOND, 15, 55,            0,  SCHEDULE[weekday][7], "15:55上课"),
            (15, 55,            0, 15, 55, START_SECOND,  "已上课",              "等待打铃"),
            (15, 55, START_SECOND, 15, 55,   END_SECOND,  "已上课",              "正在打铃"),
            (15, 55,   END_SECOND, 16, 35,            0,  SCHEDULE[weekday][7], "16:35下课"),
            (16, 35,            0, 16, 35, START_SECOND,  "已下课",              "等待打铃"),
            (16, 35, START_SECOND, 16, 35,   END_SECOND,  "已下课",              "正在打铃"),
            (16, 35,   END_SECOND, 24,  0,            0,  "放学",                "回家休息"),
        ]
    else:
        return [
            ( 0,  0,  0, 24,  0,  0,  "双休日", "好好休息")
        ]
    
# 命令 --------------------------------------------------------------------------------------------
def start_desktop():
    subprocess.Popen("explorer.exe", shell=True)

def close_desktop():
    # 防止主程序恶意被任务管理器关闭，导致explorer.exe无法重新启动
    subprocess.Popen("taskkill /f /im taskmgr.exe", shell=True)
    subprocess.Popen("taskkill /f /im explorer.exe", shell=True)

def start_cmd():
    subprocess.Popen("cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)

def start_powershell():
    subprocess.Popen("powershell.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)