import sys, webbrowser
import designCoordy
import styles_and_animation
from bs4 import BeautifulSoup 
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QBrush, QPainter, QPen, QPolygonF
from PyQt5.QtCore import QPointF, Qt, QTimer, QThread
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsPolygonItem

class PointInPolygon(QThread):
    def __init__(self, scene, step, diff_x, diff_y, min_longX, min_latY, x_y_poly):
        super().__init__()
        self.scene = scene
        self.step = step
        self.diff_x = diff_x
        self.diff_y = diff_y
        self.min_longX = min_longX
        self.min_latY = min_latY
        self.x_y_poly = x_y_poly
        

    def run(self):
        step_x = self.diff_x / self.step
        step_y = self.diff_y / self.step
        self.points = []
        self.points_coords = []
        brush = QBrush(Qt.blue)
        pen = QPen(Qt.blue)
        pen.setWidth(2)
        for i in range(self.step + 1):
            for j in range(self.step + 1):
                x_coord = self.min_longX + step_x * i
                y_coord = self.min_latY + step_y * j
                if self.point_in_polygon(self.x_y_poly, x_coord, y_coord) == True:
                    point = f'<Placemark><Point><coordinates>{x_coord},{y_coord}</coordinates></Point></Placemark>'
                    self.points_coords.append(point)
                    ellipse = QGraphicsEllipseItem(x_coord * 100000, y_coord * 100000, 1, 1)
                    ellipse.setBrush(brush)
                    ellipse.setPen(pen)
                    self.points.append(ellipse)

    def point_in_polygon(self, poly, x_coord, y_coord):
        in_polygon = False
        x = x_coord
        y = y_coord
        for i in range(len(poly)):
            xp = float(poly[i].split(',')[0])
            yp = float(poly[i].split(',')[1])
            xp_prev = float(poly[i-1].split(',')[0])
            yp_prev = float(poly[i-1].split(',')[1])
            if (((yp <= y and y < yp_prev) or (yp_prev <= y and y < yp)) and (x > (xp_prev - xp) * (y - yp) / (yp_prev - yp) + xp)):
                in_polygon = not in_polygon
        return in_polygon

