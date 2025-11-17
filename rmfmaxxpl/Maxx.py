# Imports
import os
import requests as rq

from bs4 import BeautifulSoup
# Class
class Scraping:
    """
    Makes request and returns website data
    """

    def __init__(self,
                 url='https://www.rmfmaxx.pl/',
                 header={'User-Agent' : os.getenv('USER_AGENT')}
                ):
        """
        Parameters
        ----------
        url : str
            The url base for webscraping (default is rmfmaxx.pl) 
        header : str
            The header contais your user-agent
        """
        self.url    = url
        self.header = header
    
    def GetPlaylista(self, path='muzyka/playlista', hours=24):
        """
        Gets the current playlist

        Args:
            path (str) : Complement of base url (default is 'muzyka/playlista')
            hours (int): The number of hours to be extracted (default is 24 == 1 day)

        Returns:
            dict: a dict with date, time, music title and artist name.
        """
        print('Scraping Playlista')
        playlista = []
        
        for hour in range(hours):
            # Get Page
            relative_url = self.url + path + f"/{hour}#p"
            page = rq.get(relative_url, headers=self.header)
            soup = BeautifulSoup(page.content, 'html.parser')
            
            # Find music playlist
            # Select 'list-songs' first 'cause sidebar HopBec have the same div class 'row my-4 song-row'
            playlist = soup.find('div', class_ = 'list-songs')      
            playlist = playlist.find_all('div', class_ = 'row my-4 song-row')

            # Progress tracking
            percent = round(((hour+1)/(hours))*100,2)
            pharse = f'{percent}%. Page {hour+1} of {hours}'
            print("\033[K", pharse, end='\r')
                
            # Find all music played
            for music in playlist:
                # Day 
                current_day = soup.find('b', class_='fw-500').get_text()
                # Time [CET UTC+01:00 or CEST UTC+02:00]
                time = music.find('div', class_ = 'song-options small text-muted').get_text().strip()
                # Title
                title = music.find('a', class_ = 'song-title text-muted').get_text()
                # Artist
                artist = music.find('div', class_ = 'song-artists').get_text()

                playlista.append({
                    'Date': current_day,
                    'Time': time,
                    'Title': title,
                    'Artist': artist
                    })
        print('')     
        print('Successful')
        return playlista

    def GetHopBec(self, path='hopbec/archiwalne'):
        """
        Gets the current HopBec

        Args:
            path (str) : Complement of base url (default is 'hopbec/archiwalne')

        Returns:
            dict: a dict with edition, position, music title and artist name.
        """
        print('Scraping HopBec')
        # Get Page
        rmf_hopbec = rq.get(self.url + path, headers=self.header)
        soup = BeautifulSoup(rmf_hopbec.content, 'html.parser')

        # Find music playlist
        # Select 'list-songs' first 'cause sidebar HopBec have the same div class 'row my-4 song-row'
        playlist = soup.find('div', class_ = 'list-songs')  
        playlist = playlist.find_all('div', class_ = 'row my-4 song-row')

        # Find all music played
        hop_bec = []
        for music in playlist:
            # Edition
            edition = soup.find('title').get_text()
            edition = edition[10:14]
            # Position
            position = music.find('span', class_ = 't-element-position mx-rounded bg-primary py-2 px-3 fw-bold').get_text().strip()
            # Title
            title = music.find('a', class_ = 'song-title text-muted').get_text()
            # Artist
            artist = music.find('div', class_ = 'song-artists').get_text()

            hop_bec.append({
                     'Edition'   : edition,
                     'Position'  : position,
                     'Title'     : title,
                     'Artist'    : artist
                     })

        print('Successful')
        return hop_bec