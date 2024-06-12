class SaleSystem:
    AnnualSales=0
    CommissionRate=0
    Commission=0

    def calculatedCommision(self):
        self.Commission=self.AnnualSales/self.CommissionRate


def compute(AnnualSales, LeaveDays, CashtoAccountRate):
    saleSystem = SaleSystem()  # 实例化销售系统
    saleSystem.AnnualSales=AnnualSales
    if(AnnualSales<0):
        return "年销售额不能为负数"
    if(LeaveDays<0):
        return "请假天数不能为负数"
    if(CashtoAccountRate<0 or CashtoAccountRate>1):
        return "现金到账率必须为0-1的系数"

    if(AnnualSales>200 and LeaveDays<=10):
        if(CashtoAccountRate>=0.6):
            saleSystem.CommissionRate=0
            saleSystem.Commission=0
        else:
            saleSystem.CommissionRate=7
            saleSystem.calculatedCommision()
    else:
        if(CashtoAccountRate<=0.85):
            saleSystem.CommissionRate=5
            saleSystem.calculatedCommision()
        else:
            saleSystem.CommissionRate=6
            saleSystem.calculatedCommision()


    return str(saleSystem.Commission)


if __name__ == '__main__':
    compute()