from PyQt5 import QtCore, QtGui, QtWidgets
import ast
import sqlite3

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(652, 663)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listView = QtWidgets.QListWidget(Form)
        self.listView.setObjectName("listView")
        self.horizontalLayout_3.addWidget(self.listView)
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.listView_2 = QtWidgets.QListWidget(Form)
        self.listView_2.setObjectName("listView_2")
        self.horizontalLayout_3.addWidget(self.listView_2)
        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout.addWidget(self.lineEdit_8)
        self.gridLayout.addLayout(self.horizontalLayout, 5, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 6, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 9, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setEnabled(True)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContentsOnFirstShow)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem5 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 8, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_1.clicked.connect(self.evaluate)
        conn=sqlite3.connect('Fantasy_cricket2.db')                                    #connection to sqlite3
        sql="select team_name from Teams_stats"                                            #sql command
        teams=[]
        cur=conn.execute(sql)
        for row in cur:
            self.comboBox.addItem(row[0])                                       #adding items in combobox1
        self.comboBox.activated[str].connect(self.onChanged)                    #when combobox1 item is clicked
        self.comboBox_2.addItem("match_stats")                                      #adding value to combobox2
        self.comboBox_2.addItem("match_stats_2")                                      #adding value to combobox2
        self.comboBox_2.addItem("match_stats_3")                                      #adding value to combobox2

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Evaluation of performance"))
        self.label.setText(_translate("Form", "Players"))
        self.label_2.setText(_translate("Form", "Points"))
        self.pushButton_1.setText(_translate("Form", "Calculate Score"))

    def onChanged(self,text):                                                   #function when combobox1 item is clicked
        conn = sqlite3.connect('Fantasy_cricket2.db')
        team1 = self.comboBox.currentText()
        self.listView.clear()                                                   #clear players table
        self.listView_2.clear()                                                 #clear points table
        self.lineEdit_8.clear()                                                 #clear total points table
        sql1 = "select List_of_players from Teams_stats where team_name='" + team1 + "'"           #sql command
        cur1 = conn.execute(sql1)
        row1_tuple = cur1.fetchone()
        row1_string = row1_tuple[0]                                            # get the first and only element of the tuple
        row1 = ast.literal_eval(row1_string)                                   # use ast.literal_eval() to convert the string to a list
        selected = row1
        self.listView.addItems(selected)                                       #adding data in players table

    def evaluate(self):                                                         #evaluation of points function
        team1 = self.comboBox.currentText()                                     #check combobox1 current team selected
        conn=sqlite3.connect('Fantasy_cricket2.db')
        teamtotal=0
        
        self.listView_2.clear()
        
        matchname=self.comboBox_2.currentText()

        for i in range(self.listView.count()):
            total, batsc, bowlsc, fieldsc = 0, 0, 0, 0                          #initializing points to 0
            nm=self.listView.item(i).text()                                     #nm is initialised with player name according to the range
            sql="select * from '"+matchname+"' where player_name='"+nm+"'"               #sql command
            cur=conn.execute(sql)
            row=cur.fetchone()
            batsc=batsc+((row[2])/2)                                                     #calculate batsman score
            if row[2]>=50 and row[2]<100:
                batsc+=5
            elif row[2]>=100:
                batsc+=10
            elif row[2]>0:
                sr=row[2]/row[3]                                                #calculate batsman strike rate
                if sr>=80 and sr<=100:
                    batsc+=2
                elif sr>100:
                    batsc+=4
            batsc+=row[4]                                                       #calculate 4 bonus
            batsc+=2*row[5]                                                     #calculate 6 bonus
            bowlsc+=10*row[9]                                                   #calculate bowlers score
            if row[9]>=3 and row[9]<5:
                bowlsc+=5
            elif row[9]>5:
                bowlsc+=10
            if row[8]>0:
                ec=row[8]/(row[6])                                            #calculate economic rate of bowler
                if ec>=3.5 and ec<=4.5:
                    bowlsc+=4
                elif ec>=2 and ec<3.5:
                    bowlsc+=7
                elif ec<2:
                    bowlsc+=10
            fieldsc=(row[10]+row[11]+row[12])*10                                 #calculate fielders score
            total=batsc+bowlsc+fieldsc                                          #total score of each player
            teamtotal+=total                                                    #team's total score
            self.listView_2.addItem(str(total))                                 #displaying each player's score in list1
        self.lineEdit_8.setText(str(teamtotal))                                 #displaying team's total points

if __name__ == "__main__":                                                      #main function
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QDialog()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())