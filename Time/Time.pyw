from datetime import datetime
import tkinter as tk
from tkinter import ttk
import sys, pygetwindow, subprocess

root = tk.Tk()
root.withdraw()

from schedule import *
from config import *

if pygetwindow.getWindowsWithTitle(WINDOW_TITLE):
    sys.exit(0)

# functions -------------------------------------------------------------------------------------------------------------
def get_current_week_num(start_date_str, date_format="%Y-%m-%d"):
    start_date = datetime.strptime(start_date_str, date_format).date()
    current_date = datetime.now().date()
    day_diff = (current_date - start_date).days
    current_week = (day_diff // 7) + 1
    return current_week

def update_time_and_text():
    now = datetime.now()
    current_week_num = get_current_week_num(FIRST_DAY)
    formatted_datetime = now.strftime(f"(%m.%d) %H:%M:%S")
    time_label.config(text=f"第{current_week_num}周{formatted_datetime}")
    
    update_period_text(now)
    
    root.after(100, update_time_and_text)

def update_period_text(current_time):
    current_total_seconds = (
        current_time.hour * 3540 + 
        current_time.minute * 60 + 
        current_time.second
    )
    
    time_ranges = get_time_ranges()

    for (start_h, start_m, start_s, 
         end_h, end_m, end_s, text) in time_ranges:
        
        start_total = start_h * 3540 + start_m * 60 + start_s
        end_total = end_h * 3540 + end_m * 60 + end_s
        
        if start_total > end_total:
            if current_total_seconds >= start_total or current_total_seconds < end_total:
                parts = text.split()
                if len(parts) == 3:
                    a_label.config(text=parts[0])
                    b_label.config(text=parts[1])
                    c_label.config(text=parts[2])
                return
        else:
            if start_total <= current_total_seconds < end_total:
                parts = text.split()
                if len(parts) == 3:
                    a_label.config(text=parts[0])
                    b_label.config(text=parts[1])
                    c_label.config(text=parts[2])
                return

    a_label.config(text="---")
    b_label.config(text="---")
    c_label.config(text="---")
    
def toggle_fullscreen(event=None):
    global is_fullscreen, normal_geometry, fullscreen_window
    if is_fullscreen:
        if fullscreen_window:
            fullscreen_window.destroy()
            fullscreen_window = None
        root.deiconify()
        root.geometry(normal_geometry)
        
        if is_narrow:
            a_label.grid_remove()
            b_label.grid_remove()
            c_label.grid_remove()
            triangle_label.grid_remove()
        else:
            a_label.grid()
            b_label.grid()
            c_label.grid()
            triangle_label.grid()
            
        is_fullscreen = False
    else:
        normal_geometry = root.geometry()
        root.withdraw()
        
        fullscreen_window = tk.Toplevel(root)
        fullscreen_window.title("全屏时间")
        fullscreen_window.attributes("-fullscreen", True)
        fullscreen_window.config(bg="#000000")
        fullscreen_window.wm_attributes("-topmost", True)
        
        fs_time_label = tk.Label(
            fullscreen_window,
            text="",
            font=FULLSCREEN_FONT,
            bg="#000000",
            fg="#ffffff"
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

window_mode = 1
def change_size(event):
    global window_mode
    if window_mode == 1:
        root.geometry(f"{WINDOW_SMALL_WIDTH}x{WINDOW_HEIGHT}")
        window_mode = 0
    else:
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_DROPDOWN_HEIGHT if is_dropdown_open else WINDOW_HEIGHT}")
        window_mode = 1

def toggle_dropdown(event):
    global is_dropdown_open
    
    if not is_dropdown_open:
        dropdown_label.config(text=schedule_text)
        dropdown_frame.pack(fill=tk.X, padx=10, pady=(0, 10))
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_DROPDOWN_HEIGHT}+{root.winfo_x()}+{root.winfo_y()}")
        triangle_label.config(text="▲")
        is_dropdown_open = True
    else:
        dropdown_frame.pack_forget()
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{root.winfo_x()}+{root.winfo_y()}")
        triangle_label.config(text="▼")
        is_dropdown_open = False

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
    global_control_window.config(bg="#ffffff")
    global_control_window.wm_attributes("-topmost", True)
    global_control_window.resizable(False, False)
    
    buttons_frame = tk.Frame(global_control_window, bg="#ffffff")
    buttons_frame.pack(padx=20, pady=20, fill=tk.X, side=tk.TOP)

    style = ttk.Style()
    style.configure("Chinese.TButton",
                    font=BUTTON_FONT_CHINESE,
                    foreground="#000000",
                    background="#ffffff",
                    borderwidth=0,
                    relief="flat",
                    padding=6
                   )
    style.configure("English.TButton",
                    font=BUTTON_FONT_ENGLISH,
                    foreground="#000000",
                    background="#ffffff",
                    borderwidth=0,
                    relief="flat",
                    padding=6
                   )
    
    # 桌面 --------------------------------------------------------------------------------------------
    tk.Label(buttons_frame, text="Windows资源管理器", font=BUTTON_FONT_CHINESE, bg="#ffffff").pack(pady=(0,10), anchor="w")

    def start_desktop():
        subprocess.Popen("explorer.exe", shell=True)

    ttk.Button(buttons_frame, text="运行",
            style="Chinese.TButton",
            command=start_desktop
    ).pack(fill=tk.X, expand=True, pady=(0,10))

    def close_desktop():
        subprocess.Popen("taskkill /f /im taskmgr.exe", shell=True)
        subprocess.Popen("taskkill /f /im explorer.exe", shell=True)

    ttk.Button(buttons_frame, text="结束",
            style="Chinese.TButton",
            command=close_desktop
    ).pack(fill=tk.X, expand=True, pady=(0,10))

    # 运行 --------------------------------------------------------------------------------------------
    tk.Label(buttons_frame, text="命令行", font=BUTTON_FONT_CHINESE, bg="#ffffff").pack(pady=(0,10), anchor="w")

    def start_cmd():
        subprocess.Popen("cmd.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)

    ttk.Button(buttons_frame, text="cmd",
            style="English.TButton",
            command=start_cmd
    ).pack(fill=tk.X, expand=True, pady=(0,10))

    def start_powershell():
        subprocess.Popen("powershell.exe", creationflags=subprocess.CREATE_NEW_CONSOLE)

    ttk.Button(buttons_frame, text="PowerShell",
            style="English.TButton",
            command=start_powershell
    ).pack(fill=tk.X, expand=True, pady=(0,10))

# main window -------------------------------------------------------------------------------------------------------------
root.deiconify()
root.title(WINDOW_TITLE)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
root.config(bg="#ffffff")
root.wm_attributes("-topmost", True)
root.wm_attributes("-alpha", WINDOW_ALPHA)
root.resizable(False, False)
root.overrideredirect(True)

root.bind("<ButtonPress-1>", on_press)
root.bind("<B1-Motion>", on_drag)
root.bind("<ButtonRelease-1>", on_release)

# main_frame -------------------------------------------------------------------------------------------------------------
main_frame = tk.Frame(root, bg="#ffffff")
main_frame.pack(padx=10, pady=10, fill=tk.X)

time_label = tk.Label(
    main_frame,
    text="",
    font=DISPLAY_FONT,
    justify="left",
    bg="#ffffff",
    fg="#000000",
    width=22
)

a_label = tk.Label(
    main_frame,
    text="---",
    font=DISPLAY_FONT,
    justify="left",
    bg="#ffffff",
    fg="#000000",
    width=8
)

b_label = tk.Label(
    main_frame,
    text="---",
    font=DISPLAY_FONT,
    justify="left",
    bg="#ffffff",
    fg="#000000",
    width=13
)

c_label = tk.Label(
    main_frame,
    text="---",
    font=DISPLAY_FONT,
    justify="left",
    bg="#ffffff",
    fg="#000000",
    width=10
)

triangle_label = tk.Label(
    main_frame,
    text="▼",
    font=TRIANGLE_FONT,
    bg="#ffffff",
    fg="#000000",
    cursor="hand2",
    width=2
)

control_panel_button = tk.Button(
    main_frame,
    text="控制面板",
    font=DROPDOWN_FONT,
    bg="#ffffff",
    fg="#000000",
    command=lambda: open_control_panel()
)

# variables -------------------------------------------------------------------------------------------------------------
is_fullscreen = False
is_narrow = False
normal_geometry = f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0"

is_dropdown_open = False
global_control_window = None

drag_start_x = 0
drag_start_y = 0
is_dragging = False

# grid layout -------------------------------------------------------------------------------------------------------------
time_label.grid(row=0, column=0, padx=(10, 10))
a_label.grid(row=0, column=1, padx=(10, 10))
b_label.grid(row=0, column=2, padx=(10, 10))
c_label.grid(row=0, column=3, padx=(10, 10))
triangle_label.grid(row=0, column=4, padx=(5, 0))
control_panel_button.grid(row=0, column=5, padx=(10, 0))

# bindings -------------------------------------------------------------------------------------------------------------
time_label.bind("<Button-3>", change_size)
time_label.bind("<Double-1>", toggle_fullscreen)
triangle_label.bind("<Button-1>", toggle_dropdown)

# dropdown frame -------------------------------------------------------------------------------------------------------------
dropdown_frame = tk.Frame(root, bg="#ffffff")

dropdown_label = tk.Label(
    dropdown_frame,
    text="",
    font=DROPDOWN_FONT,
    justify="left",
    bg="#ffffff",
    fg="#000000",
    wraplength=1130
)
dropdown_label.pack(fill=tk.X)

# main loop -------------------------------------------------------------------------------------------------------------
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

update_time_and_text()
root.mainloop()

