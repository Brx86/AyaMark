#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   main.py
@Time    :   2022/11/09 11:31:25
@Author  :   Ayatale 
@Version :   1.1
@Contact :   ayatale@qq.com
@Github  :   https://github.com/brx86/
@Desc    :   aya's pastbin api
"""
from fastapi import FastAPI, File, Header, Path, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import (
    FileResponse,
    HTMLResponse,
    JSONResponse,
    RedirectResponse,
    Response,
)
from fastapi.staticfiles import StaticFiles
from pygments.util import ClassNotFound
from starlette.responses import RedirectResponse

from utils import *

app = FastAPI(redoc_url=None)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/f")
def upload(
    c: UploadFile = File(),
    Host: str = Header(),
) -> dict:
    file_id = get_file_id()
    file_list.append(file_id)
    file_path = root / file_id
    try:
        with open(file_path, "wb") as f:
            while contents := c.file.read(1024 * 1024):
                f.write(contents)
    except Exception as e:
        file_list.remove(file_id)
        file_path.unlink(missing_ok=True)
        return {"code": -1, "message": "上传出错了！", "error": repr(e)}
    finally:
        c.file.close()
    return {
        "code": 0,
        "message": f"上传成功！",
        "url": f"http://{Host}/f/{file_id}",
        "short": file_id,
    }


@app.get("/f/{file_name}")
def download(
    file_name: str = Path(min_length=4, max_length=20),
    r: str = "",
) -> Response:
    f_name_suffix = file_name.split(".", 1)
    if (file_id := f_name_suffix[0]) in file_list:
        f = file_name if len(f_name_suffix) == 2 else None
        if r == "html":
            return HTMLResponse((root / file_id).read_text())
        elif r == "mp4":
            return FileResponse(path=(root / file_id), media_type="video/mp4")
        return FileResponse(path=(root / file_id), filename=f)
    else:
        return JSONResponse({"code": -1, "message": "此文件不存在"})


@app.get("/s/{file_id}")
def short_url(file_id: str = Path(min_length=4, max_length=20)) -> Response:
    if file_id in file_list:
        return RedirectResponse((root / file_id).read_text().strip())
    else:
        return JSONResponse({"code": -1, "message": "此短网址不存在"}, status_code=302)


@app.get("/f/{file_id}/{lang}")
def highlight_html(
    file_id: str = Path(min_length=4, max_length=4),
    lang: str = Path(min_length=1, max_length=10),
    style: str = "default",
) -> Response:
    if file_id in file_list:
        try:
            if lang == "info":
                return JSONResponse(show_stats(root / file_id))
            return HTMLResponse(render_html(root / file_id, lang, style))
        except ClassNotFound:
            return JSONResponse({"code": -1, "message": "不支持这种格式"})
    else:
        return JSONResponse({"code": -1, "message": "此文件不存在"})


@app.get("/")
async def index():
    return FileResponse("dist/index.html")


app.mount("/", StaticFiles(directory="dist"))
