#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Importamos la librerias que necesitamos
import preprocesoTweets as pt
import modelo as mdl
import about as info
import analisisResultados as anr
import numpy as np
import collections
try:
    import pygtk
    pygtk.require('2.0') # Intenta usar la versión 2
except:
    # algunos distribuciones con GTK2, pero no con pyGTK
    pass

try:
    import gtk
    import gtk.glade
except:
    print 'You nedd to install pyGTK or GTKv2 or set yout PYTHONPath correcty'
    sys.exit(1)


## funciones
def palabrasPorArchivo(nombreArchivo):
    v,sumba,lema=pt.preprocesar(nombreArchivo)
    l=pt.graficar(sumba)
    return l


## Interfaz Grafica (gtk-glade), Clase principal loopWhile
class MaiGui:
    "GTK/Glade User interface. This is a pyGTK window"
    def __init__(self):
        # Le indicamos al programa que archivo XML de glade usar
##        self.widgets=gtk.glade.XML("GuiTweets.glade")
        #se definen las señales
        signals={"gtk_main_quit":gtk.main_quit,
                 "On_click_button1":self.on_click_button1,
                 "On_active_vocab":self.on_active_vocab,
                 "On_active_about":self.on_active_about,
                 "On_active_open":self.on_active_open,
                 "On_clicked_button2":self.on_clicked_button2}
        
        self.gladefile = "GuiTweets.glade" 
        self.glade = gtk.Builder()
        self.glade.add_from_file(self.gladefile)
        self.glade.connect_signals(signals)
        self.window=self.glade.get_object('window1')
        if self.window:
            self.window.connect('destroy',gtk.main_quit)
        self.glade.get_object("window1").show_all()

        # se auto conectan las señales
##        self.widgets.signal_autoconnect(signals)

        # del archivo glade obtenemos los widgets a usar
        self.entry1=self.glade.get_object('entry1')
        self.textview1=self.glade.get_object('textview1')
        self.combobox1=self.glade.get_object('combobox1')
        self.combobox2=self.glade.get_object('combobox2')
        self.model=None
        ## cargar datos en el combo
        

    # Ventana generica de error (se le pasan los mensajes de error a nuestra ventana
    # de dialogo)
    def error(self, message):
        "dispay error dialog"
        dialog_error=gtk.MessageDialog(parent=None, flags=0,buttons=gtk.BUTTONS_OK)
        dialog_error.set_title("Error")
        label=gtk.Label(message)
        dialog_error.vbox.pack_start(label,True,True,0)
        # Con show_all() mostramos el contenido del dialogo en este caso
        # solo tiene la etiqueta. si no se hace aparece el cuadro vacio
        dialog_error.show_all()
        # El run y el destroy hace que la ventana se cierre al apretar el boton
        dialog_error.run()
        dialog_error.destroy()

    ## creamos ventana About
    def about_info(self,data=None):
        "Display the about dialog"
        Info=info.info()
        a=gtk.AboutDialog()
        a.set_name(Info.name)
        a.set_version(Info.version)
        a.set_comments(Info.description)
##        a.set_coyright(Info.copyright)
        def openHomePage(widget,url,url2): # Para abrir sitio
            import webbrowser
            webbrowser.open_new(url)

        gtk.about_dialog_set_url_hook(openHomePage,Info.website)
        a.set_website(Info.website)
        a.set_authors(Info.authors)
        a.set_license(Info.license)
        a.set_wrap_license(True) # Adapata el texto a la ventana
        a.run()
        a.destroy()

    ## definimos la ventana about
    def on_active_about(self,widget):
        "Open the About window"
        self.about_info()

    def on_active_open(self,widget):
        ## creamos el dialogo
        chooser=gtk.FileChooserDialog(title='Abrir Archivo resultados',action=gtk.FILE_CHOOSER_ACTION_OPEN,
                                      buttons=(gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,gtk.STOCK_OPEN,gtk.RESPONSE_OK))
        chooser.set_current_folder('C:\\Users\\ITACHI\\Documents\\Proyecto final\\Codigo')
        response=chooser.run()
        if response==gtk.RESPONSE_OK:
            filename=chooser.get_filename()
            self.resultado=anr.cargarResultados(filename)
            self.model=gtk.ListStore(str)
            self.model2=gtk.ListStore(str)
            clases=collections.Counter(self.resultado[0])
            for i in range(len(self.resultado)):
                self.model2.append(str(i))
            self.combobox2.set_model(self.model2)
            self.cell2=gtk.CellRendererText()
            self.combobox2.pack_start(self.cell2,True)
            self.combobox2.add_attribute(self.cell2,'text',0)
            self.combobox2.set_active(0)
            for c in clases.keys():
                self.model.append(str(c))
            self.combobox1.set_model(self.model)
            self.cell=gtk.CellRendererText()
            self.combobox1.pack_start(self.cell,True)
            self.combobox1.add_attribute(self.cell,'text',0)
            self.combobox1.set_active(0)
        elif response==gtk.RESPONSE_CANCEL:
            print "no seleccionado"
        chooser.destroy()
        
        
        

    ## mostramos palabras por archivo
    def on_click_button1(self,widget):
        "muestra las palabras mas comunes por documento"
        # ontenemos a partir de la entrada
        archivo=self.entry1.get_text()
        palabrasPorArchivo(archivo)

    ## mostramos el vocabulario
    def on_active_vocab(self,widget):
        # creamos un textbuffer para el resultado
        text_buffer=gtk.TextBuffer()
        #cargamos los datos del vocabulario
        voca=mdl.vocabularioTotal()
        for j in voca:
            text_buffer.set_text(str(j)+'\n')
        ## mostramos el buffer en el text view
        self.textview1.set_buffer(text_buffer)
        
    def on_clicked_button2(self,widget):
        #obtener valor del combobox
        indexactivo=self.combobox1.get_active()
        indexc=self.combobox2.get_active()
        ##analisis de resultados
        c1,c2,c3,c4,c5=anr.organizarPorClase(anr.tweets,self.resultado[indexc])
        if indexactivo==0:
            activo=c1
        elif indexactivo==1:
            activo=c2
        elif indexactivo==2:
            activo=c3
        elif indexactivo==3:
            activo=c4
        else:
            activo=c5 
        b=pt.bow(activo)
        bows=pt.bowDocumento(b[0])
        pt.graficar(bows)
        

if __name__=='__main__':
    MaiGui()
    gtk.main()
