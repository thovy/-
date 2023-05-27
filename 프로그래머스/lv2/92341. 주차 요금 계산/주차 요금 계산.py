import math


def cal_fee(total_time, fees):
    print(fees)
    first_cut, first_cut_fee, after_minute, after_minute_fee = map(int, fees)
    if total_time <= first_cut:
        return first_cut_fee
    else:
        return first_cut_fee + (math.ceil((total_time-first_cut)/after_minute)) * after_minute_fee


def cal_time(in_time, out_time):
    hour = int(out_time[:2]) - int(in_time[:2])
    minute = int(out_time[3:]) - int(in_time[3:])
    if minute < 0:
        minute = (60 - int(in_time[3:])) + int(out_time[3:])
        hour -= 1
    hour_to_min = hour * 60
    total_min = hour_to_min + minute
    return total_min


def solution(fees, records):

    answer = []

    time_stack = []
    num_stack = []
    total_time_by_num = {}
    print(records)
    for r in records:
        time, num, io = map(str, r.split())
        if io == 'IN':
            time_stack.append(time)
            num_stack.append(num)
        else:
            idx = num_stack.index(num)
            num_stack.pop(idx)
            in_time = time_stack.pop(idx)
            total_time = cal_time(in_time, time)
            if num in total_time_by_num.keys():
                total_time_by_num[num] += total_time
            else:
                total_time_by_num[num] = total_time

    while num_stack:
        num = num_stack.pop()
        time = time_stack.pop()
        total_time = cal_time(time, "23:59")
        if num in total_time_by_num.keys():
            total_time_by_num[num] += total_time
        else:
            total_time_by_num[num] = total_time

    print(total_time_by_num)
    total_fee = {}
    for num, time in total_time_by_num.items():
        total_fee[num] = cal_fee(time, fees)

    for k, v in sorted(total_fee.items()):
        answer.append(v)
    return answer