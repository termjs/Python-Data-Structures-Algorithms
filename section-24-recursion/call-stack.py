# Call Stack

# Define a function that prints "Three"
def funcThree():
    print("Three")

# Define a function that calls funcThree and then prints "Two"
def funcTwo():
    funcThree()
    print("Two")

# Define a function that calls funcTwo and then prints "One"
def funcOne():
    funcTwo()
    print("One")

# Start the call chain by calling funcOne
funcOne()
