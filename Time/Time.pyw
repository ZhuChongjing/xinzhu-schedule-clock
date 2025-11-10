from datetime import datetime
import tkinter as tk
from tkinter import ttk
import sys, pygetwindow

# 先创建主窗口，使config.py可以创建字体
root = tk.Tk()
root.withdraw()

from config import *
from functions import *

# 检查窗口是否已存在
if pygetwindow.getWindowsWithTitle(WINDOW_TITLE):
    sys.exit(0)

# 变量 -------------------------------------------------------------------------------------------------------------
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
    
# 重要变量 -------------------------------------------------------------------------------------------------------------
is_fullscreen = False
is_narrow = False
normal_geometry = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0"

is_dropdown_open = False
global_control_window = None
window_mode = 1

drag_start_x = 0
drag_start_y = 0
is_dragging = False

# 函数 -------------------------------------------------------------------------------------------------------------

def update_time_and_text():
    now = datetime.now()
    current_week_num = get_current_week_num(FIRST_DAY, "%Y-%m-%d")
    formatted_time = now.strftime(f"%H:%M:%S")
    formatted_date = now.strftime(f"(%m.%d)")
    time_label.config(text=formatted_time)
    narrow_date_label.config(text=f"第{current_week_num}周{formatted_date}")
    
    update_period_text(now)
    
    root.after(100, update_time_and_text)

def update_period_text(current_time):
    current_total_seconds = to_seconds(
        current_time.hour, 
        current_time.minute, 
        current_time.second
    )
    
    time_ranges = get_time_ranges()

    for (start_h, start_m, start_s, 
         end_h, end_m, end_s, text) in time_ranges:
        
        start_total = to_seconds(start_h, start_m, start_s)
        end_total = to_seconds(end_h, end_m, end_s)
        
        if start_total > end_total:
            if current_total_seconds >= start_total or current_total_seconds < end_total:
                parts = text.split()
                if len(parts) == 3:
                    a_label.config(text=parts[0])
                    b_label.config(text=parts[1])
                    c_label.config(text=parts[2])
                    narrow_b_label.config(text=parts[1])
                    narrow_c_label.config(text=parts[2])
                return
        else:
            if start_total <= current_total_seconds < end_total:
                parts = text.split()
                if len(parts) == 3:
                    a_label.config(text=parts[0])
                    b_label.config(text=parts[1])
                    c_label.config(text=parts[2])
                    narrow_b_label.config(text=parts[1])
                    narrow_c_label.config(text=parts[2])
                return

    a_label.config(text="---")
    b_label.config(text="---")
    c_label.config(text="---")
    narrow_b_label.config(text="---")
    narrow_c_label.config(text="---")
    
def toggle_fullscreen(event=None):
    global is_fullscreen, normal_geometry, fullscreen_window
    if is_fullscreen:
        if fullscreen_window:
            fullscreen_window.destroy()
            fullscreen_window = None
            
        is_fullscreen = False
    else:
        fullscreen_window = tk.Toplevel(root)
        fullscreen_window.title("全屏时间")
        fullscreen_window.attributes("-fullscreen", True)
        fullscreen_window.config(bg=FULLSCREEN_WINDOW_BACKGROUND_COLOR)
        fullscreen_window.wm_attributes("-topmost", True)
        
        fs_time_label = tk.Label(
            fullscreen_window,
            text="",
            font=FULLSCREEN_FONT,
            bg=FULLSCREEN_WINDOW_BACKGROUND_COLOR,
            fg=FULLSCREEN_WINDOW_FOREGROUND_COLOR
        )
        fs_time_label.place(relx=0.5, rely=0.5, anchor="center")
        
        def update_fs_time():
            if fullscreen_window.winfo_exists():
                now = datetime.now().strftime("%H:%M:%S")
                fs_time_label.config(text=now)
                fullscreen_window.after(100, update_fs_time)
        
        fullscreen_window.bind("<Double-1>", toggle_fullscreen)
        
        update_fs_time()
        is_fullscreen = True

def on_press(event):
    global drag_start_x, drag_start_y
    drag_start_x = event.x
    drag_start_y = event.y

def on_drag(event):
    global is_dragging
    is_dragging = True
    
    x_offset = event.x - drag_start_x
    y_offset = event.y - drag_start_y
    new_x = root.winfo_x() + x_offset
    new_y = root.winfo_y() + y_offset
    
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    
    if new_x < 0:
        new_x = 0
    if new_x + window_width > screen_width:
        new_x = screen_width - window_width
    if new_y < 0:
        new_y = 0
    if new_y + window_height > screen_height:
        new_y = screen_height - window_height
    
    root.geometry(f"+{new_x}+{new_y}")

def on_release(event):
    global is_dragging
    if is_dragging:
        is_dragging = False

