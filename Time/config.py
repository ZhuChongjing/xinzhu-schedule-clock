from datetime import datetime

schedule = [
    ["数学", "数学", "英语", "英语", "语文", "体锻", "选修", "选修"],
    ["数学", "英语", "地理", "信息", "生物", "体育", "语文", "历史"],
    ["数学", "英语", "体育", "语文", "生物", "语文", "道法", "劳技"],
    ["语文", "历史", "体锻", "音乐", "数学", "数学", "物理", "英语"],
    ["数学", "地理", "美术", "体育", "英语", "心理", "语文", "班会"]
]

def get_weekday():
    weekday = datetime.now().weekday()
    if 0 <= weekday <= 4:
        return weekday
    elif weekday == 5:
        # 临时修改
        # return 
        return weekday
    else:
        # 临时修改
        # return 
        return weekday

before_class = "准备上课"
during_class = "认真听讲"
class_break = "记得擦黑板"

ss = 19
es = 41
