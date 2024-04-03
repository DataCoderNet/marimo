# Copyright 2024 Marimo. All rights reserved.
"""The marimo library.

marimo is a Python library for making reactive notebooks that double as apps.

marimo is designed to be:

    1. simple
    2. immersive
    3. interactive
    4. seamless
    5. fun
"""

__all__ = [
    "App",
    "Cell",
    "MarimoStopError",
    "create_asgi_app",
    "accordion",
    "carousel",
    "as_html",
    "audio",
    "callout",
    "capture_stdout",
    "capture_stderr",
    "center",
    "defs",
    "query_params",
    "doc",
    "download",
    "hstack",
    "Html",
    "icon",
    "image",
    "lazy",
    "left",
    "md",
    "mermaid",
    "mpl",
    "output",
    "plain_text",
    "pdf",
    "redirect_stderr",
    "redirect_stdout",
    "refs",
    "right",
    "stat",
    "state",
    "status",
    "stop",
    "style",
    "tabs",
    "tree",
    "ui",
    "video",
    "vstack",
]
__version__ = "0.3.8"

from marimo._ast.app import App
from marimo._ast.cell import Cell
from marimo._output.doc import doc
from marimo._output.formatting import as_html
from marimo._output.hypertext import Html
from marimo._output.justify import center, left, right
from marimo._output.md import md
from marimo._plugins import ui
from marimo._plugins.stateless import mpl, status
from marimo._plugins.stateless.accordion import accordion
from marimo._plugins.stateless.audio import audio
from marimo._plugins.stateless.callout import callout
from marimo._plugins.stateless.carousel import carousel
from marimo._plugins.stateless.download import download
from marimo._plugins.stateless.flex import hstack, vstack
from marimo._plugins.stateless.icon import icon
from marimo._plugins.stateless.image import image
from marimo._plugins.stateless.lazy import lazy
from marimo._plugins.stateless.mermaid import mermaid
from marimo._plugins.stateless.pdf import pdf
from marimo._plugins.stateless.plain_text import plain_text
from marimo._plugins.stateless.stat import stat
from marimo._plugins.stateless.style import style
from marimo._plugins.stateless.tabs import tabs
from marimo._plugins.stateless.tree import tree
from marimo._plugins.stateless.video import video
from marimo._runtime import output
from marimo._runtime.capture import (
    capture_stderr,
    capture_stdout,
    redirect_stderr,
    redirect_stdout,
)
from marimo._runtime.control_flow import MarimoStopError, stop
from marimo._runtime.runtime import defs, query_params, refs
from marimo._runtime.state import state
from marimo._server.asgi import create_asgi_app
