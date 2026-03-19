def map_replace(input_file, output_file, from_list, to_list):
    """
    根据提供的映射关系替换文件内容
    
    参数:
        input_file: 要处理的输入文件路径
        output_file: 输出文件路径
        from_list: 要查找的字符串列表
        to_list: 对应的替换字符串列表
    """
    # 检查映射列表长度是否一致
    if len(from_list) != len(to_list):
        print("错误：from列表和to列表长度不一致！")
        return False
    
    # 创建映射字典（原字符串 -> 新字符串）
    replace_map = dict(zip(from_list, to_list))
    
    try:
        # 读取输入文件
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 执行替换
        for old, new in replace_map.items():
            content = content.replace(old, new)
        
        # 写入输出文件
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"替换完成！结果已保存到 {output_file}")
        return True
    
    except Exception as e:
        print(f"发生错误: {str(e)}")
        return False
###############################################################################

# 你的映射数据
from_str = """
171_saibotutengzhu.png
171_SCPsuipian.png
172_fuzhibaojing.png
172_SCPsuipian.png
173_mengjingpintu.png
173_SCPsuipian.png
174_jiyinbianjiqi.png
174_SCPsuipian.png
175_SCPsuipian.png
175_shouhuozhilu.png
176_SCPsuipian.png
176_wuxianyinfu.png
177_SCPsuipian.png
177_yuzhouluopan.png
178_chongdongtanceqi.png
178_SCPsuipian.png
179_anwuzhiyuanquan.png
179_SCPsuipian.png
180_SCPsuipian.png
180_xukongzhisuo.png
181_jufengzhizhong.png
181_SCPsuipian.png
182_SCPsuipian.png
182_taiyangxidingweiqi.png
183_SCPsuipian.png
183_zhaohuangudi.png
184_anyingfengchao.png
184_SCPsuipian.png
185_SCPsuipian.png
185_xingjifubiao.png
186_SCPsuipian.png
186_shiluozhimen.png
187_jixiemifeng.png
187_SCPsuipian.png
188_fangshengrenou.png
188_SCPsuipian.png
189_SCPsuipian.png
189_shiqianhuozhong.png
190_jueduimingzhongfuwen.png
190_SCPsuipian.png
191_qiheifadian.png
191_SCPsuipian.png
192_SCPsuipian.png
192_zhaomingtoudeng.png
193_kaisuogongju.png
193_SCPsuipian.png
194_SCPsuipian.png
194_suojiangdeziwoxiuyang.png
"""

to_str = """
201_jiyibianjiqi.png
201_SCPsuipian.png
202_SCPsuipian.png
202_shijianhuisuchilun.png
203_kongjianhuisuchilun.png
203_SCPsuipian.png
204_mengjingxianyingye.png
204_SCPsuipian.png
205_feixingqijiaonang.png
205_SCPsuipian.png
206_naojixinpian.png
206_SCPsuipian.png
207_SCPsuipian.png
207_xingguichegnkeka.png
208_bianxieshijijiaxiang.png
208_SCPsuipian.png
209_oumijianenglianghexin.png
209_SCPsuipian.png
210_SCPsuipian.png
210_shiwangmotouyingmeitong.png
211_chaoxingxituanlaoyin.png
211_SCPsuipian.png
212_jingjiwangguan.png
212_SCPsuipian.png
213_jueduijingzhizhimao.png
213_SCPsuipian.png
214_SCPsuipian.png
214_wuxianfangyulichang.png
215_SCPsuipian.png
215_wenmingshachaqi.png
216_SCPsuipian.png
216_yongdongji.png
217_jueduilingduzhibing.png
217_SCPsuipian.png
218_SCPsuipian.png
218_zuizhongrongyuxunzhang.png
219_qulvyinqing.png
219_SCPsuipian.png
220_fuzhirenpeiyangcang.png
220_SCPsuipian.png
221_kemengdehuiyilu.png
221_SCPsuipian.png
222_jingdiandianyingyingpan.png
222_SCPsuipian.png
223_SCPsuipian.png
223_zhumingyouxikadai.png
224_SCPsuipian.png
224_zhencangdeyingji.png
"""

# 处理映射数据
from_list = [line.strip() for line in from_str.split('\n') if line.strip()]
to_list = [line.strip() for line in to_str.split('\n') if line.strip()]

# 使用示例
input_file = 'collection.html'    # 输入文件
output_file = 'collection--.html'  # 输出文件

# 执行替换
map_replace(input_file, output_file, from_list, to_list)