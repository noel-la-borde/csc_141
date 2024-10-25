# Album 

def make_album(artist_name, album_tittle, num_songs= None):
    
    album= {'Artist': artist_name, ' Album Tittle': album_tittle}
    
    if num_songs:
        album['Number of Songs']= num_songs

    return album
    
album1= make_album ('Drake', 'For the dogs', '15')
album2= make_album ('Kanye West', 'Donda')
album3= make_album ('Bad Bunny','YHLQMDLG', '11')
   
print (album1)
print (album2)
print (album3)

# This one is more complex than the ones I've done so far, I had to test my code using ChatGPT to find the errors in it.  