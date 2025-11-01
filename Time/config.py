from datetime import datetime
from tkinter import font

SCHEDULE = [
    ["数学", "数学", "英语", "英语", "语文", "体锻", "选修", "选修"],
    ["数学", "英语", "地理", "信息", "生物", "体育", "语文", "历史"],
    ["数学", "英语", "体育", "语文", "生物", "语文", "道法", "劳技"],
    ["语文", "历史", "体锻", "音乐", "数学", "数学", "物理", "英语"],
    ["数学", "地理", "美术", "体育", "英语", "心理", "语文", "班会"]
]

def get_weekday():
    weekday = datetime.now().isoweekday()
    if 1 <= weekday <= 5:
        return weekday
    elif weekday == 6:
        # 临时修改
        # return 
        return weekday
    elif weekday == 7:
        # 临时修改
        # return 
        return weekday
    
FIRST_DAY = "2025-09-01"

BEFORE_CLASS = "准备上课"
DURING_CLASS = "认真听讲"
CLASS_BREAK = "记得擦黑板"

START_SECOND = 19
END_SECOND = 41

WINDOW_TITLE = "时间+课程显示器"

WINDOW_WIDTH = 1250
WINDOW_HEIGHT = 60
WINDOW_ALPHA = 0.8

WINDOW_SMALL_WIDTH = 445
WINDOW_DROPDOWN_HEIGHT = 540

CONTROL_PANEL_WIDTH = 400
CONTROL_PANEL_HEIGHT = 350

DISPLAY_FONT = font.Font(family="KaiTi", size=25, weight="bold")
DROPDOWN_FONT = font.Font(family="KaiTi", size=15, weight="normal")
TRIANGLE_FONT = font.Font(family="KaiTi", size=20, weight="bold")
FULLSCREEN_FONT = font.Font(family="KaiTi", size=200, weight="bold")
BUTTON_FONT_CHINESE = font.Font(family="KaiTi", size=14, weight="normal")
BUTTON_FONT_ENGLISH = font.Font(family="Consolas", size=14, weight="normal")
