import sys
from aplenty import parserule
from copy import deepcopy

MIN = 1
MAX = 4000


def get_subrange(prange, pred):
    true_range = deepcopy(prange)
    false_range = deepcopy(prange)
    if '<' in pred:
        var, val = pred.split('<')
        (l, r) = prange[var]
        if int(val) <= l:
            return None, prange
        elif int(val) > r:
            return prange, None
        else:
            true_range[var] = (l, int(val) - 1)
            false_range[var] = (int(val), r)
    else:
        var, val = pred.split('>')
        (l, r) = prange[var]
        if int(val) >= r:
            return None, prange
        elif int(val) < l:
            return prange, None
        else:
            true_range[var] = (int(val) + 1, r)
            false_range[var] = (l, int(val))
    return true_range, false_range


def match(prange, rule):
    to_expand = []
    accepted = []
    stack = [(0, prange)]
    while stack:
        i, cur_prange = stack.pop()
        if rule[i] == 'R':
            continue
        elif rule[i] == 'A':
            accepted.append(cur_prange)
        elif '<' in rule[i] or '>' in rule[i]:
            true_range, false_range = get_subrange(cur_prange, rule[i])
            if true_range:
                stack.append((i + 1, true_range))
            if false_range:
                stack.append((i + 2, false_range))
        else:
            to_expand.append((rule[i], cur_prange))
    return to_expand, accepted


def combinations(prange):
    combs = 1
    for var in 'xmas':
        l, r = prange[var]
        assert l <= r
        combs *= r - l + 1
    return combs


if __name__ == '__main__':
    data = sys.stdin.read().strip()
    rules, parts = data.split('\n\n')
    rules = dict(map(parserule, rules.split('\n')))

    stack = [("in", {c: (1, 4000) for c in "xmas"})]
    all_accepted = []
    while stack:
        rule_name, prange = stack.pop()
        to_expand, accepted = match(prange, rules[rule_name])
        stack.extend(to_expand)
        all_accepted.extend(accepted)

    print("Part 2:", sum([combinations(a) for a in all_accepted]))
