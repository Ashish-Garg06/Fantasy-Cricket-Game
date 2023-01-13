from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox
import json
import sqlite3

# global variable for value tracking
value_tracker=0
batsman_tracker=0
bowler_tracker=0
allrounder_tracker=0
wicket_keeper_tracker=0

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 588)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_4 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_4.addWidget(self.radioButton_4)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_4.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_4.addWidget(self.radioButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_5.addWidget(self.listWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_6.addWidget(self.label_15)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.listWidget_2.setFont(font)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_7.addWidget(self.listWidget_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW = QtWidgets.QAction(MainWindow)
        self.actionNEW.setObjectName("actionNEW")
        self.actionOPEN = QtWidgets.QAction(MainWindow)
        self.actionOPEN.setObjectName("actionOPEN")
        self.actionSAVE = QtWidgets.QAction(MainWindow)
        self.actionSAVE.setObjectName("actionSAVE")
        self.actionEVALUATE = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE.setObjectName("actionEVALUATE")
        self.menuManage_Teams.addAction(self.actionNEW)
        self.menuManage_Teams.addAction(self.actionOPEN)
        self.menuManage_Teams.addAction(self.actionSAVE)
        self.menuManage_Teams.addAction(self.actionEVALUATE)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        
        self.actionEVALUATE.triggered.connect(self.show_form)
        self.actionNEW.triggered.connect(self.prepare_new_window)
        self.listWidget.itemDoubleClicked.connect(self.rmv_from_lst1)
        self.listWidget_2.itemDoubleClicked.connect(self.rmv_from_lst2)
        self.radioButton_4.toggled.connect(self.update_list_for_bat)
        self.radioButton_3.toggled.connect(self.update_list_for_bwl)
        self.radioButton_2.toggled.connect(self.update_list_for_ar)
        self.radioButton.toggled.connect(self.update_list_for_Wktkeper)
        self.actionSAVE.triggered.connect(self.prepare_for_saving)
        
        self.warning_box=self.create_warning_box_for_wktkp_no()
        self.warning_box_2=self.create_warning_box_for_teamplayers_no()
        self.warning_box_3=self.create_warning_box_for_points_avlbl()
        self.warning_box_4=self.create_warning_box_for_blank_team_name()
        
        self.congratulation_box=self.create_congratulation_for_successful_save()
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.thread = None
        self.main_window=MainWindow
        
        

    def prepare_for_saving(self):
        if int(self.label_8.text())>1:
            self.warning_box.exec_()
            
        elif (self.listWidget_2.count()!=11):
            self.warning_box_2.exec_()
        
        else:
            teamname = self.lineEdit.text()
            if len(teamname)==0:
                self.warning_box_4.exec_()
            else:    
                teamlist = []
                teamvalue = int(self.label_10.text())
                for x in range(self.listWidget_2.count()):
                    teamlist.append(self.listWidget_2.item(x).text())

                # Convert the list to a string using json.dumps
                teamlist_str = json.dumps(teamlist)

                myplayer = sqlite3.connect("Fantasy_cricket2.db")

                sql = '''INSERT INTO Teams_stats
                (team_name,List_of_players ,Combined_value)
                VALUES (?,?,?);'''
                values = (teamname, teamlist_str, teamvalue)

                curplayer = myplayer.cursor()
                curplayer.execute(sql, values)
                myplayer.commit()
                
                self.congratulation_box.exec_()

                myplayer.close()
            
    def create_congratulation_for_successful_save(self):
        congratulation_box = QMessageBox()
        congratulation_box.setText("Team successfully saved")
        congratulation_box.setWindowTitle("Congratulations!!")
        congratulation_box.setIcon(QMessageBox.Information)
        congratulation_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        congratulation_box.setDefaultButton(QMessageBox.Ok)
        
        return congratulation_box
        
    def create_warning_box_for_wktkp_no(self):
        warning_box = QMessageBox()
        warning_box.setText("You can't select more than one wicketkeeper")
        warning_box.setWindowTitle("WARNING!!")
        warning_box.setIcon(QMessageBox.Warning)
        warning_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        warning_box.setDefaultButton(QMessageBox.Ok)
        
        return warning_box
    
    def create_warning_box_for_teamplayers_no(self):    
        warning_box_2 = QMessageBox()
        warning_box_2.setText("Team must contain only 11 players.")
        warning_box_2.setWindowTitle("WARNING!!")
        warning_box_2.setIcon(QMessageBox.Warning)
        warning_box_2.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        warning_box_2.setDefaultButton(QMessageBox.Ok)
        
        return warning_box_2
    
    def create_warning_box_for_points_avlbl(self):
        warning_box_3 = QMessageBox()
        warning_box_3.setText("You don't have enough points for this selection")
        warning_box_3.setWindowTitle("WARNING!!")
        warning_box_3.setIcon(QMessageBox.Warning)
        warning_box_3.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        warning_box_3.setDefaultButton(QMessageBox.Ok)
        
        return warning_box_3
    
    def create_warning_box_for_blank_team_name(self):
        warning_box_4 = QMessageBox()
        warning_box_4.setText("Team name can't be blank!")
        warning_box_4.setWindowTitle("WARNING!!")
        warning_box_4.setIcon(QMessageBox.Warning)
        warning_box_4.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        warning_box_4.setDefaultButton(QMessageBox.Ok)
        
        return warning_box_4
    
    def update_list_for_bat(self):
        self.listWidget.clear()
        
        myplayer=sqlite3.connect("Fantasy_cricket2.db")
        
        
        for counter in range(0, 15, 1):
            item = QtWidgets.QListWidgetItem()
            usrid=counter+1
            sql=("SELECT * from player_stat WHERE PlayerID ='" +str(usrid)+ "';")
            curplayer=myplayer.cursor()
            curplayer.execute(sql)
            player_record=curplayer.fetchone()
            if player_record[7]!="AR" and player_record[7]!="WK" and player_record[7]!="BWL" and player_record[7]=="BAT":
                player_name=player_record[1]
            
                # Check if player name is already in listwidget2
                already_in_listwidget2 = False
                for i in range(self.listWidget_2.count()):
                    if self.listWidget_2.item(i).text() == player_name:
                        already_in_listwidget2 = True
                        break
                    
                # Add player to listwidget if not already in listwidget2
                if not already_in_listwidget2:
                    item = QtWidgets.QListWidgetItem()
                    item.setText(player_name)
                    self.listWidget.addItem(item)
                
        myplayer.close()    
            
    def update_list_for_bwl(self):
        self.listWidget.clear()
        
        myplayer=sqlite3.connect("Fantasy_cricket2.db")
        
        
        for counter in range(0, 15, 1):
            item = QtWidgets.QListWidgetItem()
            usrid=counter+1
            sql=("SELECT * from player_stat WHERE PlayerID ='" +str(usrid)+ "';")
            curplayer=myplayer.cursor()
            curplayer.execute(sql)
            player_record=curplayer.fetchone()
            if player_record[7]!="BAT" and player_record[7]!="WK" and player_record[7]!="AR" and player_record[7]=="BWL":
                player_name=player_record[1]
            
                # Check if player name is already in listwidget2
                already_in_listwidget2 = False
                for i in range(self.listWidget_2.count()):
                    if self.listWidget_2.item(i).text() == player_name:
                        already_in_listwidget2 = True
                        break
                    
                # Add player to listwidget if not already in listwidget2
                if not already_in_listwidget2:
                    item = QtWidgets.QListWidgetItem()
                    item.setText(player_name)
                    self.listWidget.addItem(item)
                
        myplayer.close()    
    
    def update_list_for_ar(self) :
        self.listWidget.clear()
        
        myplayer=sqlite3.connect("Fantasy_cricket2.db")
        
        
        for counter in range(0, 15, 1):
            item = QtWidgets.QListWidgetItem()
            usrid=counter+1
            sql=("SELECT * from player_stat WHERE PlayerID ='" +str(usrid)+ "';")
            curplayer=myplayer.cursor()
            curplayer.execute(sql)
            player_record=curplayer.fetchone()
            if player_record[7]!="BWL" and player_record[7]!="WK" and player_record[7]!="BAT" and player_record[7]=="AR":
                player_name=player_record[1]
            
                # Check if player name is already in listwidget2
                already_in_listwidget2 = False
                for i in range(self.listWidget_2.count()):
                    if self.listWidget_2.item(i).text() == player_name:
                        already_in_listwidget2 = True
                        break
                    
                # Add player to listwidget if not already in listwidget2
                if not already_in_listwidget2:
                    item = QtWidgets.QListWidgetItem()
                    item.setText(player_name)
                    self.listWidget.addItem(item)
                
        myplayer.close()    
    
    def update_list_for_Wktkeper(self):
        self.listWidget.clear()
        
        myplayer=sqlite3.connect("Fantasy_cricket2.db")
        
        
        for counter in range(0, 15, 1):
            item = QtWidgets.QListWidgetItem()
            usrid=counter+1
            sql=("SELECT * from player_stat WHERE PlayerID ='" +str(usrid)+ "';")
            curplayer=myplayer.cursor()
            curplayer.execute(sql)
            player_record=curplayer.fetchone()
            if player_record[7]!="BWL" and player_record[7]!="AR" and player_record[7]!="BAT" and player_record[7]=="WK":
                player_name=player_record[1]
            
                # Check if player name is already in listwidget2
                already_in_listwidget2 = False
                for i in range(self.listWidget_2.count()):
                    if self.listWidget_2.item(i).text() == player_name:
                        already_in_listwidget2 = True
                        break
                    
                # Add player to listwidget if not already in listwidget2
                if not already_in_listwidget2:
                    item = QtWidgets.QListWidgetItem()
                    item.setText(player_name)
                    self.listWidget.addItem(item)
                
        myplayer.close() 
                
    def prepare_new_window(self):
        self.label_6.setStyleSheet("color: blue;")
        self.label_4.setStyleSheet("color: blue;")
        self.label.setStyleSheet("color: blue;")
        self.label_8.setStyleSheet("color: blue;")
        self.label_12.setStyleSheet("color: blue;")
        self.label_10.setStyleSheet("color: blue;")
        
        self.label_6.setText("0")
        self.label_4.setText("0")
        self.label.setText("0")
        self.label_8.setText("0")
        self.label_12.setText("1000")
        self.label_10.setText("0")
        
        self.listWidget.clear()
        self.listWidget_2.clear()
        
        # initialize the global variables every time new window is opened
        global value_tracker,batsman_tracker,bowler_tracker,allrounder_tracker,wicket_keeper_tracker
        value_tracker=0
        batsman_tracker=0
        bowler_tracker=0
        allrounder_tracker=0
        wicket_keeper_tracker=0
        
        for x in range (0,15,1) :
            item = QtWidgets.QListWidgetItem()
            self.listWidget.addItem(item)
            

            myplayer=sqlite3.connect("Fantasy_cricket2.db")
            if x<15:
                usrid=x+1
            else :
                usrid=x
            
            sql=("SELECT * from player_stat WHERE PlayerID ='" +str(usrid)+ "';")
            curplayer=myplayer.cursor()
            curplayer.execute(sql)
            player_record=curplayer.fetchone()
            player_name=player_record[1]
            
            myplayer.close()
            
            item = self.listWidget.item(x)
            item.setText(player_name)
            
    def rmv_from_lst1 (self, item):
        if int(self.label_12.text())>=0:

            selected_item_name =item.text()

            myplayer=sqlite3.connect("Fantasy_cricket2.db")
            sql=("SELECT * from player_stat WHERE player_name ='" +(selected_item_name)+ "';")
            curplayer=myplayer.cursor()
            curplayer.execute(sql)
            player_record=curplayer.fetchone()
            player_value=player_record[6]

            player_category=player_record[7]

            myplayer.close()
            
            
            if (int(self.label_12.text())-int(player_value))>0:
            
                global value_tracker
                value_tracker = value_tracker+int(player_value)
                available_points=1000-value_tracker


                if player_category=="BAT":
                    global batsman_tracker
                    batsman_tracker=batsman_tracker+1

                    self.label_6.setText(str(batsman_tracker))


                elif player_category=="BWL":
                    global bowler_tracker
                    bowler_tracker=bowler_tracker+1

                    self.label_4.setText(str(bowler_tracker))

                elif player_category=="AR":
                    global allrounder_tracker
                    allrounder_tracker=allrounder_tracker+1

                    self.label.setText(str(allrounder_tracker))

                elif player_category == "WK":
                    global wicket_keeper_tracker
                    wicket_keeper_tracker=wicket_keeper_tracker+1

                    self.label_8.setText(str(wicket_keeper_tracker))





                if int(self.label_12.text())<200:
                    self.label_12.setStyleSheet("color: red;")
                    self.label_12.setText(str(available_points))
                else:    
                    self.label_12.setStyleSheet("color: blue;")
                    self.label_12.setText(str(available_points))

                self.label_10.setStyleSheet("color: blue;")
                self.label_10.setText(str(value_tracker))
                
                self.listWidget.takeItem(self.listWidget.row(item))
                self.listWidget_2.addItem(item.text())
            
            else:
                self.warning_box_3.exec_()
        else:
            self.warning_box_3.exec_()
            
  
    def rmv_from_lst2 (self, item):
        self.listWidget_2.takeItem(self.listWidget_2.row(item))
        self.listWidget.addItem(item.text())
        
        selected_item_name =item.text()
        
        myplayer=sqlite3.connect("Fantasy_cricket2.db")
        sql=("SELECT * from player_stat WHERE player_name ='" +(selected_item_name)+ "';")
        curplayer=myplayer.cursor()
        curplayer.execute(sql)
        player_record=curplayer.fetchone()
        player_value=player_record[6]
        player_category=player_record[7]
        myplayer.close()
        
        if player_category=="BAT":
            global batsman_tracker
            batsman_tracker=batsman_tracker-1
            
            self.label_6.setText(str(batsman_tracker))
            
        
        elif player_category=="BWL":
            global bowler_tracker
            bowler_tracker=bowler_tracker-1
            
            self.label_4.setText(str(bowler_tracker))
            
        elif player_category=="AR":
            global allrounder_tracker
            allrounder_tracker=allrounder_tracker-1
            
            self.label.setText(str(allrounder_tracker))
               
        elif player_category == "WK":
            global wicket_keeper_tracker
            wicket_keeper_tracker=wicket_keeper_tracker-1
            
            self.label_8.setText(str(wicket_keeper_tracker))
        
        global value_tracker
        value_tracker=value_tracker-int(player_value)
        
        available_points=int(self.label_12.text())+int(player_value)
        
        if int(self.label_12.text())<200:
            self.label_12.setStyleSheet("color: red;")
            self.label_12.setText(str(available_points))
        else:    
            self.label_12.setStyleSheet("color: blue;")
            self.label_12.setText(str(available_points))
        
        self.label_10.setStyleSheet("color: blue;")
        self.label_10.setText(str(value_tracker))

    
    def show_form(self,main_window):
        from evaluation import Ui_Form                                      #import evaluate.py
        Form = QtWidgets.QDialog()
        ui = Ui_Form()
        ui.setupUi(Form)
        ret = Form.exec()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "Your Selections"))
        self.label_2.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.label_6.setText(_translate("MainWindow", "1"))
        self.label_5.setText(_translate("MainWindow", "Bowler(BWL)"))
        self.label_4.setText(_translate("MainWindow", "2"))
        self.label_3.setText(_translate("MainWindow", "Allrounders(AR)"))
        self.label.setText(_translate("MainWindow", "3"))
        self.label_9.setText(_translate("MainWindow", "WicketKeepers(WK)"))
        self.label_8.setText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "Points Available"))
        self.label_12.setText(_translate("MainWindow", "###"))
        self.label_13.setText(_translate("MainWindow", "Points Used"))
        self.label_10.setText(_translate("MainWindow", "555"))
        self.radioButton_4.setText(_translate("MainWindow", "BAT"))
        self.radioButton_3.setText(_translate("MainWindow", "BWL"))
        self.radioButton_2.setText(_translate("MainWindow", "AR"))
        self.radioButton.setText(_translate("MainWindow", "WK"))
        self.label_15.setText(_translate("MainWindow", "Team name"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE.setText(_translate("MainWindow", "EVALUATE Team"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())