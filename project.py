"""
wip
"""

from rmfmaxxpl.Maxx import Maxx

maxx = Maxx()

# Scraping
hop_bec = maxx.GetHopBec()
playlista = maxx.GetPlaylista()

# Split for get Current Date and Artist Fuction
# playlista['Date Played']  = playlista["Date Played"].str.split(',', n=2, expand=True)[1].str.split('(', n=2, expand=True)[0]
# playlista[['Artist', 'Feat', 'Others_Artists']] = playlista["Artist"].str.split('/', n=2, expand=True).fillna('')

print(hop_bec[10]) 
print(playlista[3])
