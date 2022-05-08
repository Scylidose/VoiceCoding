# VoiceCoding

## Description

## Use Cases 

### First Use Case

```python

print("hello world")

```

### Second Use Case

```python

lorem = "hello"
ipsum = 8.9

```

### Third Use Case 

```python

count = 2
if count < 5:
    print("count is inferior to five")

```

### Fourth Use Case

```python

count = 2
if count < 5:
    print("count is inferior to five")
else:
    print("count is superior to five")

```

### Fifth Use Case

```python

count = 0
for i in range(0, 5):
    count += 1
print("the sum of numbers between 0 and 5 is ", count)    

```

### Sixth Use Case 

```python

count = 0
for i in range(0, 5):
    if count < 4:
        count += 1
print("the sum of numbers between 0 and 3 is ", count)    

```

## Virtual Environment 

### Create

```bash
python3 -m venv venv
```

### Activate

```bash
.\venv\Scripts\activate 
```

### Install requirements

```bash
pip install -r requirements.txt
```

## Unit Test 

To execute every test and ensure the proper functioning of the application, you can execute at the root of the project, the shell command : 

```bash
pytest
```