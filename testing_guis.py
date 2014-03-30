"""
import sys
from PyQt4 import QtGui, QtCore

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        self.lbl = QtGui.QLabel("Ubuntu", self)

        combo = QtGui.QComboBox(self)
        combo.addItem("Ubuntu")
        combo.addItem("Mandriva")
        combo.addItem("Fedora")
        combo.addItem("Red Hat")
        combo.addItem("Gentoo")

        combo.move(50, 50)
        self.lbl.move(50, 150)

        combo.activated[str].connect(self.onActivated)        
         
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QtGui.QComboBox')
        self.show()
        
    def onActivated(self, text):
      
        self.lbl.setText(text)
        self.lbl.adjustSize()  
                
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
	
"""
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
from random import randint


app = QApplication(sys.argv)

model = QStandardItemModel()

for n in range(10):                   
    item = QStandardItem('Item %s' % randint(1, 100))
    check = Qt.Checked if randint(0, 1) == 1 else Qt.Unchecked
    item.setCheckState(check)
    item.setCheckable(True)
    model.appendRow(item)


view = QListView()
view.setModel(model)

view.show()
app.exec_()
"""
"""
import sys
from PyQt4 import QtGui, QtCore

class MainForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        listWidget = QtGui.QListWidget()

        item = QtGui.QListWidgetItem()
        item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
        item.setCheckState(QtCore.Qt.Unchecked)
        listWidget.addItem(item)

        widget = QtGui.QCheckBox('test')
        item.setSizeHint(widget.sizeHint())
        listWidget.setItemWidget(item, widget)

        listWidget.itemClicked.connect(self.on_listWidget_itemClicked)

        self.setCentralWidget(listWidget)

    def on_listWidget_itemClicked(self, item):
        if item.listWidget().itemWidget(item) != None: 
            if item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)
            else:
                item.setCheckState(QtCore.Qt.Checked)

def main():
    app = QtGui.QApplication(sys.argv)
    form = MainForm()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
	"""
            if i % 9 :

                cb1.insertItem( txt )
            else :
                cb1.listBox().insertItem( MyListBoxItem() )
            
        box2 = QVBox( row2 )
        box2.setSpacing( 5 )

        # Create an editable Combobox and a label below...
        cb2 = QComboBox( TRUE, box2 )
        self.label2 = QLabel( "Current Item: Combobox Item 0", box2 )
        self.label2.setMaximumHeight( self.label2.sizeHint().height() * 2 )
        self.label2.setFrameStyle( QFrame.Panel | QFrame.Sunken )

        # ... and insert 50 items into the Combobox
        for i in range(0, 50, 1 ) :
            txt = str(QString( "Combobox Item %1" ).arg( i ))
            if not i % 4 :
                cb2.insertItem( QPixmap( "fileopen.xpm" ), txt )
            else :
                cb2.insertItem( txt )
        
        # Connect the activated SIGNALs of the Comboboxes with SLOTs
        self.connect( cb1, SIGNAL("activated( const QString & )"), self.slotCombo1Activated )
        self.connect( cb2, SIGNAL("activated( const QString & )"), self.slotCombo2Activated )
    
    """ SLOT slotLeft2Right
    * Copies all selected items of the first ListBox into the second ListBox
    """
    def slotLeft2Right( self ):
        # Go through all items of the first ListBox
        for i in range( 0, self.lb1.count(), 1 ) :
            item = self.lb1.item( i )
            # if the item is selected...
            if self.lb1.isSelected( i ): #item.isSelected() :
                # ...and it is a text item...
                if item.pixmap() and not(item.text().isEmpty()):
                    self.lb2.insertItem( item.pixmap(), item.text() )
                elif not( item.pixmap() ):
                    self.lb2.insertItem( item.text() )
                elif item.text().isEmpty() :
                    self.lb2.insertItem( item.pixmap() )

    """ SLOT slotCombo1Activated( const QString &s )
    * Sets the text of the item which the user just selected in the
    * first Combobox (and is now the value of s) to the first Label.
    """
    def slotCombo1Activated( self, s ) :
        self.label1.setText( str(QString( "Current Item: %1" ).arg( s ) ) )
    
    """ SLOT slotCombo2Activated( const QString &s )
    * Sets the text of the item which the user just selected in the
    * second Combobox (and is now the value of s) to the second Label.
    """
    def slotCombo2Activated( self, s ) :
        self.label2.setText( str(QString( "Current Item: %1" ).arg( s ) ) )
    

class MyListBoxItem( QListBoxItem ):
    def __init__( self, parent=None, name=None ):
        QListBoxItem.__init__( self, parent, name )
        self.setCustomHighlighting( TRUE )
    
    def paint( self, painter ):
        # evil trick: find out whether we are painted onto our listbox
        in_list_box = 0
        if self.listBox() and self.listBox().viewport() == painter.device():
            in_list_box = 1
        r = QRect( 0, 0, self.width( self.listBox() ), self.height( self.listBox() ) )
        brush = QBrush( Qt.red, Qt.SolidPattern )
        if in_list_box and isSelected():
            painter.eraseRect( r )
        painter.fillRect( 5, 5, self.width( self.listBox() ) - 10, self.height( self.listBox() ) - 10, brush )
        if in_list_box and isCurrent():
            self.listBox().style().drawPrimitive( QStyle.PE_FocusRect, painter, r, self.listBox().colorGroup() )
            
    def width( self, QListBox ):
        return 100
    
    def height( self, QListBox ):
        return 16

    
def main( args ):
    a = QApplication( args )
    
    listboxcombo = ListBoxCombo()
    listboxcombo.resize( 400, 270 )
    listboxcombo.setCaption( "Qt Example - Listboxes and Comboboxes" )
    a.setMainWidget( listboxcombo )
    listboxcombo.show();
    
    a.exec_loop()
    
if __name__=="__main__":
    main(sys.argv)