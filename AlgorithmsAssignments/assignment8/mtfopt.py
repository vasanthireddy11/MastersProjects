import matplotlib.pyplot as plt
from copy import deepcopy as copy
from random import randint


def MTFC(in_cache, requests):

    L = copy(in_cache)
    cost = 0
    for r in requests:
        i = 0
        while i < len(L):
            if r == L[i]:
                cost += i + 1
                L = [L[i]] + L[:i] + L[i + 1:]
                break
            i += 1
    return cost


def LRUC(in_cache, requests):
    capacity = copy(in_cache)
    c1 = len(capacity)

    cost = 0
    f = []
    s = copy(requests)
    st = []
    for i in s:
        if i not in f:
            if len(f) < c1:
                f.append(i)
                st.append(len(f) - 1)
            else:
                ind = st.pop(0)
                f[ind] = i
                st.append(ind)
            cost += 1
        else:
            st.append(st.pop(st.index(f.index(i))))
    return cost


OPT_graph = dict()
MTF_graph = dict()
max_cache = 6
sample_size = 160
for k in range(2, max_cache + 1):
    sample_length = 2 * k
    in_cache = [i for i in range(k)]
    print(in_cache)
    requests = [[randint(0, k+1 ) for j in range(sample_length)] for i in range(sample_size)]
    print(requests)
    OPT_graph[k] = round(sum([LRUC(in_cache, request) for request in requests]) / (sample_length * sample_size),3)
    MTF_graph[k] = round(sum([MTFC(in_cache, request) for request in requests]) / (sample_length * sample_size),3)

fig = plt.figure()
ax = fig.add_subplot(111)
X = [i for i in range(2, max_cache + 1)]
ax.plot(X, [MTF_graph[x] for x in X], 'go', label='MTF')
ax.plot(X, [OPT_graph[x] for x in X], 'bo', label='OPT')
ax.set_ylim((0, ax.get_ylim()[1] + 1))
ax.set_xticks(X)
ax.set_xlabel('Cache size')
ax.set_ylabel('Average cost per request')
fig.suptitle('MTF vs OPT')
ax.legend()
plt.show()

