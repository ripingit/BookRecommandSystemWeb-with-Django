import requests
from lxml.html import etree
html = '''
<div><div class="item"><a onclick="ajaxget('TP3');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP3 </a><a target="dt" href="http://opac.szpt.edu.cn:8991/F/PCS1564XVGETICFMF3M6J53I3MKFAKQHNG846HJ5BPI7XQ7KS4-73173?func=find-b&amp;request=TP3%3F&amp;local_base=SZY01&amp;find_code=CLC" onclick="addsid(this)" url="?func=find-b&amp;request=TP3%3F">计算技术、计算机技术</a></div><div class="lvl" id="TP3" style=""><div><div class="item"><a onclick="ajaxget('TP30');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP30 </a><a target="dt" href="http://opac.szpt.edu.cn:8991/F/PCS1564XVGETICFMF3M6J53I3MKFAKQHNG846HJ5BPI7XQ7KS4-73173?func=find-b&amp;request=TP30%3F&amp;local_base=SZY01&amp;find_code=CLC" onclick="addsid(this)" url="?func=find-b&amp;request=TP30%3F">一般性问题</a></div><div class="lvl" id="TP30" style=""><div><div class="item"><a onclick="ajaxget('TP301');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP301 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP301%3F">理论、方法</a></div><div class="lvl" id="TP301" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP301.1 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP301.1%3F">自动机理论</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP301.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP301.2%3F">形式语言理论</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP301.4 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP301.4%3F">可计算性理论</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP301.5 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP301.5%3F">计算复杂性理论</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP301.6 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP301.6%3F">算法理论</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP302');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP302 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP302%3F">设计与性能分析</a></div><div class="lvl" id="TP302" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP302.1 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP302.1%3F">总体设计、系统设计</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP302.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP302.2%3F">逻辑设计</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP302.4 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP302.4%3F">制图</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP302.7 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP302.7%3F">性能分析、功能分析</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP302.8 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP302.8%3F">容错技术</a></div></div>
</div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP303 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP303%3F">总体结构、系统构造</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP304 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP304%3F">材料</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP305 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP305%3F">制造、装配、改造</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP306 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP306%3F">调整、测试、校验</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP307 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP307%3F">检修、维护</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP308 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP308%3F">机房</a></div></div>
<div><div class="item"><a onclick="ajaxget('TP309');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP309 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP309%3F">安全保密</a></div><div class="lvl" id="TP309" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP309.1 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP309.1%3F">计算机设备安全</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP309.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP309.2%3F">数据安全</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP309.3 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP309.3%3F">数据备份与恢复</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP309.5 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP309.5%3F">计算机病毒与防治</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP309.7 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP309.7%3F">加密与解密</a></div></div>
</div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP31');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP31 </a><a target="dt" href="http://opac.szpt.edu.cn:8991/F/PCS1564XVGETICFMF3M6J53I3MKFAKQHNG846HJ5BPI7XQ7KS4-73173?func=find-b&amp;request=TP31%3F&amp;local_base=SZY01&amp;find_code=CLC" onclick="addsid(this)" url="?func=find-b&amp;request=TP31%3F">计算机软件</a></div><div class="lvl" id="TP31" style=""><div><div class="item"><a onclick="ajaxget('TP311');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP311 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP311%3F">程序设计、软件工程</a></div><div class="lvl" id="TP311" style=""><div><div class="item"><a onclick="ajaxget('TP311.1');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP311.1 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP311.1%3F">程序设计</a></div><div class="lvl" id="TP311.1" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP311.11 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP311.11%3F">程序设计方法</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP311.12 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP311.12%3F">数据结构</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP311.13 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP311.13%3F">数据库理论与系统</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP311.5');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP311.5 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP311.5%3F">软件工程</a></div><div class="lvl" id="TP311.5" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP311.51 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP311.51%3F">程序设计自动化</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP311.52 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP311.52%3F">软件开发</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP311.54 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP311.54%3F">软件移植</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP311.56 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP311.56%3F">软件工具、工具软件</a></div></div>
</div></div>
</div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP312 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP312%3F">程序语言、算法语言</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP313 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP313%3F">汇编程序</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP314 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP314%3F">编译程、解释程序</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP315 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP315%3F">管理程序、管理系统</a></div></div>
<div><div class="item"><a onclick="ajaxget('TP316');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP316 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316%3F">操作系统</a></div><div class="lvl" id="TP316" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.1 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.1%3F">分时操作系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.2%3F">实时操作系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.3 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.3%3F">批处理</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.4 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.4%3F">分布式操作系统、并行式操作系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.5 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.5%3F">多媒体操作系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.6 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.6%3F">DOS操作系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.7 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.7%3F">Windows操作系统</a></div></div>
<div><div class="item"><a onclick="ajaxget('TP316.8');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP316.8 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.8%3F">网络操作系统</a></div><div class="lvl" id="TP316.8" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.81 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.81%3F">UNIX操作系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.82 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.82%3F">XENIX操作系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.83 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.83%3F">NOVELL操作系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.84 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.84%3F">OS/2操作系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.86 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.86%3F">Windows NT操作系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.89 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.89%3F">其他</a></div></div>
</div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP316.9 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP316.9%3F">中文操作系统</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP317');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP317 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP317%3F">程序包（应用软件）</a></div><div class="lvl" id="TP317" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP317.1 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP317.1%3F">办公自动化系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP317.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP317.2%3F">文字处理软件</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP317.3 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP317.3%3F">表处理软件</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP317.4 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP317.4%3F">图像处理软件</a></div></div>
</div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP319 <a target="dt" href="http://opac.szpt.edu.cn:8991/F/PCS1564XVGETICFMF3M6J53I3MKFAKQHNG846HJ5BPI7XQ7KS4-73173?func=find-b&amp;request=TP319%3F&amp;local_base=SZY01&amp;find_code=CLC" onclick="addsid(this)" url="?func=find-b&amp;request=TP319%3F">专用应用程序</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP32');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP32 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP32%3F">一般-计算器和计算机</a></div><div class="lvl" id="TP32" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP321 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP321%3F">非电子计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP322 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP322%3F">分析计算机(穿孔卡计算机)</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP323 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP323%3F">电子计算器</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP33');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP33 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP33%3F">电子数字计算机（不连续作用电子计算机）</a></div><div class="lvl" id="TP33" style=""><div><div class="item"><a onclick="ajaxget('TP331');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP331 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP331%3F">基本电路</a></div><div class="lvl" id="TP331" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP331.1 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP331.1%3F">逻辑电路</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP332');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP332 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP332%3F">运算器、控制器（CPU）</a></div><div class="lvl" id="TP332" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP332.1 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP332.1%3F">逻辑部件</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP332.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP332.2%3F">运算器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP332.3 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP332.3%3F">控制器、控制台</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP333');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP333 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP333%3F">存贮器</a></div><div class="lvl" id="TP333" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP333.1 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP333.1%3F">内存贮器(主存贮器)总论</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP333.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP333.2%3F">外存贮器(辅助存贮器)总论</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP333.3 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP333.3%3F">磁存贮器及其驱动器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP333.4 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP333.4%3F">光存贮器及其驱动器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP333.5 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP333.5%3F">半导体集成电路存贮器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP333.6 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP333.6%3F">起导体存贮器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP333.7 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP333.7%3F">只读(ROM)存贮器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP333.8 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP333.8%3F">随机存取存贮器</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP334');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP334 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP334%3F">外部设备</a></div><div class="lvl" id="TP334" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP334.1 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP334.1%3F">终端设备</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP334.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP334.2%3F">输入设备</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP334.3 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP334.3%3F">输入设备</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP334.4 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP334.4%3F">输入输出控制器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP334.5 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP334.5%3F">外存储器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP334.7 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP334.7%3F">接口装置、插件</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP334.8 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP334.8%3F">打印装置</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP334.9 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP334.9%3F">其他</a></div></div>
</div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP335 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP335%3F">信息转换及其设备</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP336 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP336%3F">总线、通道</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP337 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP337%3F">仿真器</a></div></div>
<div><div class="item"><a onclick="ajaxget('TP338');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP338 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP338%3F">各种电子数字计算机</a></div><div class="lvl" id="TP338" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP338.1 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP338.1%3F">微型计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP338.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP338.2%3F">小型计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP338.3 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP338.3%3F">中型计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP338.4 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP338.4%3F">大型计算机、巨型计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP338.6 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP338.6%3F">并行计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP338.7 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP338.7%3F">陈列式计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP338.8 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP338.8%3F">分布式计算机</a></div></div>
</div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP34');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP34 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP34%3F">电子模拟计算机（连续作用电子计算机)</a></div><div class="lvl" id="TP34" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP342 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP342%3F">运算放大器和控制器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP343 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP343%3F">存贮器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP344 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP344%3F">输入器、输出器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP346 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP346%3F">函数发生器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP347 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP347%3F">延时器</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP348 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP348%3F">各种电子模拟计算机</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP35');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP35 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP35%3F">混合电子计算机</a></div><div class="lvl" id="TP35" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP352 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP352%3F">数字-模拟计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP353 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP353%3F">模拟-数字计算机</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP36');shift(this)"><span><img src="/opac_lcl_chi/dircs.gif"></span>TP36 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP36%3F">微型计算机</a></div><div class="lvl" id="TP36" style="display:none"></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP37 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP37%3F">多媒体技术与多媒体计算机</a></div></div>
<div><div class="item"><a onclick="ajaxget('TP38');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP38 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP38%3F">其他计算机</a></div><div class="lvl" id="TP38" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP381 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP381%3F">激光计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP382 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP382%3F">射流计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP383 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP383%3F">超导计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP384 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP384%3F">分子计算机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP387 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP387%3F">第五代计算机</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP39');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP39 </a><a target="dt" href="http://opac.szpt.edu.cn:8991/F/PCS1564XVGETICFMF3M6J53I3MKFAKQHNG846HJ5BPI7XQ7KS4-73173?func=find-b&amp;request=TP39%3F&amp;local_base=SZY01&amp;find_code=CLC" onclick="addsid(this)" url="?func=find-b&amp;request=TP39%3F">计算机的应用</a></div><div class="lvl" id="TP39" style=""><div><div class="item"><a onclick="ajaxget('TP391');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP391 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391%3F">信息处理(信息加工）</a></div><div class="lvl" id="TP391" style=""><div><div class="item"><a onclick="ajaxget('TP391.1');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP391.1 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.1%3F">文字信息处理</a></div><div class="lvl" id="TP391.1" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.11 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.11%3F">汉字信息编码</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.12 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.12%3F">汉字处理系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.13 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.13%3F">表格处理系统</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.14 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.14%3F">文字录入技术</a></div></div>
</div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.2%3F">翻译机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.3 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.3%3F">检索机</a></div></div>
<div><div class="item"><a onclick="ajaxget('TP391.4');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP391.4 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.4%3F">模型识别与装置</a></div><div class="lvl" id="TP391.4" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.41 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.41%3F">图像识别及其装置</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.42 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.42%3F">声音识别及其装置</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.43 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.43%3F">文字识别及其装置</a></div></div>
</div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.5 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.5%3F">诊断机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.6 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.6%3F">教学机</a></div></div>
<div><div class="item"><a onclick="ajaxget('TP391.7');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP391.7 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.7%3F">机器辅助技术</a></div><div class="lvl" id="TP391.7" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.72 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.72%3F">机器辅助设计(CAD)、辅助制图</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.73 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.73%3F">机器辅助制造(CAM)</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.75 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.75%3F">机器辅助计算(CAC)</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.76 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.76%3F">机器辅助测试（CAT）</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.77 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.77%3F">机器辅助分析（CAA）</a></div></div>
</div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.8 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.8%3F">控制机</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP391.9 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP391.9%3F">计算机仿真机</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP393');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP393 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393%3F">计算机网络</a></div><div class="lvl" id="TP393" style=""><div><div class="item"><a onclick="ajaxget('TP393.0');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP393.0 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.0%3F">一般性问题</a></div><div class="lvl" id="TP393.0" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.02 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.02%3F">计算机网络结构与设计</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.03 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.03%3F">网络互连技术</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.04 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.04%3F">通信规程、通信协议</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.05 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.05%3F">网络设备</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.06 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.06%3F">计算机网络测试、运行</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.07 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.07%3F">计算机网络管理</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.08 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.08%3F">计算机网络安全</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.09 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.09%3F">计算机网络应用程序</a></div></div>
</div></div>
<div><div class="item"><a onclick="ajaxget('TP393.1');shift(this)"><span><img src="/opac_lcl_chi/diros.gif"></span>TP393.1 </a><a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.1%3F">局部网(LAN)、城域网（MAN）</a></div><div class="lvl" id="TP393.1" style=""><div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.11 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.11%3F">以太网</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.12 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.12%3F">令牌网</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.13 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.13%3F">DQDB网（分布队列双总线网络）</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.14 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.14%3F">FDDI网（高速光纤环网）</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.15 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.15%3F">ATM局域网</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.17 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.17%3F">无线局域网</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.18 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.18%3F">校园网、企业网（Ineranet）</a></div></div>
</div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.2 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.2%3F">广域网（WAN）</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.3 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.3%3F">洲际网络</a></div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP393.4 <a target="dt" href="#" onclick="addsid(this)" url="?func=find-b&amp;request=TP393.4%3F">国际互联网</a></div></div>
</div></div>
<div><div class="item"><img src="/opac_lcl_chi/dircb.gif">TP399 <a target="dt" href="http://opac.szpt.edu.cn:8991/F/PCS1564XVGETICFMF3M6J53I3MKFAKQHNG846HJ5BPI7XQ7KS4-73173?func=find-b&amp;request=TP399%3F&amp;local_base=SZY01&amp;find_code=CLC" onclick="addsid(this)" url="?func=find-b&amp;request=TP399%3F">在其他方面的应用</a></div></div>
</div></div>
</div></div>
'''

