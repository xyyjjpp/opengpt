from datetime import datetime

#代理
base_url = 'https://oneapi.xty.app/v1';
# 这里是数据保存路径
out_path = '/Users/Administrator/Desktop/gpt/date/'
# 这里是关键词文件路径，一行一个，编码utf8
file_path = '/Users/Administrator/Desktop/gpt/keywords.txt'
# 这里存放自己的apikey
API_KEYS_PATH = '/Users/Administrator/Desktop/gpt/apikey.txt'
# 生成指令存放文件路径
zl_path = '/Users/Administrator/Desktop/gpt/训练语法.txt'
# 图片开关 0关闭 1打开
pic_switch = 0
# 补全图片路径
date_str = datetime.now().strftime('%Y%m%d')
pic_path = f'/{date_str}/'
# 图片广告水印
logo = '开发时常两年半'
# 标题链接符
title_ljf_f = '-'
title_ljf_b = ''
# 多线程数量设置,默认5个线程，最大并发设置区间400-500
max_thr_num = 10
# 0代表单标题，使用chatgpt生成的标题保存
# 1代表双标题，使用关键词+chatgpt生成的标题组合
# 2代表关键词标题，使用关键词作为标题
title_mode = 1