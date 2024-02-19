#Garbage Collection - 
'''
Memory allocation and deallocation is automatic

2 Strategies- 
Refrence counting : by tracking how many times an object is referenced.
                    object’s reference count reaches zero, 
                    it becomes un-referenceable and its memory can be freed up.

Garbage collection : automatically reclaim memory that is no
                    longer accessible or in use by the app.
'''

## Reference counting
import sys
x = [1,2,3]
ref_count = sys.getrefcount(x)
print("Initial Reference Count: ", ref_count)

y = x
ref_count_x = sys.getrefcount(x)
ref_count_y = sys.getrefcount(y)
print(ref_count_x,ref_count_y)
x = None
ref_count_x = sys.getrefcount(x)
ref_count_y = sys.getrefcount(y)

## Garbage collection
import gc
print(gc.get_threshold()) # default threshold - (700, 10, 10) 
                            #no.of allocation vs no. of deallocation is greater than 700 
                            #the automatic garbage collection will run

## Manual GC
gc_collect = gc.collect()
print(gc_collect)

## Forced GC
# gc.collect([generation])

## Disable and Enable GC
gc.disable()
gc.enable()

## othe functions
gc.collect()
gc.get_threshold()
gc.set_threshold(500,5,5)