# selector = etree.HTML(html)
#
# print(selector.xpath('//div[@class="item"]//text()'))
# l2 = (selector.xpath('//div[@class="item"]/text()'))
# l2 = [i.strip() for i in l2]
#
# print(l2)
#
# l = selector.xpath('//div[@class="item"]//text()')
#
# result = {}
#
# index = 0
# while index < len(l)-1:
#     result[l[index].strip()] = l[index+1].strip()
#     index += 2
# print(result)
#
# waitFindStr = 'TP311.11'
#
# print(waitFindStr.find('TP3'))
#
# resultStr = []
# for key,value in result.items():
#     print(key)
#     if waitFindStr.find(key)!=-1:
#         resultStr.append(value)
# print(resultStr)
#
#
#


# # 获取秘钥
# keyUrl = 'http://opac.szpt.edu.cn:8991/F'
# response = requests.get(url=keyUrl)
# response.encoding = 'utf-8'
# print(response.text)
# selector = etree.HTML(response.text)
# secretKey = selector.xpath('//form/@action')[0]
# startIndex = secretKey.find('/F/')+3
# secretKey = secretKey[startIndex:]
# print(secretKey)

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'yunsuo_session_verify=d21eb089dde2f05fd34ee94b269914f2',
    'Host': 'opac.szpt.edu.cn:8991',
    'Referer': 'http://opac.szpt.edu.cn:8991/F',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
