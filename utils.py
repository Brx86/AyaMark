import os
from pathlib import Path as Path_
from random import choice
from string import ascii_letters
from time import gmtime, strftime

from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name

root = Path_(__file__).parent / "files"
if not root.is_dir():
    root.mkdir()
file_list = os.listdir(root)


def get_file_id() -> str:
    while (file_id := "".join([choice(ascii_letters) for _ in range(4)])) in file_list:
        pass
    return file_id


def format_size(size: float) -> str:
    size_text = ("B", "KB", "MB", "GB")
    index = (len(str(size)) - 1) // 3
    return f"{size/(1024**(index)):.1f}{size_text[index]}"


def show_stats(path: Path_) -> dict:
    stat = path.stat()
    ftime_8 = strftime("%Y-%m-%d %H:%M:%S", gmtime(stat.st_mtime + 28800))
    return {
        "size": (stat.st_size, format_size(stat.st_size)),
        "mtime": (stat.st_mtime, ftime_8),
    }


def render_html(path: Path_, lang: str, style: str) -> str:
    if path.stat().st_size > 1000000:
        return "文本超过1M，不再渲染"
    with open(path, "r") as f:
        code = f.read()
    lexer = get_lexer_by_name(lang)
    formatter = HtmlFormatter(linenos=True, style=style)
    css = (
        formatter.get_style_defs(".highlight")
        + "pre {padding: 6px;font-size: 14px;line-height: 1.5;}"
    )
    return f'<style type="text/css">{css}</style>{highlight(code, lexer, formatter)}'
