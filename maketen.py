import itertools

#list_nums = [2, 2, 8, 9]
#list_nums = [4, 6, 6, 9]
#list_nums = [5, 6, 7, 9]
#list_nums = [5, 5, 5, 7]
list_nums = [1, 1, 5, 8] 
#list_nums = [1, 1, 9, 9]
list_syms = ['+', '-', '*', '/']
list_cals = ['((({}{}{}){}{}){}{})', '(({}{}{}){}({}{}{}))', '({}{}({}{}({}{}{})))']
list_answers = []

cnt_total, cnt_success = 0, 0
for perm_nums in itertools.permutations(list_nums, 4):
    num_0, num_1, num_2, num_3 = float(perm_nums[0]), float(perm_nums[1]), float(perm_nums[2]), float(perm_nums[3])
    for sym_0 in list_syms:
        for sym_1 in list_syms:
            for sym_2 in list_syms:
                for cal in list_cals:
                    cnt_total += 1
                    # print(num_0, num_1, num_2, num_3, sym_0, sym_1, sym_2, cal)
                    str_cal = cal.format(num_0, sym_0, num_1, sym_1, num_2, sym_2, num_3)
                    try:
                        ans_cal = eval(str_cal)
                    except:
                        print('({}) {} = zero division error'.format(cnt_total, str_cal))
                    else:
                        cnt_success += 1
                        print('({}) {} = {}'.format(cnt_total, str_cal, ans_cal))
                        if (abs(ans_cal - 10.0) < 1e-6) and (str_cal not in list_answers): list_answers.append(str_cal)

print('# of successfully-defined calculations: {} / {}'.format(cnt_success, cnt_total))
print('Answers:')
for answer in list_answers:
    print(answer)

