# User Albums

def make_album(artist_name, album_tittle, num_songs= None):
    
    album= {'Artist': artist_name, ' Album Tittle': album_tittle}
    
    if num_songs:
        album['Number of Songs']= num_songs

    return album
'''   
album1= make_album ('Drake', 'For the dogs', '15')
album2= make_album ('Kanye West', 'Donda')
album3= make_album ('Bad Bunny','YHLQMDLG', '11')
   
print (album1)
print (album2)
print (album3)
'''
while True:
    print("Please enter the album information")
    print( ("Enter 'q' at any time to quit") )

    artist= input (" Artist Name: ")
    if artist== 'q':
        break
    tittle= input (" Album Tittle: ")
    if tittle== 'q':
        break
    songs= input (" Number of songs: ")
    if songs== 'q':
        break
    if songs== '':
       songs= None

album_info= make_album (artist, tittle, songs)
print ("\n Album created")
print (album_info)
        

# This file is a modified version of the previous one, I made the adjustments following examples from the book. 
