'''1. Importar o modulo Tkinter
   2. Criar a janela principal
   3. Adicione qualquer número de widgets à janela principal
   4. Aplique o gatilho do evento no widget'''


# Criar Calculadora simples em python com GUI simples usando Tkinter

# importar tudo do modulo tkinter
from tkinter import *

# declara a variavel global expression

expression = ""

# função para atualizar o texto de entrada
def press(num):
    global expression

    expression = expression + str(num) # concatenação da string

    equation.set(expression) # atualização  da expression usando o metodo set





# Funcao para avaliar o final da expression
def equalpress():
    try:
        global expression

        total = str(eval(expression))

        equation.set(total)

        expression = ""

    # se o erro for gerado, manipule
    # pelo bloco de exceção
    except:

        equation.set(" erro")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

if __name__ == '__main__':
    gui = Tk() # cria a janela GUI

    gui.configure(background = "light green") # define cor de fundo

    gui.title("Calculadora by PsykoInsane") # define o titulo da GUI

    gui.geometry("265x125") # Define a configuração da GUI

    equation = StringVar() # StringVar () é a classe variável  nós criamos uma instância desta classe

    expression_field = Entry(gui, textvariable=equation) # crie a caixa de entrada de texto para # mostrando a expressão

    expression_field.grid(columnspan=4, ipadx=70) # método de grade é usado para colocar # os widgets nas respectivas
                                                  # posições na tabela como estrutura

    equation.set('enter your expression')

#crie um botões e coloque em um determinado
# localização dentro da janela raiz.
# quando o usuário pressiona o botão, o comando ou
# função afiliada a esse botão é executada

    button1 = Button(gui, text='1', fg= 'white', bg= 'black', command=lambda : press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text='2', fg='white', bg='black', command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text='3', fg='white', bg='black', command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text='4', fg='white', bg='black', command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text='5', fg='white', bg='black', command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text='6', fg='white', bg='black', command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text='7', fg='white', bg='black', command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text='8', fg='white', bg='black', command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text='9', fg='white', bg='black', command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text='0', fg='white', bg='black', command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text='+', fg ='white', bg='black', command=lambda: press("+"), height=1,width=7)
    plus.grid(row=2, column=3)

    menos = Button(gui, text='-', fg='white', bg='black', command=lambda: press("-"), height=1, width=7)
    menos.grid(row=3, column=3)

    multiply = Button(gui, text='*', fg='white', bg='black', command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text='/', fg='white', bg='black', command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    igual = Button(gui, text='=', fg='white', bg='black', command=equalpress, height=1, width=7)
    igual.grid(row=5, column=2)

    clear = Button(gui, text='Limpar', fg='white', bg='black', command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    gui.mainloop() # inicia a GUI















