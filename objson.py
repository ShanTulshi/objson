import json

'''
Returns a JSON string representation of all accessible,
non-callable fields of a Python object. Useful for
transferring state of a known object generically.
'''
def objson(obj, jsonify=True):
    retdict = {'__type__': type(obj)}
    for s in dir(obj):
        t = getattr(obj, s)
        if(s == '__doc__' or callable(t)):
            continue
        elif(type(t) in [str, int, float]):
            retdict[s] = t
        else:
            retdict[s] = objson(s, False)
    if(jsonify):
        return json.dumps(retdict)
    else:
        return retdict
