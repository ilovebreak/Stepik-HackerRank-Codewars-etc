''' Код geeksforgeeks'''


def flatten_dict1(dd, separator='_', prefix=''):
    return {prefix + separator + k if prefix else k: v
            for kk, vv in dd.items()
            for k, v in flatten_dict1(vv, separator, kk).items()
            } if isinstance(dd, dict) else {prefix: dd}


''' То же, развернуто'''


def flatten_dict2(dd, separator='_', prefix=''):
    new_d = {}
    if isinstance(dd, dict):
        for key1, value1 in dd.items():
            for key2, value2 in flatten_dict2(value1, separator, key1).items():
                if prefix:
                    new_d[prefix + separator + key2] = value2
                else:
                    new_d[key2] = value2
        return new_d
    else:
        return {prefix: dd}


nested = {'Germany': {'berlin': 7},
          'Europe': {'italy': {'Rome': 3}},
          'USA': {'washington': 1, 'New York': 4}}

not_nested = {'a': 100, 'b': 200}

nested1 = {'Q': {'w': {'E': {'r': {'T': {'y': 123}}}}}}

flatten_dict2(nested)