class SaleSystem:
    # workTime=0  # 工作时间
    # freeTime=0  #请假天数
    # level=1  #员工级别
    # money=10    # 本年度销售额
    def score(self,workTime,freeTime,level,money):
        if freeTime>=20:
            return "请假过多，无资格参与考评"
        if workTime>35 or workTime<0:
            return "工作时间输入错误"
        if level not in [1,2,3,4,5]:
            return "员工级别输入错误"
        if money<10:
            return "年度销售总额不合格"
        if money>500:
            return "年度销售总额输入错误"
        if freeTime<=10 and money>=300 and workTime>=3 and level>=3:
            return "5分"
        if freeTime<=10 and money>=300:
            return "4分"
        if freeTime <=15 and money>=200 and workTime>=3 and level>=3:
            return "3分"
        if freeTime <=15 and money>=200:
            return "2分"
        return "1分"

sys = SaleSystem()
def compute(num1,num2,num3,num4):
    t = sys.score(num1,num2,num3,num4)
    return t

if __name__ == '__main__':
    compute()