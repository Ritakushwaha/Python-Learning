# Coroutine - generalization of subroutines, many entry points
# Subroutine - called by main function, single entry point
#Thread - OS(run env) decided the switch between threads according to scheduler.


# Coroutine:

def print_name(prefix):
    print(prefix)
    try: 
        while True:
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print('Closing')

corou = print_name('Dear')
corou.__next__()
corou.send('Rita')
corou.send('Miss Rita')
corou.send('Dear Rita')
corou.close()