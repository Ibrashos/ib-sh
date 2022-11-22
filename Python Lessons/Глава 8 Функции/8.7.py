def make_album(author, album, tracks=None):
	info_album = {'Author': author, 'Album': album}
	
	if tracks:
		info_album['tracks'] = tracks
	
	return info_album

print(make_album('Leonardo', 'Ada'))
print(make_album('Ds.Return', '.exe', tracks=12))
print(make_album('Urnazz', 'Lolypop'))