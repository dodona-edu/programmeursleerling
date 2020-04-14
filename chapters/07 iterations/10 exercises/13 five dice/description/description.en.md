You roll a number of six-sided dice, one by one. What is the probability that the outcome of each roll is a value that is greater then or equal to the value obtained with the previous roll?

Je gooit een aantal dobbelstenen één voor één na elkaar. Hoe groot is de kans dat de waarde van elke dobbelsteen groter of gelijk is dan de waarde van de vorige dobbelsteen?

For example, if we roll 5 dice, then

> 1, 1, 4, 4, 6
 
is a non-decreasing sequence of rolls, where

> 1, 1, 4, 3, 6

is not.

### Input

Een getal $$n \in \mathbb{N}_0$$.

### Output

A sentence giving the probability that rolling of $$n$$ dice in succession yields a non-decreasing sequence. Determine the probability by performing a large number of simulations.

### Example

#### Input:

```
5
```

#### Output:

```
P(non-decreasing sequence of 5 dice) = 0.032293
```
