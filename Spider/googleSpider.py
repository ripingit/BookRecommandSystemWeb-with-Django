import execjs
import requests

class GoogleSpider():
    def __init__(self):
        self.ctx = execjs.compile("""
        function TL(a) {
        var k = "";
        var b = 406644;
        var b1 = 3293161072;
    
        var jd = ".";
        var $b = "+-a^+6";
        var Zb = "+-3^+b+-f";
    
        for (var e = [], f = 0, g = 0; g < a.length; g++) {
            var m = a.charCodeAt(g);
            128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023),
            e[f++] = m >> 18 | 240,
            e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224,
            e[f++] = m >> 6 & 63 | 128),
            e[f++] = m & 63 | 128)
        }
        a = b;
        for (f = 0; f < e.length; f++) a += e[f],
        a = RL(a, $b);
        a = RL(a, Zb);
        a ^= b1 || 0;
        0 > a && (a = (a & 2147483647) + 2147483648);
        a %= 1E6;
        return a.toString() + jd + (a ^ b)
    };
    
    function RL(a, b) {
        var t = "a";
        var Yb = "+";
        for (var c = 0; c < b.length - 2; c += 3) {
            var d = b.charAt(c + 2),
            d = d >= t ? d.charCodeAt(0) - 87 : Number(d),
            d = b.charAt(c + 1) == Yb ? a >>> d: a << d;
            a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d
        }
        return a
    }
    """)


    def getTk(self, text):
        return self.ctx.call("TL", text)

    # 返回音频文件的content
    def getAudio(self,text:str):
        tk = self.getTk(text)
        url = 'https://translate.google.cn/translate_tts?ie=UTF-8&q={text}&tl=zh-CN&total=1&idx=0&textlen={textlen}&tk={tk}&client=t&prev=input'
        headers={
            'Accept-Encoding': 'identity;q=1, *;q=0',
            'chrome-proxy': 'frfr',
            'Range': 'bytes=0-',
            'Referer': 'https://translate.google.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        }
        response = requests.get(url.format(text=text,textlen=len(text),tk=tk),headers=headers)

        return response.content
if __name__ == "__main__":
    a = GoogleSpider()
    a.getAudio('鸡兔同笼问题')

