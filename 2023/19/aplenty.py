import sys


def parserule(r):
    name, rule = r[:-1].split('{')
    R = []
    for r in rule.split(':'):
        R.extend(r.split(','))
    return name, R


def parsepart(p):
    elems = p[1:-1].split(',')
    part = {}
    for e in elems:
        var, val = e.split('=')
        part[var] = int(val)
    return part


def match_part(part, rules):
    cur = rules['in']
    i = 0
    while True:
        if cur[i] == 'R':
            return False
        elif cur[i] == 'A':
            return True
        elif '<' in cur[i]:
            var, val = cur[i].split('<')
            if part[var] < int(val):
                i += 1
            else:
                i += 2
        elif '>' in cur[i]:
            var, val = cur[i].split('>')
            if part[var] > int(val):
                i += 1
            else:
                i += 2
        else:
            cur = rules[cur[i]]
            i = 0


if __name__ == '__main__':
    data = sys.stdin.read().strip()
    rules, parts = data.split('\n\n')
    rules = dict(map(parserule, rules.split('\n')))
    parts = list(map(parsepart, parts.split('\n')))
    accepted = [part for part in parts if match_part(part, rules)]
    print("Part 1:", sum([sum(part.values()) for part in accepted]))
