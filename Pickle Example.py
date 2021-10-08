'''

As a data scientist, you will use sets of data in the form of dictionaries, DataFrames, or any other data type.
When working with those, you might want to save them to a file, so you can use them later on or send them to someone else.
This is what Python's pickle module is for: it serializes objects so they can be saved to a file, and loaded in a program again later on.

What is pickling?
Pickle is used for serializing and de-serializing Python object structures, also called marshalling or flattening.
Serialization refers to the process of converting an object in memory to a byte stream that can be stored on disk or sent over a network.
Later on, this character stream can then be retrieved and de-serialized back to a Python object.
Pickling is not to be confused with compression! The former is the conversion of an object from one representation (data in Random Access Memory (RAM)) to another (text on disk),
while the latter is the process of encoding data with fewer bits, in order to save disk space.

What Can You Do With pickle?
Pickling is useful for applications where you need some degree of persistency in your data.
Your program's state data can be saved to disk, so you can continue working on it later on.
It can also be used to send data over a Transmission Control Protocol (TCP) or socket connection, or to store python objects in a database.
Pickle is very useful for when you're working with machine learning algorithms, where you want to save them to be able to make new predictions at a later time, without having to rewrite everything or train the model all over again.

When Not To Use pickle
If you want to use data across different programming languages, pickle is not recommended.
Its protocol is specific to Python, thus, cross-language compatibility is not guaranteed. The same holds for different versions of Python itself.
Unpickling a file that was pickled in a different version of Python may not always work properly, so you have to make sure that you're using the same version and perform an update if necessary.
You should also try not to unpickle data from an untrusted source. Malicious code inside the file might be executed upon unpickling.

Storing data with pickle

What can be pickled?
You can pickle objects with the following data types:

Booleans,
Integers,
Floats,
Complex numbers,
(normal and Unicode) Strings,
Tuples,
Lists,
Sets, and
Dictionaries that ontain picklable objects.
All the above can be pickled, but you can also do the same for classes and functions, for example, if they are defined at the top level of a module.

Not everything can be pickled (easily), though: examples of this are generators, inner classes, lambda functions and defaultdicts. In the case of lambda functions, you need to use an additional package named dill. With defaultdicts, you need to create them with a module-level function.


Pickle vs JSON
JSON stands for JavaScript Object Notation. It's a lightweight format for data-interchange, that is easily readable by humans.
Although it was derived from JavaScript, JSON is standardized and language-independent. This is a serious advantage over pickle.
It's also more secure and much faster than pickle.

However, if you only need to use Python, then the pickle module is still a good choice for its ease of use and ability to reconstruct complete Python objects.

An alternative is cPickle. It is nearly identical to pickle, but written in C, which makes it up to 1000 times faster.
For small files, however, you won't notice the difference in speed. Both produce the same data streams, which means that Pickle and cPickle can use the same files.

Pickle and multiprocessing
When very complex computations have to be executed, it is common to distribute this task over several processes.
Multiprocessing means that several processes are executed simultaneously, usually over several Central Processing Units (CPUs) or CPU cores, thus saving time.
An example is the training of machine learning models or neural networks, which are intensive and time-consuming processes.
By distributing these on a large amount of processing units, a lot of time can be saved. In Python, this is done using the multiprocessing package.

When a task is divided over several processes, these might need to share data. Processes do not share memory space,
so when they have to send information to each other, they use serialization, which is done using the pickle module.

Remember that lambda functions can't be pickled. So if you try to apply multiprocessing to a lambda function, it will fail.
There is a solution for this. dill is a package similar to pickle that can serialize lambda functions, among other things. I
ts use it almost identical to pickle.
'''

#Pickling a file
import pickle
import bz2 #module for bzip2 compression
import multiprocessing as mp
from math import cos
from builtins import type
from io import open

friend_name = { 'Rita': 1, 'Girwar': 2, 'Pragya': 3, 'Priyanshi': 4, 'Vijaya': 5, 'Piuesh': 6, 'Rashika': 7 }

filename = 'friends'
o_file = open(filename, 'wb')
pickle.dump(friend_name,o_file)
o_file.close()


#unpickle the file
i_file = open(filename,'rb')
new__friends_dict = pickle.load(i_file)
i_file.close()

print(new__friends_dict)
print(new__friends_dict==friend_name)
print(type(new__friends_dict))


#compressing pickle file
compressed_file = bz2.BZ2File('compressed_file', 'w')
pickle.dump(friend_name, compressed_file)



