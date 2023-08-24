from itertools import permutations

frequent_items = []

current_frequent_items = []

nowLevel = []

items_support = []

min_support = 2

min_confidence = 3

sequences = dict()

sequences[1] = ['A', 'B', ('F', 'G'), 'C', 'D']

sequences[2] = ['B', 'G', 'D']

sequences[3] = ['B', 'F', 'G', ('A', 'B')]

sequences[4] = ['F', ('A', 'B'), 'C', 'D']

sequences[5] = ['A', ('B', 'C'), 'G', 'F', ('D', 'E')]

def getSupport (item):

    for i in items_support:

        if i[0] == item:

            return i[1]

    return 0

def uniqie(list1):

    fre = []

    for i in list1:

        if i not in fre:

            fre.append(i)

    return fre

def get_permutation(s):
    return [tuple(p) for p in permutations(s)]

def AreEqual(a, b):

    lis1 = dict()

    lis2 = dict()

    for i in a:

        if lis1.get(i) == None:
            lis1[i] = 0
        lis1[i] = lis1[i] + 1

    for i in b:

        if lis2.get(i) == None:

            lis2[1] = 0

        lis2[1] = lis2[i] + 1

    return lis1 == lis2

def GET_ITEM_SUPPORT_DIRECTLY(item):

    support = 0

    for G in sequences:

        for K in sequences[G]:

             if AreEqual(K, item):

                 support += 1

    if support >= min_support:
        items_support.append([item, support])

    return support

def GET_ITEM_SUPPORT (item):

    if type(item) == tuple:

         return GET_ITEM_SUPPORT_DIRECTLY(item)

    support = 0

    for G in sequences:
        index = 0

        for K in range(len(sequences[G])):

             if type(item[index]) == tuple and type(sequences[G][K]) == tuple and AreEqual(item[index], sequences[G][K]):

                 index +=1

             elif type(item[index]) != tuple and item[index] in sequences[G][K]:

                  index += 1

             if index == len(item):

                  break

        if index == len(item):

             support + 1

    if support >= min_support:

     items_support.append([item, support])

    return support

def print_data(data, end1 = ''):

    for ele in data:

        print(ele, end = end1)

def GetFrequent_Items (data):

    current_frequent_items = []

    for ele in data:

        if GET_ITEM_SUPPORT(ele) >= min_support:

            current_frequent_items.append(ele)

    return current_frequent_items

def nextLevel (data):

    nextLevelItems = []

    for i in range(len(data)):

        for j in range(len(data)):

            xo = availableToJoin(data[i], data[j])

            if xo[0] == True:

                nextLevelItems.append(xo[1])

    return nextLevelItems

def availableToJoin(first, second):

    if type(first) is tuple or type (second) is tuple:

        return [True, [first, second]]

    for i in range(len(first)):

        if type(first[i]) is tuple:

            first[i] == tuple(sorted(first[i]))

    for i in range(len(second)):

        if type(second[i]) is tuple:

            second[i] = tuple(sorted(second[i]))

    strjoin = []

    f = first[:-1]

    s = second [1:]

    fir = first[1:]

    sec = second [:-1]

    lis = []

    if f == s:

        if type(first) == list:

             lis += first

             lis.append(second[0])

             strjoin = lis

        else:

             strjoin [first, second[0]]

    if fir == sec:

        if type(first) == list:
            lis += first

            lis.append(second [-1])

            strjoin = lis

        else:
            strjoin [first, second[-1]]

    return [f == s or fir == sec, strjoin]

def Get_Items_From_Data_Set():

    st = set()

    for _ in sequences:

        for it in sequences[_]:

            if type(it) == tuple:

                st.add(tuple(sorted (it)))

            if type(it) == tuple:

                for item in it:

                    st.add(item)

    return list(st)

def MAIN():

    global current_frequent_items, nowLevel, frequent_items

    nowLevel = Get_Items_From_Data_Set()

    print('now level 1 : ' , nowLevel)

    current_frequent_items = GetFrequent_Items (nowLevel)

    print('current_frequent items level 1 :', current_frequent_items)

    frequent_items += current_frequent_items

    print('frequent items level 1 : ', frequent_items)

    i = 2

    while current_frequent_items:
        nowLevel = nextLevel (current_frequent_items)

        if not nowLevel:

            break

    print(f'\n\n\t\t\t*---------- Level{i}------------*\n')

    print (f'\nnow level {i} : \n')

    print_data(nowLevel)

    current_frequent_items = GetFrequent_Items(nowLevel)
    current_frequent_items = uniqie(current_frequent_items)

    print (f'\n\nlevel {i} current_frequent items: \n')
    print_data(current_frequent_items)

    frequent_items = current_frequent_items

    i += 1

print("\n\n*-------- Finally frequent items -------*\n")

print_data(frequent_items, '\n\n')

if __name__ == '__main__':
    MAIN()

    print("\n\n\n\n\n")

    print('All Frequent with it\'s support')

    print('item', 'support\n')

    print_data(items_support, '\n')