def open_control_panel():
    global global_control_window
    if global_control_window and global_control_window.winfo_exists():
        global_control_window.lift()
        return
    global_control_window = tk.Toplevel(root)
    global_control_window.title("控制面板")
    global_control_window.geometry(f"{CONTROL_PANEL_WIDTH}x{CONTROL_PANEL_HEIGHT}")
    global_control_window.config(bg=CONTROL_PANEL_BACKGROUND_COLOR)
    global_control_window.wm_attributes("-topmost", True)
    global_control_window.resizable(False, False)

    # 课程表 --------------------------------------------------------------------------------------------
    schedule_frame = tk.Frame(global_control_window, bg=CONTROL_PANEL_FRAME_BACKGROUND_COLOR)
    schedule_frame.pack(padx=10, pady=5, fill=tk.X)

    schedule_label = tk.Label(
        schedule_frame,
        text=schedule_text,
        font=SCHEDULE_FONT,
        justify="left",
        bg=BACKGROUND_COLOR,
        fg=FOREGROUND_COLOR
    )
    schedule_label.pack(fill=tk.X)
    
    # 按钮 --------------------------------------------------------------------------------------------
    buttons_frame = tk.Frame(global_control_window, bg=CONTROL_PANEL_FRAME_BACKGROUND_COLOR)
    buttons_frame.pack(padx=20, pady=20, fill=tk.X, side=tk.TOP)

    style = ttk.Style()
    style.configure(
        "Chinese.TButton",
        font=CONTROL_PANEL_BUTTON_FONT_CHINESE,
        foreground=CONTROL_PANEL_BUTTON_FOREGROUND_COLOR,
        background=CONTROL_PANEL_BUTTON_BACKGROUND_COLOR,
        borderwidth=0,
        relief="flat",
        padding=0
    )
    style.configure(
        "English.TButton",
        font=CONTROL_PANEL_BUTTON_FONT_ENGLISH,
        foreground=CONTROL_PANEL_BUTTON_FOREGROUND_COLOR,
        background=CONTROL_PANEL_BUTTON_BACKGROUND_COLOR,
        borderwidth=0,
        relief="flat",
        padding=4
    )

    tk.Label(buttons_frame, text="快捷指令", font=CONTROL_PANEL_FONT, bg=CONTROL_PANEL_FRAME_BACKGROUND_COLOR).grid(row=0, column=0, padx=10, pady=0, sticky="w")

    ttk.Button(buttons_frame, text="explorer.exe",
            style="English.TButton",
            command=start_desktop
    ).grid(row=1, column=0, padx=10, pady=10)

    ttk.Button(buttons_frame, text="taskkill /f /im explorer.exe",
            style="English.TButton",
            command=close_desktop
    ).grid(row=1, column=1, padx=10, pady=10)

    ttk.Button(buttons_frame, text="cmd.exe",
            style="English.TButton",
            command=start_cmd
    ).grid(row=1, column=2, padx=10, pady=10)

    ttk.Button(buttons_frame, text="powershell.exe",
            style="English.TButton",
            command=start_powershell
    ).grid(row=1, column=3, padx=10, pady=10)

# 主窗口 -------------------------------------------------------------------------------------------------------------
root.deiconify()
root.title(WINDOW_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
root.config(bg=WINDOW_BACKGROUND_COLOR)
root.wm_attributes("-topmost", True)
root.wm_attributes("-alpha", WINDOW_ALPHA)
root.resizable(False, False)
root.overrideredirect(True)

root.bind("<ButtonPress-1>", on_press)
root.bind("<B1-Motion>", on_drag)
root.bind("<ButtonRelease-1>", on_release)

# 主框架 -------------------------------------------------------------------------------------------------------------
main_frame = tk.Frame(root, bg=FRAME_BACKGROUND_COLOR)
main_frame.pack(padx=10, pady=10, fill=tk.X)

time_label = tk.Label(
    main_frame,
    text="---",
    font=DISPLAY_FONT,
    justify="left",
    bg=BACKGROUND_COLOR,
    fg=FOREGROUND_COLOR,
    width=8
)

a_label = tk.Label(
    main_frame,
    text="---",
    font=DISPLAY_FONT,
    justify="left",
    bg=BACKGROUND_COLOR,
    fg=FOREGROUND_COLOR,
    width=8
)

b_label = tk.Label(
    main_frame,
    text="---",
    font=DISPLAY_FONT,
    justify="left",
    bg=BACKGROUND_COLOR,
    fg=FOREGROUND_COLOR,
    width=13
)

c_label = tk.Label(
    main_frame,
    text="---",
    font=DISPLAY_FONT,
    justify="left",
    bg=BACKGROUND_COLOR,
    fg=FOREGROUND_COLOR,
    width=10
)

control_panel_button = tk.Button(
    main_frame,
    text="更多",
    font=BUTTON_FONT,
    bg=CONTROL_PANEL_BUTTON_BACKGROUND_COLOR,
    fg=CONTROL_PANEL_BUTTON_FOREGROUND_COLOR,
    command=lambda: open_control_panel()
)

# 小字框架 -------------------------------------------------------------------------------------------------------------
narrow_frame = tk.Frame(root, bg=FRAME_BACKGROUND_COLOR)
narrow_frame.pack(padx=10, pady=0, fill=tk.X)

narrow_date_label = tk.Label(
    narrow_frame,
    text="---",
    font=NARROW_FONT,
    justify="left",
    bg=BACKGROUND_COLOR,
    fg=FOREGROUND_COLOR,
    width=12
)

narrow_b_label = tk.Label(
    narrow_frame,
    text="---",
    font=NARROW_FONT,
    justify="left",
    bg=BACKGROUND_COLOR,
    fg=FOREGROUND_COLOR,
    width=12
)

narrow_c_label = tk.Label(
    narrow_frame,
    text="---",
    font=NARROW_FONT,
    justify="left",
    bg=BACKGROUND_COLOR,
    fg=FOREGROUND_COLOR,
    width=10
)

# 网格布局 -------------------------------------------------------------------------------------------------------------
time_label.grid(row=0, column=0, padx=(5, 10))
a_label.grid(row=0, column=1, padx=(10, 10))
control_panel_button.grid(row=0, column=2, padx=(10, 0))

narrow_date_label.grid(row=0, column=0, padx=(5, 10))
narrow_b_label.grid(row=0, column=1, padx=(10, 10))
narrow_c_label.grid(row=0, column=2, padx=(10, 0))

# 绑定事件 -------------------------------------------------------------------------------------------------------------
time_label.bind("<Double-1>", toggle_fullscreen)

# 主循环 -------------------------------------------------------------------------------------------------------------
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

update_time_and_text()
root.mainloop()