cookies = {
    'yunsuo_session_verify': 'd21eb089dde2f05fd34ee94b269914f2'
}
# import re
# url = 'http://opac.szpt.edu.cn:8991/F/KAJGMA6CRVR4Q4Y346RS1FF12QYD4KIADIB9E2PRFGKLQJ82T9-13647?func=short-jump&jump=61&pag=now'
# m = re.search('jump=(\d+)',url)
# print(m.group(1))
# url = 'http://opac.szpt.edu.cn:8991/F/F7V1749GED1DFGAST95YIR7KPFGJ6K9I5JAYXCEMU3YNGEV362-94520?func=full-set-set&set_number=000708&set_entry=000008&format=999'
# response = requests.get(url)
# response.encoding = 'utf-8'
# selector = etree.HTML(response.text)
# html = selector.xpath('//script[contains(text(),"下一条记录")]/text()')[0]
# selector = etree.HTML(html)
# print(selector.xpath('//a/@href')[0])
# print(''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"出版发行")]//text()')).split(',')[1].strip())
# response =requests.get(url,headers=headers)
# response.encoding = 'utf-8'
# selector = etree.HTML(response.text)
# s = (''.join(selector.xpath('//div[@id="hitnum"]/text()'))).strip().replace(' ', '')
# m = re.search('of(\d+?)\(', s)
# print(m.group(1))
# nextJump = 1
# nextUrl = (selector.xpath('//div[@id="hitnum"]//script//text()')[0].split(',')[3][1:-3]+"{}&pag=now").format(nextJump)
# print(nextUrl)

