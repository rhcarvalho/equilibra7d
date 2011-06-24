# -*- coding: utf-8 -*-
from panda3d.core import TextNode
from direct.gui.OnscreenText import OnscreenText

from base import Manager


class HUDManager(Manager):
    def __init__(self):
        self._hud = []
    
    def setup(self):
        self.help()
    
    def clear(self):
        """Remove every text from the screen."""
        # We could remove everything from `aspect2d', however
        # it's cleaner to just destroy what we have created.
        #aspect2d.removeChildren()
        while self._hud:
            self._hud.pop().destroy()
    
    def show(self, text, **props):
        """Show text on the screen."""
        self._hud.append(OnscreenText(text=text, **props))
    
    def show_centered(self, text, **kwargs):
        props = dict(
            pos = (0, +0.5),
            scale = 0.26,
            align = TextNode.ACenter,
            shadow = (0, 0, 0, 1),
        )
        props.update(kwargs)
        self.show(text, **props)
    
    def help(self):
        text = """\
Comandos:
     W
    A D - Movimentar jogador
      S
     
    Esc - Sair do jogo
"""
        props = dict(
            pos = (-1.1, -0.55),
            scale = 0.07,
            align = TextNode.ALeft,
            fg = (0.8, 0.8, 0.8, 0.4),
            shadow = (0, 0, 0, 1),
        )
        self.show(text, **props)

    def win(self):
        text = u"Você venceu!"
        self.show_centered(text, fg=(0.3, 1, 0.2, 1))

    def lose(self):
        text = u"Você perdeu!"
        self.show_centered(text, fg=(1, 0.3, 0.2, 1))
    
    def pause(self):
        text = u"Pausado"
        self.show_centered(text, fg=(0.8, 0.8, 0.2, 1))

