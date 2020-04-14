The sieve of Eratosthenes is a method to
find all prime numbers between 1 and a given number using a list. This
works as follows: Fill the list with the sequence of numbers from 1 to
the highest number. Set the value of 1 to zero, as 1 is not prime. Now
loop over the list. Find the next number on the list that is not zero,
which, at the start, is the number 2. Now set all multiples of this
number to zero. Then find the next number on the list that is not zero,
which is 3. Set all multiples of this number to zero. Then the next
number, which is 5 (because 4 has already been set to zero), and do the
same thing again. Process all the numbers of the list in this way. When
you have finished, the only numbers left on the list are primes. Use
this method to determine all the primes between 1 and 100.
