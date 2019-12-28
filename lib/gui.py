import tkinter as tk
from .web_scraper import WebScraper
from functools import partial

class ScrapeApp:
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('ScrapeApp')
		self.root.geometry('500x500')
		self.create_widgets()

	def create_widgets(self):
		self.label = tk.Label(self.root, text='Artist Name')
		self.label.pack(side='top')

		# Entry field for artist name
		self.entry = tk.Entry(self.root)
		self.entry.pack(side='top')

		# Button widget
		self.button = tk.Button(self.root)
		self.button['text'] = 'Get Albums'
		self.button['command'] = partial(self.dump_albums, event=None) 
		self.button.pack(side='top')

		# Text widget for output
		self.text_widget = tk.Text(self.root, width=200, height=200) 
		self.text_widget.pack(side='bottom')
		
		# Bind enter (return) key with the button
		self.root.bind('<Return>', self.dump_albums)

	def dump_num_albums(self):
		'''Dump number of albums into the GUI for given artist.'''
		artist_name = self.entry.get()
		scraper = WebScraper(artist_name)
		text = f'Number of albums for {artist_name}: {scraper.num_albums}'
		self.new_label = tk.Label(self.root, text=text)
		self.new_label.pack(side='bottom')

	def dump_albums(self, event):
		'''Dump list of albums into the GUI for given artist.'''
		# If previous text is present, delete it
		try:
			self.text_widget.delete(1.0, tk.END)
		except:
			pass

		artist_name = self.entry.get()
		scraper = WebScraper(artist_name)
		
		# Set the album_dict containing the album list for the artist
		# if the artist can be found in the Wikipedia link.
		# Otherwise, display an error message and terminate the function.
		try:
			scraper._set_album_dict()
		except:
			error_msg = f"Oops! Couldn't find data for {artist_name}."
			self.text_widget.insert('1.0', error_msg)
			return -1

		album_list_str = f'Albums of {artist_name}:\n' + '*'*30 + '\n'
		for artist, albums in scraper.album_dict.items():
			if not scraper.onlyArtist:
				album_list_str += f'{artist}:\n' + '*'*30 + '\n'
			for album in albums:
				album_list_str += f'{album}\n'
			
			album_list_str += '*'*30 + '\n'

		# Update the text on the text widget 
		self.text_widget.insert('1.0', album_list_str)

class StartWindow:
	'''Start window for the ScrapeApp.'''
	def __init__(self):
		self.root = tk.Tk()
		self.root.title('ScrapeApp')
		self.root.geometry('500x500')
		self.create_widgets()
	
	def create_widgets(self):
		self.label = tk.Label(self.root, text='ScrapeApp', font=('Times', 22))
		self.label.pack(side='top')

		button_style = self.get_button_styles()
		start_button_style = button_style['Start Button']
		quit_button_style = button_style['Quit Button']

		self.start_button = tk.Button(self.root, **start_button_style)
		self.start_button['text'] = 'Get Started!'
		self.start_button['command'] = self.launch_app
		self.start_button.pack(side='top')

		self.quit_button = tk.Button(self.root, **quit_button_style)
		self.quit_button['text'] = 'Quit'
		self.quit_button['command'] = self.root.destroy
		self.quit_button.pack(side='bottom')

	def get_button_styles(self):
		'''Get a dictionary containing the style of 
		the "Start" and "Quit" buttons that appear 
		in the starting page.'''
		style = {
			'Start Button' : {
				'font': ('Calibri', 22, 'bold', 'underline'),
				'borderwidth': 4,
				'foreground' : 'red'
			},
			'Quit Button' : {
				'font' : ('Calibri', 20)
			}
		}

		return style

	def launch_start_window(self):
		'''Launch the start window.'''
		self.root.mainloop()

	def launch_app(self):
		'''Launch the ScrapeApp.'''
		app = ScrapeApp()
		app.root.mainloop()




