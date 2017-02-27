# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 15:00:14 2016

@author: lantao
"""

def song_playlist(songs, max_size):
    """
    songs: list of tuples, ('song_name', song_len, song_size)
    max_size: float, maximum size of total songs that you can fit

    Start with the song first in the 'songs' list, then pick the next 
    song to be the one with the lowest file size not already picked, repeat

    Returns: a list of a subset of songs fitting in 'max_size' in the order 
             in which they were chosen.
    """
    if songs[0][2] < max_size:
        remaining = max_size - songs[0][2]
        songlist = [songs[0][0]]
        songscopy = sorted(songs[1:], key=lambda song: song[2])
    elif songs[0][2] == max_size:
        return [songs[0][0]]
    else:
        return []
        
    for song in songscopy:
        if song[2] > remaining:
            break
        else:
            remaining -= song[2]
            songlist.append(song[0])
    
    return songlist