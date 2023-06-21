import datetime

def calendar_atom(arg_list):
    v_list_new = [str(x) for x in arg_list]
    year, month, day = arg_list[0], arg_list[1], arg_list[2]
    if (year < 2000 or year > 2100) and (month < 1 or month > 12) and (day < 1 or day > 31):
        return '不合法'
    if year < 2000 or year > 2100:
        return '年数超出了限制'
    if month < 1 or month > 12:
        return '月份超出了限制'
    if day < 1 or day > 31:
        return '天数超出了限制'
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day < 1 or day > 30:
                return "天数超出了限制"
        elif month == 2:
            if day < 1 or day > 29:
                return "天数超出了限制"
    else:
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day < 1 or day > 30:
                return "天数超出了限制"
        elif month == 2:
            if day < 1 or day > 28:
                return "天数超出了限制"
    try:
        _date = datetime.datetime.strptime('-'.join(v_list_new), '%Y-%m-%d').date()
    except Exception as e:
        return str(e)
    return str(_date + datetime.timedelta(days=1))


if __name__ == '__main__':
    print(calendar_atom([2020, 12, 31]))