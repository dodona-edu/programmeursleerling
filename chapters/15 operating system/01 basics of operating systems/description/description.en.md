A computer consists of hardware, while programs consist of software. The
software uses facilities offered by the hardware. While in the early
days of computer programming, programmers accessed hardware directly
(for instance, to make a pixel visible on a computer screen, a
programmer placed a value in a specific memory address that was directly
coupled to the screen – an approach called "poking"), nowadays hardware
is so complex and diverse that this is no longer a viable approach. Let
alone the fact that if you want to write a program that runs on multiple
computers, you cannot afford to access hardware directly as hardware
differs from computer to computer.

Therefore, programs access hardware functionalities through an
"operating system." An operating system can be seen as a layer between
programs and hardware, that offers programs high-level functions to get
the hardware to work. Typical operating systems in use nowadays on
personal computers are Microsoft's "Windows," Apple's "Mac OS," and the
open-source OS "Linux" (though there are many more). Each of these
exists in multiple variants, often differentiated by numbers or
"builds," and sometimes (in the case of Linux) by a company name.
Regardless, they all offer functionalities that allow accessing
hardware.

The problem is that while all of them offer such functionalities, the
functionalities are not named in consistent ways, and have different
parameterizations. This means that if you want to write Python programs
that access hardware by directly "talking" to the operating system, your
program is not portable to other operating systems. This is where the
`os` module comes in. The `os` module offers functions that you can use
to access the hardware with, regardless of the operating system.
Basically, the `os` module has a different implementation for each
operating system, but your program does not need to know that, as the
functions are always named the same, and have the same parameters.

That does not mean that you can be completely oblivious of OS
intricacies. For instance, when you access a file, on Windows you might
need to include a "drive letter," which Mac OS does not support. Another
example is that security and file access are much more flexible on Linux
than on either Windows or Mac OS, so accessing files on Linux might
generate different kinds of warnings and errors than on other operating
systems. There are quite a few functions that only have an effect for
particular operating systems. Still, the `os` module is a fine
compromise between portability and OS-dependent effectiveness.