# url = 'http://opac.szpt.edu.cn:8991/F/3IB5U8MA7DNF6UQLA49SSHKQLC9HNLHVPEJV4MJN9KETBYN8KV-37101?func=short-jump&jump=41&pag=now'
#
# response = requests.get(url=url)
# response.encoding = 'utf-8'
# print(response.text)
#
# selector = etree.HTML(response.text)
#
# import re
# print(selector.xpath('//div[@id="hitnum"]//script//text()')[0].split(',')[3][1:-3]+"{}")
# m = re.search('jump=(.*?)&',url)
# print(m.group(1))
#


# items = selector.xpath('//table[@class="items"]//td[@class="col2"]')
# for item in items:
#     bookName = (item.xpath('.//div[@class="itemtitle"]/a/text()'))[0].strip()
#     author = item.xpath('.//td[@class="content" and contains(preceding-sibling::td[1]/text(),"作者")]/text()')[0].strip()
#     index = item.xpath('.//td[@class="content" and contains(preceding-sibling::td[1]/text(),"索书号")]/text()')[0].strip()
#     publisher = item.xpath('.//td[@class="content" and contains(preceding-sibling::td[1]/text(),"出版社")]/text()')[0].strip()
#     publishYear = item.xpath('.//td[@class="content" and contains(preceding-sibling::td[1]/text(),"年份")]/text()')[0].strip()
#     bookUrl = item.xpath('.//div[@class="itemtitle"]/a/@href')[0].strip()
#
#     print('书名:',bookName,'\n','索书号:',index,'\n','出版社:',publisher,'\n','年份:',publishYear,'\n')




