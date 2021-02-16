from tkinter import Tk, Frame, Label, Button 
from time import sleep#Функция sleep () приостанавливает выполнение текущего потока на заданное количество секунд


class Question:
    def __init__(self, question, answers, correctLetter):
        self.question = question#Вопросы
        self.answers = answers#Ответы
        self.correctLetter = correctLetter#Правильная буква

    def check(self, letter, view):
        global right#Перемещает окно в правую сторону
        if(letter == self.correctLetter):
            label = Label(view, text="Right!")#Label - это виджет, предназначенный для отображения какой-либо надписи без возможности редактирования пользователем.
            right += 1
            #Label имеет те же свойства, что и перечисленные свойства кнопки.
        else:
            label = Label(view, text="Wrong!")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))#Lambda — это инструмент в python для вызова анонимных функций
    

  
 
    def getView(self, window):
        view = Frame(window,bg="aqua")
        Label(view,bg="lightblue", text=self.question).pack()
        Button(view,bg="lightblue", text=self.answers[0], command=lambda *args: self.check("A", view)).pack()
        Button(view,bg="lightblue", text=self.answers[1], command=lambda *args: self.check("B", view)).pack()
        Button(view,bg="lightblue", text=self.answers[2], command=lambda *args: self.check("C", view)).pack()
        Button(view,bg="lightblue", text=self.answers[3], command=lambda *args: self.check("D", view)).pack()
        return view

    def unpackView(self, view):#self — это стандартное имя первого аргумента для методов объекта.
        #view, или представление, — это то место, где мы разместим «логику» работы нашего приложения
        view.pack_forget()#Если мы хотим отменить отображение любого виджета с экрана или верхнего уровня, то используется метод Forgot ()
        askQuestion()
def close_window(): 
    window.destroy()#destroy () просто завершает mainloop и удаляет все виджеты.

def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()#getView() метод в адаптере предназначен для создания представления элемента Listbox

def quit():
 window.quit()
questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line#Строка вопроса
    answers = []
    for i in range (4):
        answers.append(file.readline())#Append вставляет содержимое, заданное параметром, в конец каждого элемента в наборе соответствующих элементов

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()#Считывает из файла одну строку и возвращает её.
file.close()
index = -1
right = 0
number_of_questions = len(questions)#Функция LEN возвращает количество символов в текстовой строке, включая пробелы.

window = Tk()
window.geometry("600x400")
window.configure(background="purple")
button = Button(window,bg="orange",fg="brown",height=3,width=9, text="Start", command=askQuestion)
button_two= Button(window,bg="green",fg="blue",height=3,width=9, text = "Quit", command = quit)
button_three = Button(height=3,width=12, text = "Screen resolution", bg = "pink",fg="blue",command=lambda:window.geometry("900x700"))
button_four = Button(height=3,width=9,text = "Color", bg = "lightblue",fg="purple",command=lambda:window.config(bg="orange"))
button.pack()
button_five = Button(height=3,width=9,fg="orange",bg="coral",text="Click", command=lambda:buttonCallback)
button.pack()
button_two.pack()
button_three.pack()
button_four.pack()
window.mainloop()
