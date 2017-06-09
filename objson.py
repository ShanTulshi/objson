import json

'''
Returns a JSON string representation of all accessible,
non-callable fields of a Python object. Useful for
transferring state of a known object generically.
NOTE: Objects passed in *must* have a default (no-args)
      constructor.
'''
def objson(obj, jsonify=True):
    retdict = {'__meta__': {'__name__' : type(obj).__name__, '__module__' : type(obj).__module__}}
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

def jsonobj(json):
    try:
        c = getattr(json['__meta__']['__module__'], json['__meta__']['__name__'])()
    except (KeyError, NameError, TypeError) as err:
        t = type(err)
        if(t is KeyError):
            raise ValueError('objson: Malformed json!')
        elif(t is NameError):
            # TODO: try importing class myself.
            raise NameError('objson: Required class is not imported!')
        elif(t is TypeError):
            raise TypeError('objson: Class does not have a valid no-args constructor!')
        else:
            raise err
    # TODO. In the meantime, just use pickle.