# response = requests.get(url)
# response.encoding = 'utf-8'
#
# print(response.text)
#
# selector = etree.HTML(response.text)
#
# print(''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"摘要")]//text()')).strip())
# print(''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"个人著者")]//text()')).strip())
# print(''.join(selector.xpath('//td[@class="td1" and preceding-sibling::td[1]//text()="\n\xa0\n"]//text()')).strip())
#
# isbn = (''.join(selector.xpath('//td[@class="td1" and contains(preceding-sibling::td[1]//text(),"ISBN")]//text()')).strip())
# print(isbn.split('\xa0')[0].replace('-',''))

bookNumber = {'TP3': '计算技术、计算机技术', 'TP30': '一般性问题', 'TP301': '理论、方法', 'TP301.1': '自动机理论', 'TP301.2': '形式语言理论',
                   'TP301.4': '可计算性理论', 'TP301.5': '计算复杂性理论', 'TP301.6': '算法理论', 'TP302': '设计与性能分析',
                   'TP302.1': '总体设计、系统设计', 'TP302.2': '逻辑设计', 'TP302.4': '制图', 'TP302.7': '性能分析、功能分析',
                   'TP302.8': '容错技术', 'TP303': '总体结构、系统构造', 'TP304': '材料', 'TP305': '制造、装配、改造', 'TP306': '调整、测试、校验',
                   'TP307': '检修、维护', 'TP308': '机房', 'TP309': '安全保密', 'TP309.1': '计算机设备安全', 'TP309.2': '数据安全',
                   'TP309.3': '数据备份与恢复', 'TP309.5': '计算机病毒与防治', 'TP309.7': '加密与解密', 'TP31': '计算机软件',
                   'TP311': '程序设计、软件工程', 'TP311.1': '程序设计', 'TP311.11': '程序设计方法', 'TP311.12': '数据结构',
                   'TP311.13': '数据库理论与系统', 'TP311.5': '软件工程', 'TP311.51': '程序设计自动化', 'TP311.52': '软件开发',
                   'TP311.54': '软件移植', 'TP311.56': '软件工具、工具软件', 'TP312': '程序语言、算法语言', 'TP313': '汇编程序',
                   'TP314': '编译程、解释程序', 'TP315': '管理程序、管理系统', 'TP316': '操作系统', 'TP316.1': '分时操作系统', 'TP316.2': '实时操作系统',
                   'TP316.3': '批处理', 'TP316.4': '分布式操作系统、并行式操作系统', 'TP316.5': '多媒体操作系统', 'TP316.6': 'DOS操作系统',
                   'TP316.7': 'Windows操作系统', 'TP316.8': '网络操作系统', 'TP316.81': 'UNIX操作系统', 'TP316.82': 'XENIX操作系统',
                   'TP316.83': 'NOVELL操作系统', 'TP316.84': 'OS/2操作系统', 'TP316.86': 'Windows NT操作系统', 'TP316.89': '其他',
                   'TP316.9': '中文操作系统', 'TP317': '程序包（应用软件）', 'TP317.1': '办公自动化系统', 'TP317.2': '文字处理软件',
                   'TP317.3': '表处理软件', 'TP317.4': '图像处理软件', 'TP319': '专用应用程序', 'TP32': '一般-计算器和计算机', 'TP321': '非电子计算机',
                   'TP322': '分析计算机(穿孔卡计算机)', 'TP323': '电子计算器', 'TP33': '电子数字计算机（不连续作用电子计算机）', 'TP331': '基本电路',
                   'TP331.1': '逻辑电路', 'TP332': '运算器、控制器（CPU）', 'TP332.1': '逻辑部件', 'TP332.2': '运算器',
                   'TP332.3': '控制器、控制台', 'TP333': '存贮器', 'TP333.1': '内存贮器(主存贮器)总论', 'TP333.2': '外存贮器(辅助存贮器)总论',
                   'TP333.3': '磁存贮器及其驱动器', 'TP333.4': '光存贮器及其驱动器', 'TP333.5': '半导体集成电路存贮器', 'TP333.6': '起导体存贮器',
                   'TP333.7': '只读(ROM)存贮器', 'TP333.8': '随机存取存贮器', 'TP334': '外部设备', 'TP334.1': '终端设备', 'TP334.2': '输入设备',
                   'TP334.3': '输入设备', 'TP334.4': '输入输出控制器', 'TP334.5': '外存储器', 'TP334.7': '接口装置、插件', 'TP334.8': '打印装置',
                   'TP334.9': '其他', 'TP335': '信息转换及其设备', 'TP336': '总线、通道', 'TP337': '仿真器', 'TP338': '各种电子数字计算机',
                   'TP338.1': '微型计算机', 'TP338.2': '小型计算机', 'TP338.3': '中型计算机', 'TP338.4': '大型计算机、巨型计算机',
                   'TP338.6': '并行计算机', 'TP338.7': '陈列式计算机', 'TP338.8': '分布式计算机', 'TP34': '电子模拟计算机（连续作用电子计算机)',
                   'TP342': '运算放大器和控制器', 'TP343': '存贮器', 'TP344': '输入器、输出器', 'TP346': '函数发生器', 'TP347': '延时器',
                   'TP348': '各种电子模拟计算机', 'TP35': '混合电子计算机', 'TP352': '数字-模拟计算机', 'TP353': '模拟-数字计算机', 'TP36': '微型计算机',
                   'TP37': '多媒体技术与多媒体计算机', 'TP38': '其他计算机', 'TP381': '激光计算机', 'TP382': '射流计算机', 'TP383': '超导计算机',
                   'TP384': '分子计算机', 'TP387': '第五代计算机', 'TP39': '计算机的应用', 'TP391': '信息处理(信息加工）', 'TP391.1': '文字信息处理',
                   'TP391.11': '汉字信息编码', 'TP391.12': '汉字处理系统', 'TP391.13': '表格处理系统', 'TP391.14': '文字录入技术',
                   'TP391.2': '翻译机', 'TP391.3': '检索机', 'TP391.4': '模型识别与装置', 'TP391.41': '图像识别及其装置',
                   'TP391.42': '声音识别及其装置', 'TP391.43': '文字识别及其装置', 'TP391.5': '诊断机', 'TP391.6': '教学机',
                   'TP391.7': '机器辅助技术', 'TP391.72': '机器辅助设计(CAD)、辅助制图', 'TP391.73': '机器辅助制造(CAM)',
                   'TP391.75': '机器辅助计算(CAC)', 'TP391.76': '机器辅助测试（CAT）', 'TP391.77': '机器辅助分析（CAA）', 'TP391.8': '控制机',
                   'TP391.9': '计算机仿真机', 'TP393': '计算机网络', 'TP393.0': '一般性问题', 'TP393.02': '计算机网络结构与设计',
                   'TP393.03': '网络互连技术', 'TP393.04': '通信规程、通信协议', 'TP393.05': '网络设备', 'TP393.06': '计算机网络测试、运行',
                   'TP393.07': '计算机网络管理', 'TP393.08': '计算机网络安全', 'TP393.09': '计算机网络应用程序',
                   'TP393.1': '局部网(LAN)、城域网（MAN）', 'TP393.11': '以太网', 'TP393.12': '令牌网', 'TP393.13': 'DQDB网（分布队列双总线网络）',
                   'TP393.14': 'FDDI网（高速光纤环网）', 'TP393.15': 'ATM局域网', 'TP393.17': '无线局域网',
                   'TP393.18': '校园网、企业网（Ineranet）', 'TP393.2': '广域网（WAN）', 'TP393.3': '洲际网络', 'TP393.4': '国际互联网',
                   'TP399': '在其他方面的应用'}

