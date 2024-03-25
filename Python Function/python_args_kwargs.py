'''
*args - non keyword arguments
**kwargs - keyword arguments
'''

def fun(*argv):
    for arg in argv:
        print(arg)

fun('Hello', 'Welcome', [0,1,2,3], 'daily_data_prep')


def fun1(**kwargv):
    for k,v in kwargv.items():
        print(k,v)

fun1(a='daily_data_prep',b='enliven_arts',c='youtube',d='instagram')
