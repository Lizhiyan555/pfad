from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtGui import QPainter, QPen, QColor, QPalette, QBrush, QPixmap, QRadialGradient
from PyQt5.QtCore import Qt, QPoint, QTimer
import traceback
from game import Gomoku
from corner_widget import CornerWidget


def run_with_exc(f):
    """When there is an error in the game, use the messagebox to display the error message"""

    def call(window, *args, **kwargs):
        try:
            return f(window, *args, **kwargs)
        except Exception:
            exc_info = traceback.format_exc()
            QMessageBox.about(window, 'Wrong message', exc_info)
    return call


class GomokuWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()  
        self.g = Gomoku()  

        self.last_pos = (-1, -1)
        self.res = 0  
        self.operate_status = 0  

    def init_ui(self):
        """Initialize the game interface"""
        
        self.setObjectName('MainWindow')
        self.setWindowTitle('GoBang')
        self.setFixedSize(650, 650)
        # self.setStyleSheet('#MainWindow{background-color: green}')
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(QPixmap('GomokuCode/imgs/muzm.jpg')))
        self.setPalette(palette)
        
        self.setMouseTracking(True)
        
        self.corner_widget = CornerWidget(self)
        self.corner_widget.repaint()
        self.corner_widget.hide()
       
        self.end_timer = QTimer(self)
        self.end_timer.timeout.connect(self.end_flash)
        self.flash_cnt = 0  
        self.flash_pieces = ((-1, -1), )  
        
        self.show()

    @run_with_exc
    def paintEvent(self, e):
        """Draw game content"""

        def draw_map():
            """Draw the chessboard"""
            qp.setPen(QPen(QColor(0, 0, 0), 2, Qt.SolidLine))  
            
            for x in range(15):
                qp.drawLine(40 * (x + 1), 40, 40 * (x + 1), 600)
            
            for y in range(15):
                qp.drawLine(40, 40 * (y + 1), 600, 40 * (y + 1))
            
            qp.setBrush(QColor(0, 0, 0))
            key_points = [(4, 4), (12, 4), (4, 12), (12, 12), (8, 8)]
            for t in key_points:
                qp.drawEllipse(QPoint(40 * t[0], 40 * t[1]), 5, 5)

        def draw_pieces():
            """Draw the pieces"""
            
            qp.setPen(QPen(QColor(0, 0, 0), 1, Qt.SolidLine))
            # qp.setBrush(QColor(0, 0, 0))
            for x in range(15):
                for y in range(15):
                    if self.g.g_map[x][y] == 1:
                        if self.flash_cnt % 2 == 1 and (x, y) in self.flash_pieces:
                            continue
                        radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)  
                        radial.setColorAt(0, QColor(96, 96, 96))
                        radial.setColorAt(1, QColor(0, 0, 0))
                        qp.setBrush(QBrush(radial))
                        qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)
            
            qp.setPen(QPen(QColor(160, 160, 160), 1, Qt.SolidLine))
            # qp.setBrush(QColor(255, 255, 255))
            for x in range(15):
                for y in range(15):
                    if self.g.g_map[x][y] == 2:
                        if self.flash_cnt % 2 == 1 and (x, y) in self.flash_pieces:
                            continue
                        radial = QRadialGradient(40 * (x + 1), 40 * (y + 1), 15, 40 * x + 35, 40 * y + 35)  
                        radial.setColorAt(0, QColor(255, 255, 255))
                        radial.setColorAt(1, QColor(160, 160, 160))
                        qp.setBrush(QBrush(radial))
                        qp.drawEllipse(QPoint(40 * (x + 1), 40 * (y + 1)), 15, 15)

        if hasattr(self, 'g'):  
            qp = QPainter()
            qp.begin(self)
            draw_map()  
            draw_pieces()  
            qp.end()

    @run_with_exc
    def mouseMoveEvent(self, e):
       
        mouse_x = e.windowPos().x()
        mouse_y = e.windowPos().y()
        if 25 <= mouse_x <= 615 and 25 <= mouse_y <= 615 and (mouse_x % 40 <= 15 or mouse_x % 40 >= 25) and (mouse_y % 40 <= 15 or mouse_y % 40 >= 25):
            game_x = int((mouse_x + 15) // 40) - 1
            game_y = int((mouse_y + 15) // 40) - 1
        else:  
            game_x = -1
            game_y = -1

        
        pos_change = False  
        if game_x != self.last_pos[0] or game_y != self.last_pos[1]:
            pos_change = True
        self.last_pos = (game_x, game_y)
        
        if pos_change and game_x != -1:
            self.setCursor(Qt.PointingHandCursor)
        if pos_change and game_x == -1:
            self.setCursor(Qt.ArrowCursor)
        if pos_change and game_x != -1:
            self.corner_widget.move(25 + game_x * 40, 25 + game_y * 40)
            self.corner_widget.show()
        if pos_change and game_x == -1:
            self.corner_widget.hide()

    @run_with_exc
    def mousePressEvent(self, e):
        """Determine the mouse movements based on the mouse position"""
        if not (hasattr(self, 'operate_status') and self.operate_status == 0):
            return
        if e.button() == Qt.LeftButton:
            
            mouse_x = e.windowPos().x()
            mouse_y = e.windowPos().y()
            if (mouse_x % 40 <= 15 or mouse_x % 40 >= 25) and (mouse_y % 40 <= 15 or mouse_y % 40 >= 25):
                game_x = int((mouse_x + 15) // 40) - 1
                game_y = int((mouse_y + 15) // 40) - 1
            else: 
                return
            self.g.move_1step(True, game_x, game_y)

            
            res, self.flash_pieces = self.g.game_result(show=True)  
            if res != 0:  
                self.repaint(0, 0, 650, 650)
                self.game_restart(res)
                return
            # self.g.ai_move_1step()  
            self.g.ai_play_1step()  
            res, self.flash_pieces = self.g.game_result(show=True)
            if res != 0:
                self.repaint(0, 0, 650, 650)
                self.game_restart(res)
                return
            self.repaint(0, 0, 650, 650)  

    @run_with_exc
    def end_flash(self):

        if self.flash_cnt <= 5:
            
            self.flash_cnt += 1
            self.repaint()
        else:
           
            self.end_timer.stop()
            
            if self.res == 1:
                QMessageBox.about(self, 'End', 'Player win!')
            elif self.res == 2:
                QMessageBox.about(self, 'End', 'Computer win!')
            elif self.res == 3:
                QMessageBox.about(self, 'End', 'A Draw!')
            else:
                raise ValueError('The current game is over' + self.res + '. The end of the game must be marked by 1, 2 or 3')
           
            self.res = 0
            self.operate_status = 0
            self.flash_cnt = 0
            self.g = Gomoku()  
            self.repaint(0, 0, 650, 650)  

    def game_restart(self, res):
        """Begin"""
        self.res = res   
        self.operate_status = 1  
        self.end_timer.start(300)  
