def make_album(author, album):
	return {'Author': author, 'Album': album}

while True:
	au_name = input("Введите 'q' для выхода\nВведите имя автора: ")
	if au_name == 'q':
		break
	print(f"{make_album(au_name.title(), input('Введите название альбома: ').title())}")