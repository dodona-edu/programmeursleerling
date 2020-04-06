Python wordt door velen gezien als een taal die bij uitstek geschikt is
om mensen te leren programmeren. Het is een krachtige taal, die
gemakkelijk te gebruiken is, en die alle mogelijkheden biedt die andere
talen ook bieden. Je kunt Python programma's draaien op verschillende
machines en verschillende besturingssystemen. Het is gratis
verkrijgbaar. Voor beginnende programmeurs heeft het het voordeel dat
het dwingt om nette code te schrijven. Python wordt ook in de praktijk
veel gebruikt, soms als basis voor complete programma's, soms als
uitbreiding op programma's die in een andere taal geschreven zijn.

Het belangrijkste voordeel is dat Python het mogelijk maakt om je te
concentreren op "denken als een programmeur," in plaats van op alle
excentrieke afwijkingen die een specifieke taal heeft. Hier volgt een
voorbeeld van het verschil tussen Python en een aantal andere populaire
programmeertalen: Het eerste programma dat iedereen schrijft in een
computertaal is *Hello World*. Dit is een programma dat de tekst "Hello,
world!" op het scherm zet. In de zeer populaire taal C++, wordt *Hello
World* als volgt gecodeerd:

```cpp
#include <iostream>
int main() {
    std::cout << "Hello, world!";
}
```

In C#, de populaire variant can C++ die uitgebracht is door Microsoft,
is het:

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

In Objective-C, Apple's variant op C++, is het nog erger:

```objective_cpp
#import <Foundation/Foundation.h>
int main ( int argc, const char * argv[] ) {
    NSAutoreleasePool *pool = [[NSAutoreleasePool alloc] init];
    NSLog (@"Hello, world!");
    [pool drain];
    return 0;
}
```

In Java, dat voor veel studenten aan universiteiten en hogescholen de
eerst-geleerde taal is, wordt het:

```java
class Hello {
    public static void main( String[] args ) {
        System.out.println( "Hello, world!" );
    }
}
```

En zie nu wat *Hello World* in Python is:

```python
print( "Hello, world!" )
```

Ik neem aan dat we het met elkaar eens zijn dat de Python versie van dit
programma leesbaarder en begrijpelijker is dan de andere varianten –
zelfs als je de taal niet kent.
