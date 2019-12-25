import tkinter as tk
from web_scraper import WebScraper

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
		self.button['command'] = self.dump_albums 
		self.button.pack(side='bottom')

		# Text widget for output
		self.text_widget = tk.Text(self.root, width=200, height=200) 
		self.text_widget.pack(side='bottom')

	def dump_num_albums(self):
		'''Dump number of albums into the GUI for given artist.'''
		artist_name = self.entry.get()
		scraper = WebScraper(artist_name)
		text = f'Number of albums for {artist_name}: {scraper.num_albums}'
		self.new_label = tk.Label(self.root, text=text)
		self.new_label.pack(side='bottom')

	def dump_albums(self):
		'''Dump list of albums into the GUI for given artist.'''
		# If previous text is present, delete it
		try:
			self.text_widget.delete(1.0, tk.END)
		except:
			pass

		artist_name = self.entry.get()
		scraper = WebScraper(artist_name)
		
		# Set the album_dict: self.album_dict will be filled with relevant albums
		scraper._set_album_dict()

		album_list_str = f'Albums of {artist_name}:\n' + '*'*30 + '\n'
		for artist, albums in scraper.album_dict.items():
			if not scraper.onlyArtist:
				album_list_str += f'{artist}:\n' + '*'*30 + '\n'
			for album in albums:
				album_list_str += f'{album}\n'
			
			album_list_str += '*'*30 + '\n'

		# Update the text on the text widget 
		self.text_widget.insert('1.0', album_list_str)


app = ScrapeApp()
app.root.mainloop()
