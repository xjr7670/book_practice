# -*- coding:utf-8 -*-


def main():
    sale_price = float(input('please input your sale price: '))
    down_payment = sale_price * 0.1
    annual_interest = 0.12
    month = 0
    total_rest = sale_price - down_payment

    print('%10s%10s%10s%10s%10s%10s' % ('第几个月', '当前欠款总额', '该月所欠利息',
                                        '该月所欠本金', '该月还款额', '还款后所欠总金额'))

    while True:
        month += 1
        interest = total_rest * annual_interest / 12
        principal = total_rest * 0.05 - interest
        payable = total_rest * 0.05
        old_rest = total_rest
        total_rest -= payable

        print('%-10d%20.5f%20.5f%20.5f%20.5f%20.5f' % (month, old_rest, interest,
                                                      principal, payable, total_rest))
        if round(total_rest, 2) <= 0:
            break

if __name__ == "__main__":
    main()

