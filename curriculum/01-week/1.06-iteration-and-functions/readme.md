---
title: Iteration
duration: "1:30"
creator: DSI-DC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Iteration
Week 1 | Lesson 1.06

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Iterate using for loops
- Iterate using while loops
- Write a basic function

---

<a name="for and while loops"></a>
## Introduction: for and while loops (10 mins)
The for statement is used to iterate over the elements of a sequence. It's used when you have a piece of code which you want to repeat *n* number of times. You can use any iterable object (such as strings, arrays, lists, tuples, dict and so on) in a for loop in Python.

The while loop tells the computer to do something as long as a condition is met. A while loop consists of a block of code and a condition. The condition is evaluated, and if the condition is true, the code within the block is executed. This repeats until the condition becomes false.

Here is [a resource](http://www.pythonforbeginners.com/control-flow-2/python-for-and-while-loops) and here is [another one](http://www.cyberciti.biz/faq/python-for-loop-examples-statements/) on for and while loops.


<a name="for loops"></a>
## Demo: for loops

In Jupyter notebook type:
```bash
# basic for loop example
for count in [1, 2, 3]:
    print(count)
    print('Yes' * count)
```

This is a for loop. It has the heading starting with for, followed by a variable name (count in this case), the word in, some sequence, and a final colon. As with function definitions and other heading lines, the colon at the end of the line indicates that a consistently indented block of statements follows to complete the for loop.

Let's try a simple repeat for loop. When you just want to repeat the exact same thing a specific number of times. In that case only the length of the sequence, not the individual elements are important.

In Jupyter notebook type:
```bash
# simple repeat loop
for i in range(10):
    print('Hello')
```

Let's try a for loop through words. In Jupyter notebook type:
```bash
# using a for loop to go through the letters in a word
word = 'computer'
for letter in word:
    print letter
```

Let's try using a for loop to print out a list.
In Jupyter notebook type:
```bash
shuttles = ['columbia', 'endeavor', 'challenger', 'discovery', 'atlantis', 'enterprise', 'pathfinder' ]

for s in shuttles:
    print s
```

[Additional resource for loops.](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/loops.html)

Now, try creating a few for loops on your own.

**Check** What is the basic syntax for a for loop?


<a name="while loops"></a>
## Demo: while loops

Let's create a simple counter using a while loop.
In Jupyter notebook type:
```bash
# create a counter using a while loop
count = 0
while count < 5:
    print count
    count = count + 1  
```

Let's try another.
In Jupyter notebook type:
```bash
# another counter using a while loop
a = 0		
while a < 10:
   a = a + 1
   print a
```

And maybe one more...
In Jupyter notebook type:
```bash
while True:
    reply = raw_input('Enter text, [type "stop" to quit]: ')
    print reply.lower()
    if reply == 'stop':
        break
```

This while loop will stop when the user types "stop."

Remember, a while loop runs until the expression is False. The problem is, sometimes they don't stop. To avoid this, here are practical guidelines:
1. Make sure that you use while-loops sparingly. Usually a for-loop is better.
2. Review your while statements and make sure that the boolean test will become False at some point.
3. When in doubt, print out your test variable at the top and bottom of the while-loop to see what it's doing.

[while loops](http://learnpythonthehardway.org/book/ex33.html)

**Check** What is a common problem that might occur with while loops? What are ways to avoid this problem?

<a name="functions"></a>
## Introduction: What is a function?

A function is a piece of code that has an output based on what is input.

We sometimes call the inputs of a function the arguments.

The basic structure of a function is:
```bash
def function_name(input1,input2,...):
    do something with inputs
    return output
```

Let's create a function to add two numbers:

```bash
def addition(input1,input2):
    output = input1 + input2
    return output
```

**Check:** How might we make a function to add three numbers?

**Check:** When might functions be important?

<a name="conclusion"></a>
## Conclusion
- When is a for loop useful?
- When is a while loop useful?
- What are the differences between for and while loops?
- What is a problem that while loops run into?
- What are some things you can do so you don't run into this problem with while loops?
- What is a function?