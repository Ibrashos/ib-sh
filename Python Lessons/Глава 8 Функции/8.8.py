# def make_album(author, album):
# 	return {'Author': author, 'Album': album}

# while True:
# 	au_name = input("Введите 'q' для выхода\nВведите имя автора: ")
# 	if au_name == 'q':
# 		break
# 	print(f"{make_album(au_name.title(), input('Введите название альбома: ').title())}")

# 	

def make_album(author, album):
	if album == 'q':
		raise SystemExit(1)
	full_album = {'Author': author.title(), 'Album': album.title()}
	return full_album
while True:
	author_name = input("Введите 'q' для выхода\nВведите имя автора: ")
	if author_name == 'q':
		break
	print(make_album(author_name, input('Введите название альбома: ')))



