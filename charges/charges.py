class ChargeSystem:
    basic_charge = 25
    fee_per_min = 0.15
    fee = 0

    def __init__(self, phone_time, missed_payments):
        self.phone_time = phone_time
        self.missed_payments = missed_payments

    def condition(self):
        if self.phone_time < 0:
            return False
        if self.missed_payments < 0:
            return False
        if self.phone_time > 20000:
            return False
        if self.missed_payments > 20:
            return False
        return True

    def conditionstr(self):
        if self.phone_time < 0:
            return "通话分钟数不能小于0"
        if self.missed_payments < 0:
            return "不按时缴费次数不能小于0"
        if self.phone_time > 20000:
            return "通话分钟数超出了限制"
        if self.missed_payments > 20:
            return "不按时缴费次数超出了限制"

    def calculatedFee(self):
        if 0 <= self.phone_time <= 60 and self.missed_payments <= 1:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time * (1 - 0.01)
        elif 60 < self.phone_time <= 120 and self.missed_payments <= 2:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time * (1 - 0.015)
        elif 120 < self.phone_time <= 180 and self.missed_payments <= 3:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time * (1 - 0.02)
        elif 180 < self.phone_time <= 300 and self.missed_payments <= 3:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time * (1 - 0.025)
        elif 300 < self.phone_time and self.missed_payments <= 6:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time * (1 - 0.03)
        else:
            self.fee = self.basic_charge + self.fee_per_min * self.phone_time
        return round(self.fee, 7)

    def calculatedCount(self):
        if 0 <= self.phone_time <= 60:
            return 1
        elif 60 < self.phone_time <= 120:
            return 2
        elif 120 < self.phone_time <= 300:
            return 3
        elif self.phone_time > 300:
            return 6


def compute(phone_time, missed_payments):
    chargeSystem = ChargeSystem(phone_time, missed_payments)  # 实例化收费系统

    if chargeSystem.condition():
        return chargeSystem.calculatedFee()
    else:
        return chargeSystem.conditionstr()

def count(phone_time, missed_payments):
    chargeSystem = ChargeSystem(phone_time, missed_payments)  # 实例化收费系统
    if chargeSystem.condition():
        return chargeSystem.calculatedCount()
    else:
        return 0

if __name__ == '__main__':
    compute()
    count()