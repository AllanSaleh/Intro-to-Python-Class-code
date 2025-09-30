# In-Class Assignments - Lesson 1: Introduction to Python

## Assignment 1: Basic Output Practice (15 minutes)

### Instructions
Create a file called `assignment1_output.py` and complete the following tasks:

1. **Print Statements**
   - Print your name
   - Print your favorite programming language
   - Print a fun fact about yourself

2. **String Variables**
   - Create variables for your name, age, and hometown
   - Print them using f-strings
   - Print them using string concatenation

3. **Number Operations**
   - Create two number variables
   - Perform all four basic operations (+, -, *, /)
   - Print the results with clear labels

### Example Output
```
My name is John
My favorite programming language is Python
I love playing guitar!

Name: John, Age: 25, Hometown: New York
Name: John, Age: 25, Hometown: New York

First number: 10, Second number: 3
Addition: 13
Subtraction: 7
Multiplication: 30
Division: 3.3333333333333335
```

## Assignment 2: Interactive Program (20 minutes)

### Instructions
Create a file called `assignment2_interactive.py` and build an interactive program that:

1. **Gets User Information**
   - Ask for the user's name
   - Ask for their favorite number
   - Ask for their birth year

2. **Performs Calculations**
   - Calculate their current age
   - Calculate what year they'll turn 100
   - Calculate the square of their favorite number

3. **Displays Results**
   - Show all the information in a formatted way
   - Include some fun facts or predictions

### Example Output
```
What's your name? Alice
What's your favorite number? 7
What year were you born? 1995

=== Alice's Profile ===
Age: 29 years old
You'll turn 100 in the year 2095!
Your favorite number squared is 49!

Fun fact: You've been alive for about 10,585 days!
```

## Assignment 3: Mini Calculator (25 minutes)

### Instructions
Create a file called `assignment3_calculator.py` and build a calculator that:

1. **Menu System**
   - Display a menu with 5 operations (add, subtract, multiply, divide, power)
   - Ask user to choose an operation

2. **Input Validation**
   - Get two numbers from the user
   - Handle division by zero
   - Handle invalid menu choices

3. **Enhanced Features**
   - Add a "quit" option
   - Allow the program to run multiple calculations
   - Show the calculation history

### Example Output
```
=== Mini Calculator ===
1. Add
2. Subtract
3. Multiply
4. Divide
5. Power
6. Quit

Choose operation (1-6): 1
Enter first number: 15
Enter second number: 7
Result: 15 + 7 = 22

Choose operation (1-6): 4
Enter first number: 20
Enter second number: 0
Error: Cannot divide by zero!

Choose operation (1-6): 6
Goodbye!
```

## Assignment 4: Creative Challenge (20 minutes)

### Instructions
Create a file called `assignment4_creative.py` and build something creative using what you've learned:

**Option A: Story Generator**
- Ask for character name, setting, and action
- Generate a short story using the inputs
- Include some random elements

**Option B: Personal Quiz**
- Create 5 questions about the user
- Calculate a "personality score" based on answers
- Give them a fun result

**Option C: Unit Converter**
- Convert between different units (miles/km, pounds/kg, etc.)
- Include multiple conversion options
- Add some interesting facts about the conversions

### Example (Story Generator)
```
Character name: Bob
Setting: Space station
Action: Dancing

=== Bob's Space Adventure ===
Bob was floating in the space station when suddenly...
they started dancing! The zero gravity made the dance moves
look absolutely incredible. All the other astronauts joined in,
and it became the first intergalactic dance party!

The end.
```

## Assignment 5: Debugging Challenge (15 minutes)

### Instructions
Create a file called `assignment5_debug.py` and fix the following broken code:

```python
# This code has several errors - fix them!
name = input("What's your name? ")
age = input("How old are you? ")
height = input("How tall are you in feet? ")

# Calculate some facts
birth_year = 2024 - age
height_inches = height * 12
name_length = len(name)

print("Name: " + name)
print("Age: " + age)
print("Birth year: " + birth_year)
print("Height in inches: " + height_inches)
print("Your name has " + name_length + " letters!")
```

### Tasks
1. Identify all the errors in the code
2. Fix the type conversion issues
3. Fix the string concatenation problems
4. Test the program with different inputs
5. Add error handling for invalid inputs

## Assignment Guidelines

### Time Management
- **Assignment 1**: 15 minutes (basic practice)
- **Assignment 2**: 20 minutes (interactive program)
- **Assignment 3**: 25 minutes (calculator with validation)
- **Assignment 4**: 20 minutes (creative project)
- **Assignment 5**: 15 minutes (debugging)

### Instructor Tips
1. **Circulate the room** to help students who get stuck
2. **Encourage collaboration** - students can help each other
3. **Provide hints** rather than complete solutions
4. **Celebrate creative solutions** - there's often more than one way to solve problems
5. **Use the whiteboard** to explain concepts when multiple students have the same question

### Common Issues to Watch For
- **Type conversion errors**: Students forgetting to convert input to numbers
- **String concatenation**: Mixing strings and numbers without conversion
- **Indentation**: Python's strict indentation rules
- **Variable scope**: Understanding where variables are accessible
- **Input validation**: Not handling invalid user input

### Assessment Criteria
- **Functionality**: Does the program work as intended?
- **Code quality**: Is the code readable and well-structured?
- **Error handling**: Does it handle invalid inputs gracefully?
- **Creativity**: Did they add interesting features beyond requirements?
- **Understanding**: Can they explain how their code works?

### Extension Activities
For students who finish early:
1. Add more features to their programs
2. Create additional programs using the same concepts
3. Help other students who are struggling
4. Research additional Python functions and try them out
5. Start working on the homework assignment 