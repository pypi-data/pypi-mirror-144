#! /usr/bin/python3
# -*- coding: utf-8 -*-

##############################################################################
# Copyright 2020 AlexPDev
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
##############################################################################
"""Magnet Widget containing Testing creation of Magnet URIs."""

import os
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QFileDialog, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QSpacerItem, QToolButton,
                               QVBoxLayout, QWidget)
from torrentfile import magnet


class MagnetWidget(QWidget):
    """Tab for creating magnet URL's and downloading torrentfiles from them."""

    def __init__(self, parent=None):
        """Initialize the widget form for creating magnet URI's from a metafile."""
        super().__init__(parent=parent)
        self.window = parent.window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.hlayout = QHBoxLayout()
        self.top_spacer = QSpacerItem(0, 50)
        self.bottom_spacer = QSpacerItem(0, 400)
        self.metafile_label = QLabel("Metafile", parent=self)
        self.metafile_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.metafile_input = QLineEdit(parent=self)
        self.output = QLineEdit(parent=self)
        self.file_button = MetafileButton(parent=self)
        self.submit_button = SubmitButton(parent=self)
        self.hlayout.addWidget(self.metafile_input)
        self.hlayout.addWidget(self.file_button)
        self.layout.addSpacerItem(self.top_spacer)
        self.layout.addWidget(self.metafile_label)
        self.layout.addLayout(self.hlayout)
        self.layout.addWidget(self.output)
        self.layout.addWidget(self.submit_button)
        self.layout.addSpacerItem(self.bottom_spacer)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        """Accept incoming drag events for magnet tab."""
        self.current_path = event.mimeData().data("text/plain")
        event.accept()
        return True

    def dropEvent(self, event):
        """Accept drop events for magnet tab."""
        text = event.mimeData().text()
        if text.startswith("file:///"):
            text = text[8:]
            self.metafile_input.setText(text)
            self.submit_button.click()
            return True
        return False


class SubmitButton(QPushButton):
    """Submit current information to be processed into a megnet URI."""

    def __init__(self, parent=None):
        """Initialize the button for magnet creation."""
        super().__init__(parent=parent)
        self.widget = parent
        self.window = parent.window
        self.setText("Create Magnet")
        self.clicked.connect(self.magnet)

    def magnet(self):
        """Create a magnet URI from information contained in form."""
        fd = self.widget.metafile_input.text()
        if os.path.exists(fd):
            uri = magnet(fd)
            self.widget.output.setText(uri)


class MetafileButton(QToolButton):
    """
    Find a .torrent file in native file browser button actions.

    Perameters
    ----------
    parent : `QWidget`
        This widgets parent.
    """

    def __init__(self, parent=None):
        """Initialize the metafile button."""
        super().__init__(parent=parent)
        self.window = parent.window
        self.widget = parent
        self.setText("...")
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.pressed.connect(self.select_metafile)

    def select_metafile(self, filename=None):
        """Find metafile in file browser."""
        if not filename:   # pragma: nocover
            filename, _ = QFileDialog.getOpenFileName(
                parent=self,
                caption="Select '.torrent' file",
                dir=str(Path.home()),
                filter="*.torrent",
                selectedFilter=None,
            )
        self.widget.metafile_input.setText(filename)
