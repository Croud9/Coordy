# Coordy

GUI приложение для экспорта рельефа из Google Earth и создания csv файла для импорта рельефа в PVsyst
## Стек технологий
- Python
- PyQt5
- BeautifulSoup (Парсинг XML)
  
## Обзор
- **Окно программы**
	> ![5 s](https://github.com/Croud9/Coordy/assets/61747240/795a430e-212a-4149-88cc-19b9f88c5325)
## Функции
### Выгрузка рельефа:
- **In: KML файл с необходимой областью**
	> ![6](https://github.com/Croud9/Coordy/assets/61747240/7d20257c-4588-43bf-92c3-01d1c5d47a13)
- **Out: KML файл с контуром, заполненным точками**
	> ![2](https://github.com/Croud9/Coordy/assets/61747240/10e4cf31-4bb0-42d8-957f-9920b6d75c45)

### Рельеф в PVsyst:
- **In: TXT файл с добавленными высотами с помощью сайта GPSVisualizer.com**
	> ![7](https://github.com/Croud9/Coordy/assets/61747240/63195bac-7b39-4f33-9194-4dc73949dcfd)
- **Out: CSV файл для импорта в PVsyst**
	> ![8](https://github.com/Croud9/Coordy/assets/61747240/813c6a5c-d52f-407b-b59c-8397c38900d0)

### Результат в PVSyst
![3](https://github.com/Croud9/Coordy/assets/61747240/2de991a6-a4d0-4a82-8875-287df85ece7a)
![4](https://github.com/Croud9/Coordy/assets/61747240/7cf8f6f9-7f9e-463d-9670-ba378d5f2410)
