"""
窝趣
户型：
A:35㎡ B:48㎡ C:45㎡ D:66㎡ E:66㎡ F:65㎡
租金标准
根据面积大小去定租金，用户不支付任何租金？押一付三
签合同同时就打租金，每季度付一次
违约：5年起签，5年内付违约，2年内反悔3万元，3年2万，4，5年1万
66平 1600一个月
装修风格去现场选
"""

house_type_A = 35
house_type_B = 48
house_type_C = 45
house_type_D = 66
house_type_E = 66
house_type_F = 65
rent_value_A = house_type_A * 40 # 每月收益
rent_value_B = house_type_B * 40
rent_value_C = house_type_C * 38
rent_value_D = house_type_D * 35
rent_value_E = house_type_E * 35
rent_value_F = house_type_F * 35
renovation_cost_A = house_type_A * 700
renovation_cost_B = house_type_B * 600
renovation_cost_C = house_type_C * 600
renovation_cost_D = house_type_D * 500
renovation_cost_E = house_type_E * 500
renovation_cost_F = house_type_F * 500


# 自定义装修费用
def self_renovation_cost():
    house_type = input(f'请输入你的房型大小：')
    cost_per_meter = input('请输入你自己的装修单价：')
    self_cost_total = int(house_type) * int(cost_per_meter)
    print(f'你自己装修需要花费{self_cost_total}元左右.')


# self_renovation_cost()

# 定义分隔符函数
def print_line():
    print('-' * 30)

# 根据房型估算自己装修费用
def estimate_self_renovation_cost(a, b=350):
    # a = input('请输入你的房型：(A,B,C,D,E,F):')
    if str(a) == 'A':
        print(f'假设外面每平米装修350元，你自己装修需要花费{house_type_A * b}元左右。')
    elif str(a) == 'B':
        print(f'假设外面每平米装修350元，你自己装修需要花费{house_type_B * b}元左右。')
    elif str(a) == 'C':
        print(f'假设外面每平米装修350元，你自己装修需要花费{house_type_C * b}元左右。')
    elif str(a) == 'D':
        print(f'假设外面每平米装修350元，你自己装修需要花费{house_type_D * b}元左右。')
    elif str(a) == 'E':
        print(f'假设外面每平米装修350元，你自己装修需要花费{house_type_E * b}元左右。')
    elif str(a) == 'F':
        print(f'假设外面每平米装修350元，你自己装修需要花费{house_type_F * b}元左右。')
    else:
        print(f'请输入正确的房型。')
    # return estimate_self_renovation_cost(a)


# estimate_self_renovation_cost('null')

# estimate_self_cost = estimate_self_renovation_cost()

# 定义自己出租收益
def self_income(money,month='12'):
    # self_money_per_month = input('请输入你的月租金')
    self_total_money = int(self_money_per_month) * int(month)
    print(f'你自己出租的话每年收入为：{self_total_money}元，5年收益为{self_total_money * 5}元。（这是理想情况，加上空置时间，折旧费用，大概算收益的85%，'
          f'约为：{self_total_money * 5 * 0.85}元。）')

# 参与窝趣
# 窝趣装修自己支付费用
def woqu_renovation_cost(a):
    if a == str('A'):
        print(f'你的户型为{a}户型，前期参与窝趣还需支付{renovation_cost_A}元。')
    elif a == str('B'):
        print(f'你的户型为{a}户型，前期参与窝趣还需支付{renovation_cost_B}元。')
    elif a == str('C'):
        print(f'你的户型为{a}户型，前期参与窝趣还需支付{renovation_cost_C}元。')
    elif a == str('D'):
        print(f'你的户型为{a}户型，前期参与窝趣还需支付{renovation_cost_D}元。')
    elif a == str('E'):
        print(f'你的户型为{a}户型，前期参与窝趣还需支付{renovation_cost_E}元。')
    elif a == str('F'):
        print(f'你的户型为{a}户型，前期参与窝趣还需支付{renovation_cost_F}元。')
    else:
        print(f'请正确输入你的户型')

