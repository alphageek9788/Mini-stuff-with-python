def frequency_counter(strg):
    dict = {}
    for n in strg:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(frequency_counter('google.com'))
