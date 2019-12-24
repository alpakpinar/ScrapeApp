import tkinter as tk
from web_scraper import WebScraper

class ScrapeApp(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.create_widgets()
	
	def create_widgets(self):
		self.label = tk.Label(self, text='Artist Name')
		self.label.pack(side='top')

		self.entry = tk.Entry(self)
		self.entry.pack(side='top')

		self.button = tk.Button(self)
		self.button['text'] = 'Get Number of Albums'
		self.button['command'] = self.dump_num_albums 
		self.button.pack(side='bottom')
	
	def dump_num_albums(self):
		'''Dump number of albums into the GUI for given artist.'''
		artist_name = self.entry.get()
		scraper = WebScraper(artist_name)
		text = f'Number of albums for {artist_name}: {scraper.num_albums}'
		self.new_label = tk.Label(self, text=text)
		self.new_label.pack(side='bottom')


app = ScrapeApp()
app.mainloop()