def woqu_income(house_type,collaborate_year):
    if 0 < int(collaborate_year) <= 2:
        if house_type == str('A'):
            print(f'你的户型为{house_type},两年内，如果双方都不毁约，你的收入为：{rent_value_A * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_A * 12 * collaborate_year - 30000}元，如果窝趣毁约，你的收入为{rent_value_A * 12 * collaborate_year + 30000}元。')
        elif house_type == str('B'):
            print(f'你的户型为{house_type},两年内，如果双方都不毁约，你的收入为：{rent_value_B * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_B * 12 * collaborate_year - 30000}元，如果窝趣毁约，你的收入为{rent_value_B * 12 * collaborate_year + 30000}元。')
        elif house_type == str('C'):
            print(f'你的户型为{house_type},两年内，如果双方都不毁约，你的收入为：{rent_value_C * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_C * 12 * collaborate_year - 30000}元，如果窝趣毁约，你的收入为{rent_value_C * 12 * collaborate_year + 30000}元。')
        elif house_type == str('D'):
            print(f'你的户型为{house_type},两年内，如果双方都不毁约，你的收入为：{rent_value_D * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_D * 12 * collaborate_year - 30000}元，如果窝趣毁约，你的收入为{rent_value_D * 12 * collaborate_year + 30000}元。')
        elif house_type == str('E'):
            print(f'你的户型为{house_type},两年内，如果双方都不毁约，你的收入为：{rent_value_E * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_E * 12 * collaborate_year - 30000}元，如果窝趣毁约，你的收入为{rent_value_E * 12 * collaborate_year + 30000}元。')
        elif house_type == str('F'):
            print(f'你的户型为{house_type},两年内，如果双方都不毁约，你的收入为：{rent_value_F * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_F * 12 * collaborate_year - 30000}元，如果窝趣毁约，你的收入为{rent_value_F * 12 * collaborate_year + 30000}元。')
        else:
            print(f'请输入正确的户型。')
    elif 2 < int(collaborate_year) <= 3:
        if house_type == str('A'):
            print(f'你的户型为{house_type},两到三年内，如果双方都不毁约，你的收入为：{rent_value_A * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_A * 12 * collaborate_year - 20000}元，如果窝趣毁约，你的收入为{rent_value_A * 12 * collaborate_year + 20000}元。')
        elif house_type == str('B'):
            print(f'你的户型为{house_type},两到三年内，如果双方都不毁约，你的收入为：{rent_value_B * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_B * 12 * collaborate_year - 20000}元，如果窝趣毁约，你的收入为{rent_value_B * 12 * collaborate_year + 20000}元。')
        elif house_type == str('C'):
            print(f'你的户型为{house_type},两到三年内，如果双方都不毁约，你的收入为：{rent_value_C * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_C * 12 * collaborate_year - 20000}元，如果窝趣毁约，你的收入为{rent_value_C * 12 * collaborate_year + 20000}元。')
        elif house_type == str('D'):
            print(f'你的户型为{house_type},两到三年内，如果双方都不毁约，你的收入为：{rent_value_D * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_D * 12 * collaborate_year - 20000}元，如果窝趣毁约，你的收入为{rent_value_D * 12 * collaborate_year + 20000}元。')
        elif house_type == str('E'):
            print(f'你的户型为{house_type},两到三年内，如果双方都不毁约，你的收入为：{rent_value_E * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_E * 12 * collaborate_year - 20000}元，如果窝趣毁约，你的收入为{rent_value_E * 12 * collaborate_year + 20000}元。')
        elif house_type == str('F'):
            print(f'你的户型为{house_type},两到三年内，如果双方都不毁约，你的收入为：{rent_value_F * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_F * 12 * collaborate_year - 20000}元，如果窝趣毁约，你的收入为{rent_value_F * 12 * collaborate_year + 20000}元。')
        else:
            print(f'请输入正确的户型。')

    elif 3 < int(collaborate_year) <= 5:
        if house_type == str('A'):
            print(f'你的户型为{house_type},三到五年期间，如果双方都不毁约，你的收入为：{rent_value_A * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_A * 12 * collaborate_year - 10000}元，如果窝趣毁约，你的收入为{rent_value_A * 12 * collaborate_year + 10000}元。')
        elif house_type == str('B'):
            print(f'你的户型为{house_type},三到五年期间，如果双方都不毁约，你的收入为：{rent_value_B * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_A * 12 * collaborate_year - 10000}元，如果窝趣毁约，你的收入为{rent_value_B * 12 * collaborate_year + 10000}元。')
        elif house_type == str('C'):
            print(f'你的户型为{house_type},三到五年期间，如果双方都不毁约，你的收入为：{rent_value_C * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_A * 12 * collaborate_year - 10000}元，如果窝趣毁约，你的收入为{rent_value_C * 12 * collaborate_year + 10000}元。')
        elif house_type == str('D'):
            print(f'你的户型为{house_type},三到五年期间，如果双方都不毁约，你的收入为：{rent_value_D * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_A * 12 * collaborate_year - 10000}元，如果窝趣毁约，你的收入为{rent_value_D * 12 * collaborate_year + 10000}元。')
        elif house_type == str('E'):
            print(f'你的户型为{house_type},三到五年期间，如果双方都不毁约，你的收入为：{rent_value_E * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_A * 12 * collaborate_year - 10000}元，如果窝趣毁约，你的收入为{rent_value_E * 12 * collaborate_year + 10000}元。')
        elif house_type == str('F'):
            print(f'你的户型为{house_type},三到五年期间，如果双方都不毁约，你的收入为：{rent_value_F * 12 * collaborate_year}元，'
                  f'如果你毁约，你的收入为{rent_value_A * 12 * collaborate_year - 10000}元，如果窝趣毁约，你的收入为{rent_value_F * 12 * collaborate_year + 10000}元。')
        else:
            print(f'请输入正确的户型。')
    else:
        print('目前最多先算五年，更多年份确认后再算。')




# main
print_line()
print('自选方案')
your_house_type = input('请输入你的房型(A,B,C,D,E,F)：')
your_choice = input('如果你自己装修，请选择你自己装修方案：1，自己根据具体情况计算。2：系统估算：')
if int(your_choice) == 1:
    self_renovation_cost()
elif int(your_choice) == 2:
    estimate_self_renovation_cost(your_house_type)
else:
    print('请输入1或者2！！！')

self_money_per_month = input('现在计算你的收入，请输入你的月租金：')
self_income(self_money_per_month)
# print('-' * 20)
print_line()
print('窝趣方案：')
woqu_renovation_cost(your_house_type)
collo_year = input('请输入你跟窝趣的合约年数：')
woqu_income(your_house_type,collo_year)