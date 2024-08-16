from PyQt6.QtWidgets import *

from calcFace import *

import math
class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def pressIt(self, pressed):
        '''
        This is the function that takes whatever the user presses and displays it to the screen

        :param pressed: Whatever the user pressed
        :return: what the user pressed to the display screen
        '''
        if pressed == 'C':
            self.label.setText('0')
        else:
            #Check to see if start with 0 & delete 0
            if self.label.text() == '0':
                self.label.setText('')
            #Concat previous pressed button
            self.label.setText(f'{self.label.text()}{pressed}')

    def dotIt(self):
        '''
        This function makes a decimal on the current number in display

        :return: a decimal onto a number
        '''
        screen = self.label.text()
        charList = ['*', '/', '-', '+'] #check for symbols in label
        isValid = True
        for i in screen: #Goes through current string in label
            if i in charList:
                isValid = True
            elif i == '.':
                isValid = False
        if isValid:
            self.label.setText(f'{screen}.')

    def delIt(self):
        '''
        This function deletes the most recent number/symbol on the display

        :return:
        '''
        screen = self.label.text() 
        screen = screen[:-1]
        self.label.setText(screen)

    def negPosIt(self):
        '''
        This functions switches the number from positive to negative and vise versa.

        :return:
        '''
        screen = self.label.text()
        if '-' in screen:
            self.label.setText(screen.replace('-', ''))
        else:
            self.label.setText((f'-{screen}'))

    def equalIt(self):
        '''
        This function analyzes the screen and calculates the math equation

        :return:
        '''
        screen = self.label.text()
        try:
            ans = eval(screen) #eval() reads entire screen and calculates
            self.label.setText(str(ans))
        except:
            self.label.setText('ERROR')

    def area(self):
        '''
        This function detects which radio area button is checked and displays the correct values needed

        :return:
        '''
        if self.buttonCircle.isChecked():
            self.entryOne.setText('')
            self.entryTwo.setText('')
            self.entryOne.show()
            self.entryTwo.hide()
            self.entryOne.setPlaceholderText("Radius")

        elif self.buttonSquare.isChecked():
            self.entryOne.setText('')
            self.entryTwo.setText('')
            self.entryOne.show()
            self.entryTwo.hide()
            self.entryOne.setPlaceholderText("Side Length")

        elif self.buttonRectangle.isChecked():
            self.entryOne.setText('')
            self.entryTwo.setText('')
            self.entryOne.show()
            self.entryTwo.show()
            self.entryOne.setPlaceholderText("Length")
            self.entryTwo.setPlaceholderText("Width")

        elif self.buttonTriangle.isChecked():
            self.entryOne.setText('')
            self.entryTwo.setText('')
            self.entryOne.show()
            self.entryTwo.show()
            self.entryOne.setPlaceholderText("Base")
            self.entryTwo.setPlaceholderText("Height")

        else:
            self.entryOne.setText('')
            self.entryTwo.setText('')
            self.label.setText('ERROR')

    def computeIt(self):
        '''
        This function computes the area of previous selected shape

        :return:
        '''
        try:
            one = self.entryOne.text()
            two = self.entryTwo.text()
            #Circle
            if self.buttonCircle.isChecked():
                radius = float(one)
                if radius <= 0:
                    raise TypeError
                else:
                    result = math.pi * math.pow(radius, 2)
                    self.label.setText(f'{result:.4f}')
                    self.entryOne.setText('')
                    self.entryTwo.setText('')
            #Square
            elif self.buttonSquare.isChecked():
                side = float(one)
                if side <= 0:
                    raise TypeError
                else:
                    result = math.pow(side, 2)
                    self.label.setText(f'{result:.2f}')
                    self.entryOne.setText('')
                    self.entryTwo.setText('')
            #Rectangle
            elif self.buttonRectangle.isChecked():
                length = float(one)
                width = float(two)
                if length <= 0 or width <= 0:
                    raise TypeError
                else:
                    result = length * width
                    self.label.setText(f'{result:.2f}')
                    self.entryOne.setText('')
                    self.entryTwo.setText('')
            #Triangle
            elif self.buttonTriangle.isChecked():
                base = float(one)
                heigth = float(two)
                if base <= 0 or heigth <= 0:
                    raise TypeError
                else:
                    result = 0.5 * (base * heigth)
                    self.label.setText(f'{result:.2f}')
                    self.entryOne.setText('')
                    self.entryTwo.setText('')
        except TypeError:
            self.label.setText('ERROR')
        except ValueError:
            self.label.setText('ERROR')


