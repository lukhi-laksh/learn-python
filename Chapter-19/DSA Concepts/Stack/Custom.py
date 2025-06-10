class Stack:
    def __init__(self, s):
        self.size = s
        self.top = -1
        self.arr = [0] * s
# This function push one value
    def push(self, value):
        if self.top < self.size - 1:
            self.top += 1
            self.arr[self.top] = value
            print(f"Pushed {value} to stack.")
        else:
            print("Stack Overflow")

    def display(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print("Stack elements:")
            for i in range(self.top, -1, -1):
                print(self.arr[i])

# Create Stack object
st = Stack(5)

# Push some values
st.push(10)
st.push(20)
st.push(30)

# Display current stack
st.display()