# 要搜索的图书的分类号
searchNumber = ['TP317.5', 'TP317.6', 'TP301.5', 'TP301.2', 'TP302.2', 'TP302.7', 'TP302.8', 'TP303', 'TP305', 'TP307',
                'TP306', 'TP308', 'TP309.2', 'TP309.3', 'TP309.5', 'TP309.7', 'TP311.51', 'TP311.11', 'TP311.12',
                'TP311.13', 'TP311.52', 'TP311.56', 'TP313', 'TP316.1', 'TP315', 'TP314', 'TP316.2', 'TP316.3', 'TP312',
                'TP316.4', 'TP316.6', 'TP316.81', 'TP316.83', 'TP316.9', 'TP316.84', 'TP316.86', 'TP316.89', 'TP317.2',
                'TP317.1', 'TP317.3', 'TP316.7', 'TP319', 'TP331.1', 'TP323', 'TP332.2', 'TP332.3', 'TP333.1',
                'TP333.2', 'TP333.3', 'TP332.1', 'TP333.5', 'TP333.4', 'TP334.1', 'TP334.3', 'TP334.2', 'TP334.7',
                'TP334.8', 'TP335', 'TP336', 'TP338.2', 'TP338.3', 'TP338.4', 'TP338.7', 'TP338.6', 'TP338.8', 'TP37',
                'TP381', 'TP387', 'TP391.12', 'TP391.2', 'TP391.14', 'TP391.3', 'TP391.13', 'TP391.42', 'TP391.43',
                'TP391.6', 'TP391.41', 'TP391.72', 'TP391.76', 'TP391.73', 'TP391.75', 'TP391.9', 'TP393.03',
                'TP393.02', 'TP393.06', 'TP393.07', 'TP393.08', 'TP393.11', 'TP393.09', 'TP393.18', 'TP393.2', 'TP399',
                'TP393.4', 'TP301.6']

print(len(searchNumber))
for key, value in bookNumber.items():
    if key not in searchNumber:
        searchNumber.append(key)

print(searchNumber)
print(len(searchNumber))