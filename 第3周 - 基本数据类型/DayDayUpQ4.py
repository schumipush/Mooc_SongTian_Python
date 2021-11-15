#DayDayUpQ4.py
def dayUP(df):
    dayup=1
    for i in range(365): #带有计数的循环
        if i%7 in [6,0]:
            dayup = dayup*(1-0.01)
        else:
            dayup = dayup*(1+df)
    return dayup
dayfactor = 0.01
while dayUP(dayfactor)<37.78: #带有条件的循环
    dayfactor+=0.001
print("工作日的努力参数是：{:.3f}".format(dayfactor))
