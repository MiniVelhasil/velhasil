import xml

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
import atasozlerOneri
import velhasil
import os
import sys

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        layout = QVBoxLayout()
        self.editor = QPlainTextEdit()  # Could also use a QTextEdit and set self.editor.setAcceptRichText(False)

        # Setup the QTextEdit editor configuration
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

        layout.addWidget(self.editor)
        self.listwidget = QListWidget ()
        self.listwidget.setFont (fixedfont)
        layout.addWidget(self.listwidget)
        self.listwidget.hide()


        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        file_toolbar = QToolBar("Dosya")
        file_toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(file_toolbar)
        file_menu = self.menuBar().addMenu("&Dosya")

        open_file_action = QAction(QIcon(os.path.join('images', 'icons8-opened-folder-50.png')), "Dosya Aç...", self)
        open_file_action.setStatusTip("Dosya Aç")
        open_file_action.triggered.connect(self.file_open)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join('images', 'icons8-save-50.png')), "Kaydet", self)
        save_file_action.setStatusTip("Gerçerli Metni Kaydet")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        saveas_file_action = QAction(QIcon(os.path.join('images', 'icons8-save-as-50.png')), "Farklı Kaydet...", self)
        saveas_file_action.setStatusTip("Geçerli Dosyayı Farklı Kaydet")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)
        file_toolbar.addAction(saveas_file_action)

        print_action = QAction(QIcon(os.path.join('images', 'icons8-print-50.png')), "Yazdır...", self)
        print_action.setStatusTip("Geçerli Sayfayı Yazdır")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)
        file_toolbar.addAction(print_action)

        edit_toolbar = QToolBar("Düzenle")
        edit_toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(edit_toolbar)
        edit_menu = self.menuBar().addMenu("&Düzenle")

        undo_action = QAction(QIcon(os.path.join('images', 'icons8-undo-50.png')), "Geri Al", self)
        undo_action.setStatusTip("Son Değişikliği Geri Al")
        undo_action.triggered.connect(self.editor.undo)
        edit_toolbar.addAction (undo_action)
        edit_menu.addAction(undo_action)

        redo_action = QAction(QIcon(os.path.join('images', 'icons8-redo-50.png')), "Yinele", self)
        redo_action.setStatusTip("Son Değişikliği Yinele")
        redo_action.triggered.connect(self.editor.redo)
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        cut_action = QAction(QIcon(os.path.join('images', 'icons8-cut-50.png')), "Kes", self)
        cut_action.setStatusTip("Seçili Metni Kes")
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)

        copy_action = QAction(QIcon(os.path.join('images', 'icons8-copy-50.png')), "Kopyala", self)
        copy_action.setStatusTip("Seçili Metni Kopyala")
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)

        paste_action = QAction(QIcon(os.path.join('images', 'icons8-paste-50.png')), "Yapıştır", self)
        paste_action.setStatusTip("Yapıştır")
        paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)

        select_action = QAction(QIcon(os.path.join('images', 'icons8-rename-50.png')), "Tümünü Seç", self)
        select_action.setStatusTip("Tüm Metni Seçer")
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)

        edit_menu.addSeparator()

        wrap_action = QAction(QIcon(os.path.join('images', 'icons8-text-width-50.png')), "Metni Pencereye Sığdır", self)
        wrap_action.setStatusTip("Metni Pencereye Sığdır")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)
        edit_menu.addAction(wrap_action)

        Velhasıl_toolbar = QToolBar("Velhasıl")
        Velhasıl_toolbar.setIconSize(QSize(32, 32))
        self.addToolBar(Velhasıl_toolbar)
        Velhasıl_menu = self.menuBar().addMenu("&Velhasıl")

        yazimdenetimi_action = QAction(QIcon(os.path.join('images', 'icons8-spellcheck-50.png')), "Yazım Denetimi", self)
        yazimdenetimi_action.setStatusTip("Yazım Denetimi Yap")
        yazimdenetimi_action.triggered.connect(self.yazimDenetimi)
        Velhasıl_toolbar.addAction(yazimdenetimi_action)
        Velhasıl_menu.addAction(yazimdenetimi_action)

        cumle_action = QAction(QIcon(os.path.join('images', 'icons8-check-book-50.png')), "Cümle Analizi", self)
        cumle_action.setStatusTip("Cümle Ve Metin Analizi Yapar")
        cumle_action.triggered.connect(self.cumleAnalizi)
        Velhasıl_toolbar.addAction(cumle_action)
        Velhasıl_menu.addAction(cumle_action)

        istatistik_action = QAction(QIcon(os.path.join('images', 'icons8-futures-50.png')), "Metin İstatistikleri", self)
        istatistik_action.setStatusTip("Metin istatistiklerini Gösterir")
        istatistik_action.triggered.connect(self.istatistikGoster)
        Velhasıl_toolbar.addAction(istatistik_action)
        Velhasıl_menu.addAction(istatistik_action)

        atasozu_action = QAction(QIcon(os.path.join('images', 'icons8-concept-50.png')), "Atasözü Öner", self)
        atasozu_action.setStatusTip("Metinle Alakalı Atasözleri Gösterir")
        atasozu_action.triggered.connect(self.atasozuOneri)
        Velhasıl_toolbar.addAction (atasozu_action)
        Velhasıl_menu.addAction(atasozu_action)

        self.velhasil_ = velhasil.Velhasil ()

        self.update_title()
        self.show()

    def dialog_critical(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(self, "Dosya Aç", "", "Metin Dosyaları (*.txt);All files (*.*)")

        if path:
            try:
                with open(path, 'rU',encoding="UTF-8") as f:
                    text = f.read()

            except Exception as e:
                self.dialog_critical(str(e))

            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()

    def file_save(self):
        if self.path is None:
            # If we do not have a path, we need to use Save As.
            return self.file_saveas()

        self._save_to_path(self.path)

    def file_saveas(self):
        path, _ = QFileDialog.getSaveFileName(self, "Dosya Kaydet", "", "Metin Dosyaları (*.txt);All files (*.*)")

        if not path:
            # If dialog is cancelled, will return ''
            return

        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.toPlainText()
        try:
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))

        else:
            self.path = path
            self.update_title()

    def file_print(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            self.editor.print_(dlg.printer())

    def update_title(self):
        self.setWindowTitle("%s - Velhasıl..." % (os.path.basename(self.path) if self.path else "Başlıksız"))

    def edit_toggle_wrap(self):
        self.editor.setLineWrapMode( 1 if self.editor.lineWrapMode() == 0 else 0 )

    def atasozuOneri(self):
        self.listwidget.clear ()
        self.listwidget.show ()
        textboxValue = self.editor.toPlainText ()

        atasozleri_ = atasozlerOneri.AtasozleriOneri ()
        oneriler = atasozleri_.atasozuBul (textboxValue)

        oneriler.sort (reverse=True)
        if len(oneriler)==0:
            self.listwidget.addItem("Atasözü Önerisi Bulunamadı...")
        for i in oneriler:
            self.listwidget.addItem (i)


    def yazimDenetimi(self):
        self.listwidget.clear ()
        self.editor.setLineWrapMode(0)

        textboxValue = self.editor.toPlainText ().rstrip()
        #
        textboxValue = textboxValue.replace("\n", " *** ")
        kelimeler= textboxValue.split(" ")
        self.editor.clear()


        oneriler =""
        kontrol = self.velhasil_.yazimDenetimi(textboxValue.rstrip())
        print(kontrol)
        #print(kelimeler)
        newText =""
        for count, kelime in enumerate(kelimeler):
            print(kelime)
            if kelime=="***":
                newText += "<br>"
            elif (kontrol[count]==0):
                newText += kelime+" "
            elif (kontrol[count]==1):
                newText += '<span style="background-color: blue";color:white>'+str(kelime)+'</span>' + " "
                #for i in velhasil_.kelimeOneri(kelime):
                   #self.listwidget.addItem(kelime,i)
            elif (kontrol[count]==2):
                if not (self.velhasil_.isCorrect (str(kelime))):
                    newText += '<span style="background-color: red";color:white>'+str(kelime)+'</span>' + " "
            elif (kontrol[count] == 3):
                newText += '<span style="background-color: yellow";color:yellow>'+str(kelime)+'</span>' + " "
            elif (kontrol[count] == 4):
                newText += '<span style="background-color: green";color:green>'+str(kelime)+'</span>' + " "
            elif (kontrol[count] == 5):
                newText += '<span style="background-color: #999966";color:white>'+str(kelime)+'</span>' + " "
            elif (kontrol[count] == 6):
                newText += '<span style="background-color: brown";color:brown>'+str(kelime)+'</span>' + " "

        print(newText)

        self.editor.appendHtml(newText)
        test = 1
        #self.listwidget.addItem ("Kelime sayisi :"+ str(velhasil_.kelimesayisi))
        self.editor.setLineWrapMode (1)


    def cleanhtml(raw_html):
        return

    def istatistikGoster(self):
        self.listwidget.clear ()
        self.listwidget.show ()
        textboxValue = self.editor.toPlainText ()
        velhasil__ = velhasil.Velhasil (textboxValue)
        self.listwidget.addItem ("Kelime sayisi :"+ str(velhasil__.kelimesayisi))
        self.listwidget.addItem ("Kelime sayisi :"+ str(velhasil__.kelimesayisi))
        self.listwidget.addItem ("benzersiz kelime sayisi :"+ str(velhasil__.benzersizkelimesayisi))
        self.listwidget.addItem ("Karakter sayisi :"+ str(velhasil__.karaktersayisi))
        self.listwidget.addItem ("Benzersiz karakter sayisi :"+ str(velhasil__.benzersizkaraktersayisi))
        self.listwidget.addItem ("Paragraf sayisi :"+ str(velhasil__.paragrafSayisi))
        self.listwidget.addItem ("Cümle sayisi :"+ str(velhasil__.cumleSayisi))
        self.listwidget.addItem ("Kelimeler :"+ str( velhasil__.benzersizkelimeler))

    def mousePressEvent(self, event):

        if event.button () == Qt.RightButton:
            print ('right')  # FOR DEBUGGING
            #nokta = event.pos().x()
            textCursor = self.editor.cursorForPosition (QPoint(event.pos().x(), event.pos().y()-70))
            #print(event.pos().x())
            textCursor.select (QTextCursor.WordUnderCursor)
            self.editor.setTextCursor (textCursor)
            self.word = textCursor.selectedText ()
            print("word : ",self.word)

        menu = QMenu ()

        VelAction = menu.addAction ("Velhasıl")
        menu.addSeparator ()

        if self.word != "" or len (self.word) > 1 or self.word != " ":
            print ("burada")
            print (self.velhasil_.isCorrect (self.word))
            if not (self.velhasil_.isCorrect (self.word)):
                for i, kelime in enumerate (set (self.velhasil_.kelimeOneri (self.word))):
                    kelime = menu.addAction (kelime)
            elif len(self.velhasil_.turkcesiniOner(self.word))>0:
                for kelime in self.velhasil_.turkcesiniOner(self.word):
                    kelime = menu.addAction(kelime)
        #quitAction = menu.addAction ("Quit")
        action = menu.exec_ (self.mapToGlobal (event.pos ()))
        print(str(action.text()))

        if action != VelAction:
            self.degistir(str(action.text()))
        menu.addSeparator ()
        #if action == quitAction:
            #qApp.quit ()

        if event.button()==Qt.LeftButton:
               pass# menu.destroy()

    def degistir(self,kelime):


        metin = self.editor.toPlainText ().rstrip()
        #

        print(metin)
        cursor = self.editor.textCursor ()
        metin = metin[:cursor.selectionStart ()] +" "+ kelime+" " + metin[ cursor.selectionEnd ():]
        self.editor.clear ()
        metin = metin.replace ("\n", " <br> ")
        print(metin)

        self.editor.appendHtml((metin))
        self.yazimDenetimi()

    def cumleAnalizi(self):
        metin = self.editor.toPlainText()
        self.editor.clear()
        velhasil__ = velhasil.Velhasil (metin)
        newText =""
        cumleler=[]
        for cumle in velhasil__.cumleler:
            print(cumle)
            #print(len(cumle.split(" ")))
            test = (velhasil__.cumleBolucu(cumle))
            if (test==1):
                print(cumle)
                newText += '<span style="background-color: yellow">' + str (cumle) + '</span>' + " "
            elif cumle =="\n" or cumle =="":
                newText += "<br>"
            else:
                newText += str(cumle)+ " "

        self.editor.appendHtml(newText)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setApplicationName("Velhasıl...")

    window = MainWindow()
    app.exec_()