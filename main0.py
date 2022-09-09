import tkinter as tk

reader = ''
ready = False

def equalsFunction():
    global number1
    global number2
    global reader
    global ready
    global operation
    if ready:
        number2 = reader
        operationFunctions = {
            '+': float(number1) + float(number2),
            '-': float(number1) - float(number2),
            '*': float(number1) * float(number2),
            '/': float(number1) / float(number2),
            '%': float(number1) % float(number2),
            '^': float(number1) ** float(number2)
            }
        solution = operationFunctions[operation]
        if solution == int(solution):
            solution = int(solution)
        reader = str(solution)
        display.set_text(reader)
        ready = False

def eraseFunction():
    global ready
    global number1
    global number2
    global reader
    global operation
    ready = False
    number1 = None
    number2 = None
    reader = ''
    display.set_text('')

def pmFunction():
    global number1

def operations(op):
    global reader
    global number1
    global ready
    global operation
    if op == '=':
        equalsFunction()
    elif op == 'C':
        eraseFunction()
    elif op == '+/-':
        number1 = (-1) * float(reader)
        if number1 == int(number1):
            number1 = int(number1)
        number1 = str(number1)
        display.set_text(number1)
        reader = number1
    elif not ready:
        number1 = reader
        ready = True
        operation = op
        display.add_text(op)
        reader = ''

class Cell():
    def __init__(self):
        self.cell = None

class NumberCell(Cell):
    def __init__(self):
        super().__init__()

    def create_number_btn(self, loc, num, widthX, heightY, posx, posy):
        self.cell = tk.Button(
            loc, 
            text = str(num), 
            width = widthX, 
            height = heightY,
            command = lambda: display.add_text(num)
            )
        self.cell.place(x = posx, y = posy)
        
class OperationCell(Cell):
    def __init__(self):
        super().__init__()
        
    def create_operation_btn(self, loc, operation, widthX, heightY, posx, posy):
        self.cell = tk.Button(
            loc,
            command = lambda: operations(operation),
            text = operation,
            width = widthX,
            height = heightY
            )
        self.cell.place(x = posx, y = posy)
        
class DisplayCell(Cell):
    def __init__(self):
        super().__init__()
        
    def create_display(self, loc, widthX, posx, posy):
        self.cell = tk.Label(
            loc,
            text = '',
            justify = 'center',
            width = widthX,
            state = 'disabled'
            )
        self.cell.place(x=posx,y=posy)
    
    def set_text(self, newText):
        self.cell.config(text = newText)
        
    def add_text(self, newText):
        global reader
        reader = reader + str(newText)
        self.cell.config(text = reader)

root = tk.Tk()

root.configure(bg = 'black')
root.geometry('360x480')
root.title('Calculator')
root.resizable(False, False)

display_frame = tk.Frame(
    root,
    bg = '#e0e0e0',
    width = 360,
    height = 80)

display_frame.place(x=0,y=0)

operation_frame_1 = tk.Frame(
    root,
    bg = '#e0e0e0',
    width = 90,
    height = 400)

operation_frame_1.place(x=270, y=80)

numbers_frame = tk.Frame(
    root,
    bg = '#e0e0e0',
    width = 270,
    height = 320)

numbers_frame.place(x=0, y=160)

operation_frame_2 = tk.Frame(
    root,
    bg = '#e0e0e0',
    width = 270,
    height = 80)

operation_frame_2.place(x = 0, y = 80)

number_btn_list = []
operations_btn_list = []

i=0
for y in range(3):
    for x in range(3):
        i=i+1
        number_btn_list.append(NumberCell())
        number_btn_list[x + y].create_number_btn(numbers_frame, i, 10, 3, 9 + 84 * x, 10 + 75 * y)

number_btn_list.append(NumberCell())
number_btn_list[9].create_number_btn(numbers_frame, 0, 10, 3, 9, 235)

number_btn_list.append(NumberCell())
number_btn_list[10].create_number_btn(numbers_frame, '.', 10, 3, 93, 235)

operation_list = ['+', '-', '/', '*', '%', 'C', '+/-', '^']

for i in range(5):
    operations_btn_list.append(OperationCell())
    operations_btn_list[i].create_operation_btn(operation_frame_1, operation_list[i], 10, 3, 0, 14 + 75 * i)
    
operations_btn_list.append(OperationCell())
operations_btn_list[5].create_operation_btn(numbers_frame, '=', 10, 3, 93+84, 235)

for i in range(5,8):
    operations_btn_list.append(OperationCell())
    operations_btn_list[i].create_operation_btn(operation_frame_2, operation_list[i], 10, 3, 9 + 84 * (i-5), 14)

display = DisplayCell()
display.create_display(display_frame, 46, 12, 40)

root.mainloop()
