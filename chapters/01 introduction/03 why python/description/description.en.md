Python has become a language of choice for teaching people how to
program. It is a powerful language, that is easy to use, and that offers
all the possibilities that any other computer language offers. It is
easily portable between different operating systems. It is freely
available. For beginning programmers, it has the advantage that it
enforces writing readable code. Python is also a language that is used
for many practical applications, either as a basis for complete
programs, or as an extension to programs written in a different
language.

The main advantage of using Python is that it allows you to focus on
"thinking like a programmer," rather than learning all the arcane
intricacies of a language. Here is an example of the difference between
using Python, and using some other popular programming languages: The
first program that anybody writes in any language, is *Hello World*.
This is a program that displays the text "Hello, world!" on the screen.
In the highly popular computer language C++, *Hello World* is coded as
follows:

```cpp
#include <iostream>
int main() {
    std::cout << "Hello, world!";
}
```

In C#, Microsoft’s popular variant of C++, it is:

```csharp
using System;
namespace HelloWorld {
    class Hello {
        static void Main() {
            Console.WriteLine( "Hello, world!" );
            Console.ReadKey();
        }
    }
}
```

In Objective-C, Apple's C++ variation, the code becomes even worse:

```objective_c
#import <Foundation/Foundation.h>
int main ( int argc, const char * argv[] ) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSLog (@"Hello, world!");
    [pool drain];
    return 0;
}
```

In Java, which is taught as the first language to many computer science
students, it is:

```java
class Hello {
    public static void main( String[] args ) {
        System.out.println( "Hello, world!" );
    }
}
```

Now compare this to writing *Hello World* in Python:

```python
print( "Hello, world!" )
```

I think we can agree that the Python version of this program is much
more readable and understandable – even without knowing the language –
than any of the other languages.
