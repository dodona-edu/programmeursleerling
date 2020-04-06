This book is not only meant to teach you to use Python, but, more
importantly, to teach you how to think like a programmer, because
thinking like a programmer is a necessity to understand what you can use
computers for and how you should use them. But what does "thinking like
a programmer" entail? I will answer this question by illustrating it
with performing a specific task:

Suppose that you have a deck of cards, each card with a different number
on it. You have to sort these cards from low to high, lowest card on
top. Most people are able to do that. Also, most people, when you ask
them how they do it, will look at you mystified, and answer: "Well,... I
just sort them low to high... what do you mean with how do I do it?"
Other people may say: "I first seek the highest card, and put it down.
Then I seek the next highest card, and put it on top of the highest
card. Etcetera." While this more or less explains how they sort cards,
if you then ask them: "But how do you seek the highest card?," most of
them, again, will look at you mystified.

The problem is that if you need to explain to a computer how to sort a
deck of cards, you cannot assume that the computer can infer anything
from vague statements, even if such statements would be completely clear
to a human. You cannot tell the computer: "Seek the highest card,"
because even if the computer would understand English, it would ask you
how it should seek the highest card. You will have to be very explicit
about it. You have to say something like "Take the top card from the
deck and hold it in you left hand. Then do the following until the deck
runs out: take the top card from the deck in your right hand. If the
value of the card in your right hand is higher than the value of the
card in your left hand, put the left-hand card in the discard pile and
put the right-hand card in your left hand. Otherwise, put the right-hand
card in the discard pile. Once the deck has run out and your right hand
is empty, the card in your left hand is the highest card."

Of course, a computer has no notion of left hand and right hand, and
does not understand English. But a computer does understand computer
language. Every computer language has a very precise syntax, and very
precise semantics, which means that a computer program is an unambiguous
explanation of how to perform a task. To have a computer perform a task,
you have to use a computer language, bound by its syntax, to explain
step-by-step how the task should be performed. Then, and only then, a
computer can perform the task.

Since it is often very hard to think of all the steps needed to perform
a task, you will have to divide the task into smaller subtasks, which
you may have to divide again into even smaller subtasks, until the
subtasks are so small that you can envision the steps needed to perform
those subtasks. Then you can create implementations for each of the
subtasks, and put them together to form a program for the task as a
whole.

Thinking like a programmer means that you are able to approach a task
from the perspective of programming a computer to perform that task,
that you are able to recognize what a logical division into subtasks is,
and that you can recognize when subtasks are sufficiently small so that
you can implement them. This is a skill that most people can learn, but
that requires a lot of practice and a thought process that is different
from what most people are used to.

Using this book, by learning to create programs in Python, starting with
small programs that gradually increase in complexity, you should also
learn to use the thought processes that come naturally to a programmer.
