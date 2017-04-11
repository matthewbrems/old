# ![logo](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Quiz One Review

## For loops

For loops iterate through a list of items until there are no longer any further items to iterate over.

```python
shuttles = ['columbia', 'endeavor', 'challenger', 'discovery', 'atlantis', 'enterprise', 'pathfinder' ]

for s in shuttles:
    print s
```

This will print out (each on a new line):

```
columbia
endeavor
challenger
discovery
atlantis
enterprise
pathfinder
```

## While loops

While loops repeat a set of operations until some condition is no longer met/True.

```python
a = 0		
while a < 10:
   a = a + 1
   print a
```

This will iterate nine times and print:

```
1
2
3
4
5
6
7
8
9
```

## Functions

A function is a piece of code that has an output based on what is input. You declare functions, and they are not run until they are called.

We sometimes call the inputs of a function the arguments.

The basic structure of a function is:

```ptyhon
def function_name(input1,input2,...):
    do something with inputs
    return output
```

Read more on iteration and functions [here](https://github.com/ga-students/DC-DSI4/tree/master/curriculum/01-week/1.06-iteration-and-functions)

## Misc

Study how `range()` operates. It is inclusive or exclusive on either side? Eg what numbers are in `range(1,6)`?

Study basic mathematical operations. Be sure you know what each of the following do: `+`, `-`, `*`, `/`, `**`

