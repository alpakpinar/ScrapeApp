#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup
import tkinter as tk

class WebScraper:
    '''Class for scraping Wikipedia for artists.
       Example usage:
       >>> scraper = WebScraper('Porcupine Tree')
       >>> scraper.get_discography() # Will print the discography of the artist
       >>> scraper.num_albums # Will return the number of albums that the artist has released
    '''
    def __init__(self, artist_name):
        self.artist_name = artist_name
        # Transform the artist name for the URL
        artist_name = '_'.join(artist_name.split(' '))
        self.link = 'https://en.wikipedia.org/wiki/' + artist_name
        self.response = requests.get(self.link)
        # Raise exception if GET request fails
        self.response.raise_for_status()
        self.artist_name = ' '.join(artist_name.split('_'))
        print('Data taken from:', self.link)
    
    def __repr__(self):
        print_str = f'WebScraper object with artist {self.artist_name}'
        return print_str
    
    @property
    def text(self):
        self.soup = BeautifulSoup(self.response.text, "html.parser")
        return self.soup
    
    def get_discography(self, print_results=True):
        '''Get the discography of the artist.'''
        # Get the unordered list containing the discography of the artist
        discography_header = self.text.find_all(id='Discography')[0]
        assert len(discography_header) == 1
        # Create a dictionary containing artists and albums
        self.album_dict = {}
        current_element = discography_header
        
        # Find and loop through each dl element if there are some
        if current_element.findNext('dl'):
            while current_element.findNext('dl'):
                onlyArtist = False
                current_element = current_element.findNext('dl')
                current_artist = current_element.getText()

                albums = []
                albums_ul = current_element.findNext('ul')
                album_items = albums_ul.find_all('li')
                for album in album_items:
                    albums.append(album.getText())
                self.album_dict[current_artist] = albums
        
        # Handle the case if there is no dl element in HTML source code
        else:
            onlyArtist = True
            albums = []
            current_artist = self.artist_name
            albums_ul = current_element.findNext('ul')
            album_items = albums_ul.find_all('li')
            for album in album_items:
                albums.append(album.getText())
            self.album_dict[current_artist] = albums
            
        # Print the albums, if requested
        if print_results:
            print('*'*30)
            print(f'Albums of {self.artist_name}:')
            print('*'*30)
            for artist, albums in self.album_dict.items():
                if not onlyArtist:
                    print(f'With artist: {artist}')
                for album in albums:
                    print(album)
                print('*'*30)
    
    def _set_album_dict(self):
        '''Sets the album_dict class variable by running get_discography.'''
        self.get_discography(print_results=False)
        
    @property
    def num_albums(self):
        '''Returns the number of albums that the artist has released.'''
        num_albums = 0
        self._set_album_dict()
        albums_list = list(self.album_dict.values())
        for album_list in albums_list:
            num_albums += len(album_list)
        return num_albums
        
        
    


