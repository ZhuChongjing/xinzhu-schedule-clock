from tkinter import font

# 课程表 --------------------------------------------------------------------------------------------
SCHEDULE = [
    ["数学", "数学", "英语", "英语", "语文", "体锻", "选修", "选修"], # 周一
    ["数学", "英语", "地理", "信息", "生物", "体育", "语文", "历史"], # 周二
    ["数学", "英语", "体育", "语文", "生物", "语文", "道法", "劳技"], # 周三
    ["语文", "历史", "体锻", "音乐", "数学", "数学", "物理", "英语"], # 周四
    ["数学", "地理", "美术", "体育", "英语", "心理", "语文", "班会"], # 周五
]

# 用于临时修改，设置周六和周日的课程
SATURDAY = 6
SUNDAY = 7

# 课程设置 --------------------------------------------------------------------------------------------
FIRST_DAY = "2025-09-01"

START_SECOND = 21
END_SECOND = 42

# 窗口设置 --------------------------------------------------------------------------------------------
WINDOW_TITLE = "时间+课程显示"

WINDOW_WIDTH = 425
WINDOW_HEIGHT = 95
WINDOW_ALPHA = 0.5

CONTROL_PANEL_WIDTH = 880
CONTROL_PANEL_HEIGHT = 475

# 颜色 --------------------------------------------------------------------------------------------
WINDOW_BACKGROUND_COLOR = "#FFFFFF"
FRAME_BACKGROUND_COLOR = "#FFFFFF"
FULLSCREEN_WINDOW_BACKGROUND_COLOR = "#000000"
FULLSCREEN_WINDOW_FOREGROUND_COLOR = "#FFFFFF"
BACKGROUND_COLOR = "#FFFFFF"
FOREGROUND_COLOR = "#000000"
BUTTON_BACKGROUND_COLOR = "#FFFFFF"
BUTTON_FOREGROUND_COLOR = "#000000"

CONTROL_PANEL_BACKGROUND_COLOR = "#FFFFFF"
CONTROL_PANEL_FOREGROUND_COLOR = "#000000"
CONTROL_PANEL_FRAME_BACKGROUND_COLOR = "#FFFFFF"
CONTROL_PANEL_BUTTON_BACKGROUND_COLOR = "#FFFFFF"
CONTROL_PANEL_BUTTON_FOREGROUND_COLOR = "#000000"

# 字体 --------------------------------------------------------------------------------------------
DISPLAY_FONT = font.Font(family="KaiTi", size=25, weight="bold")
SMALL_FONT = font.Font(family="KaiTi", size=20, weight="normal")
SCHEDULE_FONT = font.Font(family="KaiTi", size=15, weight="normal")
BUTTON_FONT = font.Font(family="KaiTi", size=15, weight="normal")
FULLSCREEN_FONT = font.Font(family="KaiTi", size=200, weight="bold")
CONTROL_PANEL_FONT = font.Font(family="KaiTi", size=20, weight="normal")
CONTROL_PANEL_BUTTON_FONT_CHINESE = font.Font(family="KaiTi", size=14, weight="normal")
CONTROL_PANEL_BUTTON_FONT_ENGLISH = font.Font(family="Consolas", size=14, weight="normal")

# 布局 --------------------------------------------------------------------------------------------
FRAME_PADX = 8

MAIN_FRAME_PADY = FRAME_PADX
MAIN_FRAME_LEFT_MARGIN = 5
MAIN_FRAME_ELEMENTS_PADX = 10

SMALL_FRAME_PADY = 0
SMALL_FRAME_LEFT_MARGIN = 5
SMALL_FRAME_ELEMENTS_PADX = 10
