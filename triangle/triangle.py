class Triangle:
    def isornot(self,a,b,c):
        if 0 < a <= 100 and 0 < b <= 100 and 0 < c <= 100 and a + c > b and a + b > c and c + b > a:
            return "是"
        else:
            return "否"

    def type(self, a, b, c):
        if a == 0:
            return "第一条边不能为0"
        if b == 0:
            return "第二条边不能为0"
        if c == 0:
            return "第三条边不能为0"
        if a < 0:
            return "第一条边不能小于0"
        if b < 0:
            return "第二条边不能小于0"
        if c < 0:
            return "第三条边不能小于0"
        if a > 100:
            return "第一条边超出了边界"
        if b > 100:
            return "第二条边超出了边界"
        if c > 100:
            return "第三条边超出了边界"
        if a + c > b and a + b > c and c + b > a:
            if a == b == c:
                return "等边三角形"
            elif a == b or b == c or a == c:
                return "等腰三角形"
            else:
                return "一般三角形"
        else:
            return "不构成三角形"


def compute(a, b, c):
    a = float(a)
    b = float(b)
    c = float(c)
    t = Triangle().type(a, b, c)  # 实例化三角形
    return t

def judge(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    t = Triangle().isornot(a, b, c)  # 实例化三角形
    return t