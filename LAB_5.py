# -*- encoding: utf-8 -*-

import gi, os, time, sys
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository.GdkPixbuf import Pixbuf as pxbf


folder = '/lab_files'
# ~ try:
	# ~ os.mkdir(os.getcwd()+folder) #lab_files hardcoded (resolve)
# ~ except:
	# ~ pass
	
#------------------------------
from lab_files import *
list_of_files = ['systemsolver']#sorted(list(filter(lambda i : i != None,list(map(lambda i : i[0:-3] if (i[0] != "_") and (i[-1] != "t") else None, os.listdir(os.getcwd()+folder))))))
print(list_of_files)
#------------------------------

class Wind(Gtk.Window):
	counter = 0
	counter_file = 0
	angle_l2 = 0
	flag = 0
	focus_flag1 = 0
	req_var_counter = 0	
	res = {}
	name = ""
	
	def __init__(self):
		Gtk.Window.__init__(self, title="LAB_5", resizable=True, default_height = 400, default_width = 700)
		self.frame = Gtk.Frame()
		self.add(self.frame)
		
		self.screen = Gdk.Screen.get_default()
		self.css_provider = Gtk.CssProvider()
		self.style_context = Gtk.StyleContext()
		self.style_context.add_provider_for_screen(self.screen, self.css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
		
		#Backgroud : general
		css = "box * {font: 16px mono, monospace;}\
			   box#vb6 {background: #d9ffb3;\
						 border-radius: 4px;}\
			   label#l2 {background: #DCDCDC;\
						 color: yellow;\
						 border-radius: 4px 4px 0px 0px;\
						 text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;\
						 font: 18px Arial, monospace; font-weight: bold;}\
			    table#tr1 {text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;\
						  border : 2px;\
						  background: #DCDCDC;\
			    }\
			   "
		self.css_provider.load_from_data(css.encode("UTF-8"))
		
		self.box = Gtk.Box(spacing=6, name="b")
		self.frame.add(self.box)
		
		self.vbox = Gtk.VBox(spacing=6, height_request=110-30, name="vb")
		self.box.pack_start(self.vbox, True, True, 0)
		
		self.vbox2 = Gtk.VBox(spacing=6,height_request=290+30, name="vb2")
		self.vbox.pack_end(self.vbox2, True, True, 0)
		
		self.vbox3 = Gtk.VBox(spacing=6,height_request=30, name="vb3")
		self.vbox2.pack_end(self.vbox3, True, True, 0)
		
		self.vbox4 = Gtk.VBox(spacing=6, height_request=260+30, name="vb4")
		self.vbox3.pack_start(self.vbox4, True, True, 0)
		
		self.vbox5 = Gtk.VBox(spacing=6, height_request=170+30, name="vb5")
		self.vbox4.pack_end(self.vbox5, True, True, 0)
		
		self.vbox7 = Gtk.VBox(spacing=6, margin=3, name="vb7")
		self.vbox5.pack_end(self.vbox7, True, True, 0)
		
		self.frame = Gtk.Frame(label = "", width_request=300, margin_right=5, margin_bottom=5, name="f1")
		self.box.pack_start(self.frame, True, True, 0)
		
		self.vbox6 = Gtk.VBox(spacing=6, margin=3, name="vb6")
		self.frame.add(self.vbox6)
		
		
		self.box1 = Gtk.Box(spacing=6, height_request=40, name="b1")
		self.vbox6.pack_start(self.box1, True, True, 0)
		
		self.box2 = Gtk.Box(spacing=6, height_request=180, name="b2")
		self.vbox6.pack_start(self.box2, True, True, 0)
		
		self.box3 = Gtk.Box(spacing=6, height_request=180, name="b3")
		self.vbox6.pack_start(self.box3, True, True, 0)
		
		self.frame1 = Gtk.Frame(label="Результат", width_request=300, margin=5, name="f1")
		self.box3.pack_start(self.frame1, True, True, 0)
		
		
		self.init_control_elements()
		self.init_labels()
#		self.init_images()
		self.init_threads()
		self.handle_alg(self)
				
	def init_control_elements(self):
		
		self.button1 = Gtk.Button(label="Ввести", margin_top=25/2.0, margin_bottom=25/4.0, margin_left=5, margin_right=5, height_request=40)
		self.button1.connect("clicked", self.on_button_clicked)
		self.vbox.pack_start(self.button1, True, True, 0)
		
		self.button2 = Gtk.Button(label="Очистити", margin_top=25/4.0, margin_bottom=0, margin_left=5, margin_right=5, height_request=40)
		self.button2.connect("clicked", self.on_button_clicked2)
		self.vbox.pack_start(self.button2, True, True, 0)
		
		self.sep1 = Gtk.Separator(margin_left=5, hexpand=False, height_request=1)
		self.vbox.pack_end(self.sep1, True, True, 0)
		
		self.button3 = Gtk.Button(label="Виконати", margin_top=25/4.0, margin_bottom=0, margin_left=35, margin_right=35, height_request=20)
		self.button3.connect("clicked", self.on_button_clicked3)
		self.vbox4.pack_end(self.button3, True, True, 0)
		
		self.cb1 = Gtk.ComboBoxText(tearoff_title ="Select LAB", add_tearoffs=False, height_request=20, margin_left=5, margin_right=5, name="cb1")
		self.store = Gtk.ListStore(str)
#		self.cell = Gtk.CellRendererText()
#		self.cb1.pack_start(self.cell, True)
#		self.cb1.add_attribute(self.cell,'text', 0)
		for i in list_of_files:
			self.store.append(["{}".format(i)])
		self.vbox4.pack_end(self.cb1, True, True, 0)
		self.cb1.set_model(self.store)

#		self.cb1.set_active(0)
		self.cb1.connect("changed" ,self.handle_alg)

		self.ent1 = Gtk.Entry(placeholder_text="Введіть необхідні змінні", margin=5)
		self.ent1.connect("activate", self.on_button_clicked)
		self.box1.pack_end(self.ent1, True, True, 0)
		
	def init_labels(self):

		self.label1 = Gtk.Label(label="", margin_left=5, margin_right=5, margin_bottom=5, margin_top=5, name="l1")		#, halign=Gtk.Align.START
		self.label1.set_markup("<b>{} : </b>".format(self.counter))
		self.label1.set_justify(Gtk.Justification.LEFT)
		self.box1.pack_start(self.label1, True, False, 20)
		
		
		self.scrolledwindow = Gtk.ScrolledWindow()
		self.box2.add(self.scrolledwindow)	
		self.scrolledwindow.set_hexpand(True)
		
		self.tree1 = Gtk.TreeView.new_with_model(Gtk.ListStore(str,str,str))
		self.tree1.props.border_width = 2
		for i, column_title in enumerate(["№", "Змінна", "Значення"]):
			renderer = Gtk.CellRendererText()
			column = Gtk.TreeViewColumn(column_title, renderer, markup=i)
			self.tree1.append_column(column)
		self.scrolledwindow.add(self.tree1)
		
# fancy 1
		self.eventbox1 = Gtk.EventBox()
		self.vbox3.pack_start(self.eventbox1, True, True, 0)
		self.label2 = Gtk.Label(label="        ", angle=self.angle_l2, margin_left=5, height_request=35, width_request=35, name="l2", visible=False, focus_on_click=True, selectable=False)
		self.label2.set_justify(Gtk.Justification.CENTER)
		self.eventbox1.add(self.label2)
		self.eventbox1.connect("button-press-event" ,self.focus)
# fancy 1

		self.label3 = Gtk.Label(label= "Виберіть алгоритм")
		self.vbox4.pack_end(self.label3, True, True, 0)
		
		self.label4 = Gtk.Label(label="", margin_left=5, height_request=35, width_request=35, name="l4", visible=False, focus_on_click=True, selectable=False)
		self.label4.set_justify(Gtk.Justification.CENTER)
		self.frame1.add(self.label4)
	
	def init_images(self):
		self.pixbf = pxbf.new_from_file_at_size(os.getcwd()+'/plot.png',450,450)
		self.image = Gtk.Image.new_from_pixbuf(self.pixbf) 
		self.box.pack_start(self.image, False, True, 0)
		
	def init_threads(self):
		Gdk.threads_add_timeout(100, 10, self.rot)
			
	def on_button_clicked(self, widget):
		model = self.tree1.get_model()
		if len(self.req)-1 > self.counter:
			self.counter += 1
			read_from_entry = self.ent1.props.text
			self.label1.set_markup("<b>{} : </b>".format(list(self.req.keys())[self.counter]))
			self.res.update({list(self.req.keys())[self.counter-1] : read_from_entry})
			self.ent1.props.text = ""
			model.append([str(self.counter), list(self.req.keys())[self.counter-1], str(read_from_entry)])
		else: 
			read_from_entry = self.ent1.props.text
			self.res.update({list(self.req.keys())[self.counter] : read_from_entry})
			self.ent1.props.text = ""
			model.append([str(self.counter+1), list(self.req.keys())[self.counter], str(read_from_entry)])
			print("end of req")
		self.module.res = self.res
		print(self.module.res)

	def on_button_clicked2(self, widget):
		self.counter = 0
		model = self.tree1.get_model()
		model.clear()
		self.label4.props.label = ""
		self.res.clear()
		self.module.res = self.res
		print(self.module.res)
		Wind.handle_alg(self, widget)
	
	def on_button_clicked3(self, widget):
		self.label4.props.label = self.module.main()
		
	def focus(self, widget, event):
		if self.flag == 0 :
			self.label2.props.label="kekemon"
			self.focus_flag1 = 1
		else :
			self.label2.props.label=""
			self.focus_flag1 = 0
		
#fancy 1		     	
	def rot(self):

		if self.angle_l2 <= 10 and self.flag == 0 :
			self.angle_l2 += 0.2
		else :
			self.flag = 1  
		if self.angle_l2 >=-10 and self.flag == 1 :
			self.angle_l2 -= 0.2
		else :
			self.flag = 0
			
		self.label2.set_angle(self.angle_l2)
#		time.sleep(1)
		return True
#fancy 1	

	def handle_alg(self, widget):
		try:
			selected_alg = str(self.cb1.get_active_text())
			self.module = sys.modules.get(folder[1:]+'.'+selected_alg)
			self.req = self.module.req
		except:
			selected_alg = list_of_files[0]
			self.module = sys.modules.get(folder[1:]+'.'+selected_alg)
			self.req = self.module.req
		self.label1.set_markup("<b>{} : </b>".format(list(self.req.keys())[self.counter]))
		self.frame.props.label = self.module.name
		if widget == self.cb1 :
			self.read_from_file()
		
	def read_from_file(self):
		model = self.tree1.get_model()
		try:
			with open(os.getcwd()+folder+'/'+self.cb1.get_active_text()+'_defaults.txt','r') as loaded :
				loaded_list = loaded.read().splitlines()
				prepared_list = []
				for i in loaded_list: 
					k = i.split('=')
					k = list(map(lambda x : x.replace('\\n','\n'),k))
					prepared_list.append(k)
				prepared_list[-1][-1] = prepared_list[-1][-1][0:-1]
				self.res = dict(prepared_list)
				self.module.res = self.res
				model.clear()
				self.counter_file = 0
				self.counter_file += 1
				print(self.res)
				for i in range(len(self.res)):
					print([str(self.counter_file), list(self.res.keys())[self.counter_file-1], list(self.res.values())[self.counter_file-1]])
					model.append([str(self.counter_file), list(self.res.keys())[self.counter_file-1], list(self.res.values())[self.counter_file-1]])
					self.counter_file += 1
		except:
			print('Немає файлу зі стандартними налаштуваннями.\n {name}_defaults.txt'.format(name=self.cb1.get_active_text()))			

class IconView(Gtk.Window):

	def __init__(self):
		pass

def main():
	win = Wind()
	win.connect("destroy", Gtk.main_quit)
	win.show_all()
	Gtk.main()

if __name__ == "__main__" :
	main()
