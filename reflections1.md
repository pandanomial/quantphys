Three things are interesting:

### 1. Python is a dynamic language and scripts can easily be executed from the command line. 

I also like that you can easily run the interpreter from the command line to test things. For example:

```
$ python

>>> name = "Steph"
>>> name
'Steph'
```

Also, I can use type(), dir(), and help(), for example:

```
>>> name = "Steph"
>>> type(name)
<class 'str'>
```

###  2. Python uses easy and simple syntax 
A comparison of Python with C++:

#### C++ code 
```
#include <iostream>
#include <string>
using namespace std;

int main() {
      string name;
      cin >> name;
      cout << "Good evening, " << name << endl;
      return 0;
}
```
#### Python code:
```
name = input()
print("Good evening, " + name)
```

### 3. Python NumPy is a great package for scientific computing.

Simple example showing Numpy array:

```
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))
```
