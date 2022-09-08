import tkinter as tk

print('hello')

reader = ''
def readDisplay(new):
    global reader
    reader = reader + new
    return reader

ready = False
plus = False
minus = False
multiplication = False
division = False
modulo = False
intDivision = False
exponent = False

def equalsFunction():
    global number1
    global number2
    global reader
    global plus
    global minus
    global multiplication
    global division
    global modulo
    global intDivision
    global exponent
    global ready
    if ready:
        number2 = reader
        if plus:
            solution = float(number1) + float(number2)
            plus = False
        elif minus:
            solution = float(number1) - float(number2)
            minus = False
        elif multiplication:
            solution = float(number1) * float(number2)
            multiplication = False
        elif division:
            solution = float(number1) / float(number2)
            division = False
        elif modulo:
            solution = float(number1) % int(number2)
            modulo = False
        elif intDivision:
            solution = float(number1) // float(number2)
            intDivision = False
        elif exponent:
            solution = float(number1) ** float(number2)
            exponent = False
        if solution == int(solution):
            solution = int(solution)
        reader = str(solution)
        display.set_text(reader)
        ready = False

def eraseFunction():
    print('hello')
    global ready
    global number1
    global number2
    global reader
    ready = False
    number1 = False
    number2 = False
    reader = ''
    display.set_text('')

def plusFunction():
    global reader
    global number1
    global ready
    global plus
    if not ready:
        number1 = reader
        ready = True
        plus = True
        display.add_text('+')
        reader = ''

def minusFunction():
    global reader
    global number1
    global ready
    global minus
    if not ready:
        number1 = reader
        ready = True
        minus = True
        display.add_text('-')
        reader = ''

def multiplicationFunction():
    global reader
    global number1
    global ready
    global multiplication
    if not ready:
        number1 = reader
        ready = True
        multiplication = True
        display.add_text('*')
        reader = ''

def divisionFunction():
    global reader
    global number1
    global ready
    global division
    if not ready:
        number1 = reader
        ready = True
        division = True
        display.add_text('/')
        reader = ''

def moduloFunction():
    global reader
    global number1
    global ready
    global modulo
    if not ready:
        number1 = reader
        ready = True
        modulo = True
        display.add_text('%')
        reader = ''

def intDivisionFunction():
    global reader
    global number1
    global ready
    global intDivision
    if not ready:
        number1 = reader
        ready = True
        intDivision = True
        display.add_text('//')
        reader = ''

def exponentFunction():
    global reader
    global number1
    global ready
    global exponent
    if not ready:
        number1 = reader
        ready = True
        exponent = True
        display.add_text('^')
        reader = ''

class Cell():
    def __init__(self):
        self.cell = None
        self.operations = {
"=": lambda: equalsFunction(),
"+": lambda: plusFunction(),
"-": lambda: minusFunction(),
"/": lambda: divisionFunction(),
"*": lambda: multiplicationFunction(),
"%": lambda: moduloFunction(),
"C": lambda: eraseFunction(),
"//": lambda: intDivisionFunction(),
"^": lambda: exponentFunction()
}
        
        
    def create_number_btn(self, loc, num, widthX, heightY, posx, posy):
        self.cell = tk.Button(
            loc, 
            text = str(num), 
            width = widthX, 
            height = heightY,
            command = lambda: display.add_text(num)
            )
        self.cell.place(x = posx, y = posy)
    
    def create_operation_btn(self, loc, operation, widthX, heightY, posx, posy):
        self.cell = tk.Button(
            loc,
            command = self.operations[operation],
            text = operation,
            width = widthX,
            height = heightY
            )
        self.cell.place(x = posx, y = posy)
    
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
        addText = readDisplay(str(newText))
        self.cell.config(text = addText)
        

root = tk.Tk()

root.configure(bg = 'black')
root.geometry('360x480')
root.title('Calculator')
root.resizable(False, False)

display_frame = tk.Frame(
    root,
    bg = '#e0e0e0',
    width = 360,
    height = 80
    )

display_frame.place(x=0,y=0)

operation_frame_1 = tk.Frame(
    root,
    bg = '#e0e0e0',
    width = 90,
    height = 400
    )

operation_frame_1.place(x=270, y=80)

numbers_frame = tk.Frame(
    root,
    bg = '#e0e0e0',
    width = 270,
    height = 320
    )

numbers_frame.place(x=0, y=160)

operation_frame_2 = tk.Frame(
    root,
    bg = '#e0e0e0',
    width = 270,
    height = 80
    )

operation_frame_2.place(x = 0, y = 80)


number_btn_list = []
operations_btn_list = []

i=0

for x in range(3):
    for y in range(3):
        i=i+1
        number_btn_list.append(Cell())
        number_btn_list[x + y].create_number_btn(numbers_frame, i, 10, 3, 9 + 84 * y, 10 + 75 * x)

number_btn_list.append(Cell())
number_btn_list[9].create_number_btn(numbers_frame, 0, 10, 3, 9, 235)

operation_list = ['+', '-', '/', '*', '%', 'C', '//', '^']

for i in range(5):
    operations_btn_list.append(Cell())
    operations_btn_list[i].create_operation_btn(operation_frame_1, operation_list[i], 10, 3, 0, 14 + 75 * i)
    
operations_btn_list.append(Cell())
operations_btn_list[5].create_operation_btn(numbers_frame, '=', 22, 3, 93, 235)

for i in range(5,8):
    operations_btn_list.append(Cell())
    operations_btn_list[i].create_operation_btn(operation_frame_2, operation_list[i], 10, 3, 9 + 84 * (i-5), 14)

display = Cell()
display.create_display(display_frame, 46, 12, 40)

root.mainloop()
