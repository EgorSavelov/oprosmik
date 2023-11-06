from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QGroupBox,QApplication, QWidget, QPushButton, QLabel,QMessageBox, QVBoxLayout, QRadioButton, QHBoxLayout, QButtonGroup
from random import shuffle
from random import randint

class Question():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_l = []
q1 = Question('Какой человек перестал ходить на занятия по алгоритмике?','Р.Ферин','Р.Арсений','Н.Лера','С.Егор')
q2 = Question('Какого цвета нету во флаге России?','чёрный','белый','красный','синий')    
q3 = Question('С какого года отменили платные звонки по России?','2006','2004','2008','2007')
q4 = Question('В каком году отменили крепостное право?','1861','1860','1868','1867')
q5 = Question('В каком году была Куликовская битва?','1380','1381','1390','1360')
q6 = Question('Когда день официанта?','21 мая','21 июня','22 апреля','12 апреля')
q7 = Question('Кто самый харизматичный человек?','>>С.Егор<<','Р.Арсений','Н.Лера','Д.Иван')
q8 = Question('У кого самая лучшая улыбка?','Д.Иван','С.Егор','Р.Арсений','Ф.Руслан')
q9= Question('Кто прёт на таран?','Н.Лера','Р.Арсений','С.Егор','Д.Иван')
q10 = Question('Кто самый умный в мире человек?','Н.Лера','Р.Арсений','С.Егор','Д.Иван')

question_l.append(q1)
question_l.append(q2)
question_l.append(q3)
question_l.append(q4)
question_l.append(q5)
question_l.append(q6)
question_l.append(q7)
question_l.append(q8)
question_l.append(q9)
question_l.append(q10)

app=QApplication([])
win=QWidget()
win.setWindowTitle('Самый сложый вопрос в мие!')

btn_ok = QPushButton('Ответить')
lb_Question = QLabel('Какой человек перестал ходить на занятия по алгоритмике?')

RadioGroupBox = QGroupBox('Варианты ответов')

bt_1=QRadioButton('Ф.Руслан')
bt_2=QRadioButton('Р.Арсений')
bt_3=QRadioButton('Н.Лера')
bt_4=QRadioButton('С.Егор')

RadioGroup = QButtonGroup()
RadioGroup.addButton(bt_1)
RadioGroup.addButton(bt_2)
RadioGroup.addButton(bt_3)
RadioGroup.addButton(bt_4)

layout_bt1= QHBoxLayout()
layout_bt2 = QVBoxLayout()
layout_bt3 = QVBoxLayout()

layout_bt2.addWidget(bt_1)
layout_bt2.addWidget(bt_2)
layout_bt3.addWidget(bt_3)
layout_bt3.addWidget(bt_4)

layout_bt1.addLayout(layout_bt2)
layout_bt1.addLayout(layout_bt3)

RadioGroupBox.setLayout(layout_bt1)

AnsGroupBox = QGroupBox('Результат теста')
layout_r = QLabel('Правильно ли ты ответил?')
layout_c = QLabel('Ответ будет тут)')

layout_result = QVBoxLayout()
layout_result.addWidget(layout_r, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_result.addWidget(layout_c, alignment =Qt.AlignHCenter, stretch=4)
AnsGroupBox.setLayout(layout_result)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch = 3)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1,stretch=2)
layout_card.addLayout(layout_line2,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3,stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий ответ')

def show_q():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    bt_1.setChecked(False)
    bt_2.setChecked(False)
    bt_3.setChecked(False)
    bt_4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [bt_1,bt_2,bt_3,bt_4]

def start_test():
    if 'Ответить' == btn_ok.text():
        show_result()
    else:
        show_q()

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    layout_c.setText(q.right_answer)
    show_q()

def show_correct(res):
    layout_r.setText(res)
    show_result()

def check():
    if answers[0].isChecked():
        show_correct('Правильно!')
        win.score += 1
        print('Статистика\n-Всего вопросов: ', win.total,'\n-Правильно овтетов: ', win.score)
        print('Рейтинг: ', (win.score/win.total * 100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно')
            print('Рейтинг: ', (win.score/win.total * 100),'%')
def next_q():
    win.total += 1
    q = question_l[randint(0,len(question_l)-1)]
    ask(q)
    print('Статистика\n-Всего вопросов: ', win.total,'\n-Правильно овтетов: ', win.score)

def click_ok():
    if btn_ok.text() == 'Ответить':
        check()
    else:
        next_q()

win=QWidget()
win.setLayout(layout_card)
win.setWindowTitle('Memory Card')
btn_ok.clicked.connect(click_ok)
win.total = 0
win.score = 0
next_q()
win.show()
app.exec_()