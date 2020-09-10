
from PyQt5.QtGui import QPixmapCache, QPixmap, QImage, QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import QRect, QRectF, Qt


class SpriteContainer():

    def __init__(self, spriteconfig, scale=4):
        print("Constructing new SpriteContainer")
        #self.setCacheLimit(2200 * (5 + len(spriteconfig)))
        #print("cacheLimit: " + str(self.cacheLimit()))
        self._scale = scale
        self._scale_limit = 512
        self._renderer = {}
        self._pixmaps = {}
        self._placeholder = QPixmap(
            ["2 2 2 1", "a c #ffffff", "b c #000000", "ab", "ba"])
        self._init_renderer(spriteconfig)
        self._render_sprites()
        print("finished")

    def _init_renderer(self, spriteconfig):
        self._renderer = {x[0]: QSvgRenderer(
            x[1]) for x in spriteconfig.items()}
        self._renderer["$mrk"] = QSvgRenderer("sprites/common/mark.svg")
        self._renderer["$p1b"] = QSvgRenderer("sprites/common/p_1b.svg")
        self._renderer["$p2s"] = QSvgRenderer("sprites/common/p_2s.svg")
        self._renderer["$p2c"] = QSvgRenderer("sprites/common/p_2c.svg")
        self._renderer["$p4e"] = QSvgRenderer("sprites/common/p_1e.svg")


    def _render_sprites(self):
        rect = QRectF(0, 0, self._scale, self._scale)
        for item in self._renderer.items():
            image = QImage(self._scale, self._scale, QImage.Format_ARGB32)
            image.fill(Qt.transparent)
            item[1].render(QPainter(image), rect)
            self._pixmaps[item[0]] = QPixmap.fromImage(image)

    # Probably inefficient use of QPainter, but should not be relevant.
    def update_sprites(self):
        self._render_sprites()
        # rect = QRectF(0, 0, self._scale, self._scale)
        # for item in self._keys.items():
        #     image = QImage(self._scale, self._scale, QImage.Format_ARGB32)
        #     image.fill(Qt.transparent)
        #     self._renderer[item[0]].render(QPainter(image), rect)
        #     self.replace(item[1], QPixmap.fromImage(image))

    def find(self, key):
        return self._pixmaps.get(key, self._placeholder)

    def _check_scale(self):
        if self._scale <= 1:
            self._scale = 1
        elif self._scale > self._scale_limit:
            self._scale = self._scale_limit

    def scale(self, ratio):
        self._scale *= ratio
        self._check_scale()
        self._rect = QRect(0, 0, self._scale, self._scale)
        print("Scale: " + str(self._scale))
        self.update_sprites()

    def get_scale(self):
        return self._scale

    # def get_keys(self):
    #     return self._keys

    def set_scale(self, scale):
        self._scale = scale
        self._check_scale()
        self._rect = QRect(0, 0, scale, scale)
        print("Scale: " + str(self._scale))
        self.update_sprites()
