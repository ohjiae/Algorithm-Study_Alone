import itertools
from collections import Counter

def solution(orders, course):
    answer = []
    for n in course:
        orders_comb = []
        for order in orders:
            orders_comb += itertools.combinations(sorted(order),n)
        most = Counter(orders_comb).most_common()
        answer += [k for k,v in most if v>1 and v == most[0][1]]
    
    return [''.join(x) for x in sorted(answer)]

''' 1ㅂㅓㄴㅉㅐ ㄷㅏㅂ
import itertools

def org_alphabet(x):
    temp = sorted(list(set(x)))
    orgd = ''.join(temp)
    return orgd

def solution(orders, course):
    answer = []
    new = {}
    for n in course:
        for o in orders:
            if len(o) >= n: 
                o = org_alphabet(o)
                comb = itertools.combinations(o,n)
                for c in comb:
                    if c in new: # if c is already in dict
                        new[c] += 1 # add count number
                    else: 
                        new[c] = 1
    for i in course: # 가장 많이 함께 주문된 메뉴일 때만
        popular = {}
        for menu in new:
            if (len(menu) == i) and (new[menu]>=2):
                popular[menu] = new[menu]
        for pop in popular:
            if popular[pop] == max(popular.values()):
                answer.append(''.join(pop))
    answer.sort()
    return answer
'''