class MainApp(QtWidgets.QMainWindow, designCoordy.Ui_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        self.setWindowIcon(QtGui.QIcon('Data/System/5.png'))
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.scene = QGraphicsScene(self)    
        self.btnAddAltitude.clicked.connect(lambda: webbrowser.open('https://www.gpsvisualizer.com/elevation'))
        self.btnMaxStep.clicked.connect(self.set_max_step)
        self.btnMinStep.clicked.connect(self.set_min_step)
        self.btnPolygon.clicked.connect(self.load_kml)
        self.btnTxt.clicked.connect(self.load_txt)
        self.btnSavePointsPolygon.clicked.connect(self.create_kml)
        self.btnSaveCsv.clicked.connect(self.create_csv)
        self.horizontalSlider.sliderReleased.connect(self.points_grid)
        self.movie = QMovie('Data/System/2.gif')
        self.labelLoading.setMovie(self.movie)
        self.draw_points = []
        self.x_y_poly = []
        self.points_coords = []
        self.txt_path = ''
        self._zoom = 0
        self._empty = True
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setResizeAnchor(QGraphicsView.AnchorUnderMouse)
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setDragMode(QGraphicsView.NoDrag)
        self.graphicsView.setFrameShape(QtWidgets.QFrame.NoFrame)

    def hasPhoto(self):
        return not self._empty

    def fitInView(self, scale=True):
        rect = self._photo.boundingRect()
        if not rect.isNull():
            self.graphicsView.setSceneRect(rect)
            if self.hasPhoto():
                unity = self.graphicsView.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
                self.graphicsView.scale(1 / unity.width(), 1 / unity.height())
                viewrect = self.graphicsView.viewport().rect()
                scenerect = self.graphicsView.transform().mapRect(rect)
                factor = min(viewrect.width() / scenerect.width(),
                             viewrect.height() / scenerect.height())
                self.graphicsView.scale(factor, factor)
            self._zoom = 0

    def wheelEvent(self, event):
        if self.hasPhoto():
            # print(self._zoom)
            # print(event.angleDelta().y())
            if event.angleDelta().y() > 0:
                factor = 1.25
                self._zoom += 1
            else:
                factor = 0.8
                self._zoom -= 1
            if self._zoom > 0:
                self.graphicsView.scale(factor, factor)
            elif self._zoom == 0:
                self.fitInView()
            else:
                self._zoom = 0

    def inPolygonFinished(self):
        for p in self.draw_pip.points:
            self.scene.addItem(p)
        self.points_coords = self.draw_pip.points_coords
        self.graphicsView.setScene(self.scene)
        self.horizontalSlider.setEnabled(True)
        styles_and_animation.animation_stop(self.movie, self.labelLoading)
        # self.labelCountPoint.show()
        self.fitInView()
        del self.draw_pip
        
    def load_kml(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл c контуром участка', "Data/", "*.kml")[0] #открытие диалога для выбора файла
        print(path)
        if len(path) != 0:
            self.polygon(path)

    def load_txt(self):
        self.txt_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл выгрузки с сайта', "Data/", "*.txt")[0] #открытие диалога для выбора файла
        print(self.txt_path)
        if len(self.txt_path) != 0:
            self.statusBar.showMessage('Координаты загружены', 4000)
            self.statusBar.setStyleSheet(styles_and_animation.status_green)
            QTimer.singleShot(4000, lambda: self.statusBar.setStyleSheet(styles_and_animation.status_white))
        else:
            self.txt_path = ''

    def set_min_step(self):
        self.horizontalSlider.setValue(5)
        self.points_grid()

    def set_max_step(self):
        self.horizontalSlider.setValue(200)
        self.points_grid()

    def polygon(self, path):
        self.horizontalSlider.setValue(5)
        self.points_coords = []
        self.draw_points = []
        self.x_y_poly = []
        longX_poly = []
        latY_poly = []

        try:
            fd = open(path, 'r') 
            xml_file = fd.read() 
            soup = BeautifulSoup(xml_file, features="xml") 
            for tag in soup.findAll("LineString"): 
                coord_polygon = tag.coordinates.text
                a_poly = coord_polygon.replace('\t', '').replace('\n', ' ').split(' ')
                self.x_y_poly += list(filter(None, a_poly))

            for tag in soup.findAll("LinearRing"): 
                coord_polygon = tag.coordinates.text
                a_poly = coord_polygon.replace('\t', '').replace('\n', ' ').split(' ')
                self.x_y_poly += list(filter(None, a_poly))
            fd.close()
                
            for x in self.x_y_poly:
                x_y = x.split(',')
                longX_poly.append(x_y[0])
                latY_poly.append(x_y[1])
                self.draw_points.append(QPointF(float(x_y[0]) * 100000, float(x_y[1]) * 100000))

            max_longX = float(max(longX_poly))
            max_latY = float(max(latY_poly))
            self.min_longX = float(min(longX_poly))
            self.min_latY = float(min(latY_poly))
            self.diff_x = max_longX - self.min_longX
            self.diff_y = max_latY - self.min_latY

            self.scene.clear()
            pen = QPen(Qt.black)
            pen.setWidth(2)
            self._empty = False
            self.graphicsView.setDragMode(QtWidgets.QGraphicsView.ScrollHandDrag)
            self._photo = QGraphicsPolygonItem(QPolygonF(self.draw_points))
            self._photo.setPen(pen)
            self.scene.addItem(self._photo)
            self.graphicsView.setScene(self.scene)
            self.fitInView()
        except Exception:
            self.statusBar.showMessage('Проблема с KML файлом', 4000)
            self.statusBar.setStyleSheet(styles_and_animation.status_yellow)
            QTimer.singleShot(4000, lambda: self.statusBar.setStyleSheet(styles_and_animation.status_white))
            self.scene.clear()
            self.horizontalSlider.setValue(5)
            self.points_coords = []
            self.draw_points = []
            self.x_y_poly = []
            longX_poly = []
            latY_poly = []

    def points_grid(self):
        if self.draw_points != []:
            self.scene.clear()
            self.points_coords = []
            step = self.horizontalSlider.value()
            pen = QPen(Qt.blue)
            pen.setWidth(2)
            self._photo = QGraphicsPolygonItem(QPolygonF(self.draw_points))
            self._photo.setPen(pen)
            self.scene.addItem(self._photo)
            self.graphicsView.setScene(self.scene)
            self.horizontalSlider.setEnabled(False)
            styles_and_animation.animation_start(self.movie, self.labelLoading)
            self.draw_pip = PointInPolygon(self.scene, step, self.diff_x, self.diff_y, self.min_longX, self.min_latY, self.x_y_poly)
            self.draw_pip.finished.connect(self.inPolygonFinished)
            self.draw_pip.start()
        else:
            self.statusBar.showMessage('Загрузите контур для расстановки на нем точек', 2000)
            self.statusBar.setStyleSheet(styles_and_animation.status_yellow)
            QTimer.singleShot(2000, lambda: self.statusBar.setStyleSheet(styles_and_animation.status_white))

    def create_kml(self):
        if self.x_y_poly != [] and self.points_coords != []:
            polygon = '; '.join(self.x_y_poly)
            points = '; '.join(self.points_coords)
            kml_pattern = f'<?xml version="1.0" encoding="UTF-8"?>\n\
            <kml xmlns="http://www.opengis.net/kml/2.2">\n\
            <Document>\n\
                <name>COORDY</name>\n\
                <Folder>\n\
                    <name>Path and GEN Points</name>\n\
                    <Placemark>\n\
                        <LineString>\n\
                            <coordinates>\n\
                                {polygon}\n\
                            </coordinates>\n\
                        </LineString>\n\
                    </Placemark>\n\
                    {points}\n\
                </Folder>\n\
            </Document>\n\
            </kml>'

            my_file = open("Data/Out/GEN Area and Points.kml", "w+")
            my_file.write(kml_pattern)
            my_file.close()
            self.statusBar.showMessage('Файл KML создан, добавьте высоту и загрузите TXT', 4000)
            self.statusBar.setStyleSheet(styles_and_animation.status_green)
            QTimer.singleShot(4000, lambda: self.statusBar.setStyleSheet(styles_and_animation.status_white))
        elif self.x_y_poly == []:
            self.statusBar.showMessage('Не загружен контур', 4000)
            self.statusBar.setStyleSheet(styles_and_animation.status_yellow)
            QTimer.singleShot(4000, lambda: self.statusBar.setStyleSheet(styles_and_animation.status_white))
        else:
            self.statusBar.showMessage('Нет сетки точек', 4000)
            self.statusBar.setStyleSheet(styles_and_animation.status_yellow)
            QTimer.singleShot(4000, lambda: self.statusBar.setStyleSheet(styles_and_animation.status_white))

    def create_csv(self):
        if self.txt_path != '':
            try:
                with open("Data/Out/GEN Points for PVsyst.csv", "w+") as csv:
                    with open(self.txt_path, "r") as file:
                        for line in file:
                            if not 'type' in line and line != '\n': 
                                all_str = line.split('\t')
                                lat = float(all_str[1]) * -100000 
                                long = float(all_str[2]) * 100000
                                alt = all_str[3]
                                csv.write(f"{lat},{long},{alt}\n")
                self.statusBar.showMessage('Файл CSV создан', 4000)
                self.statusBar.setStyleSheet(styles_and_animation.status_green)
                QTimer.singleShot(4000, lambda: self.statusBar.setStyleSheet(styles_and_animation.status_white))
            except Exception:
                self.statusBar.showMessage('Проблема с TXT файлом', 4000)
                self.statusBar.setStyleSheet(styles_and_animation.status_yellow)
                QTimer.singleShot(4000, lambda: self.statusBar.setStyleSheet(styles_and_animation.status_white))
        else:
            self.statusBar.showMessage('Не загружен файл с координатами', 4000)
            self.statusBar.setStyleSheet(styles_and_animation.status_yellow)
            QTimer.singleShot(4000, lambda: self.statusBar.setStyleSheet(styles_and_animation.status_white))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    window.setFixedSize(600, 580)
    app.exec_()