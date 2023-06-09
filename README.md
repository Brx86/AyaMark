# AyaMark 在线剪贴板

Github: [https://github.com/Brx86/AyaMark](https://github.com/Brx86/AyaMark)

Demo: [https://mark.aya1.pro](https://mark.aya1.pro)

![图片1](https://user-images.githubusercontent.com/44391900/232374306-9466dca7-1378-4336-a5aa-22d8ee98f27e.png)

![图片2](https://user-images.githubusercontent.com/44391900/232374248-08ca962a-cb52-4934-a497-c034ec37b7e7.png)

## 使用方法：

### 〇 打开网页，输入文本，点击 Render 预览 Markdown，点击左上角按钮发布文档

### 〇 请求 api ，可以在命令行使用 curl 上传

示例：

```bash
- 上传uname命令的标准输出
❯ uname -a | curl -sF "c=@-" "https://mark.aya1.pro/f"

- 上传文件main.py
❯ curl -sF "c=@-" "https://mark.aya1.pro/f" < main.py

- 上传图片 ~/Pictures/aya4.jpg
❯ curl -sF "c=@-" "https://mark.aya1.pro/f" < ~/Pictures/aya4.jpg

```

返回值示例:

```json
{
  "code": 0,
  "message": "上传成功！",
  "url": "https://mark.aya1.pro/f/ZuMj",
  "short": "ZuMj"
}
```

## 小技巧：

### 〇 在剪贴板地址后加 `/info`，可以查询文件信息（大小和创建时间）

如：https://mark.aya1.pro/f/main/info

### 〇 在剪贴板地址后加 `.文件后缀`，可以下载对应后缀的文件

如：https://mark.aya1.pro/f/main.py

### 〇 在剪贴板地址后加 `/文件后缀`，可以高亮显示

如：https://mark.aya1.pro/f/main/py

使用参数 `style=xxx` 可以更换指定主题
如：https://mark.aya1.pro/f/main/py?style=nord-darker

可用主题：main
default emacs friendly friendly_grayscale colorful autumn murphy manni material monokai perldoc pastie borland trac native fruity bw vim vs tango rrt xcode igor paraiso-light paraiso-dark lovelace algol algol_nu arduino rainbow_dash abap solarized-dark solarized-light sas staroffice stata stata-light stata-dark inkpot zenburn gruvbox-dark gruvbox-light dracula one-dark lilypond nord nord-darker github-dark

### 〇 把上传的请求写进shell配置文件，方便以后使用

如 `.zshrc` 里可以这样写：

```bash
# 简单alias
alias clip='curl -sF "c=@-" "https://mark.aya1.pro/f"'
# 写成函数，直接使用jq解析返回url并输出
clip2(){curl -sF "c=@-" "https://mark.aya1.pro/f"|jq -r ".url"}
```

使用时：

```bash
fcitx5-diagnose | clip2
clip2 < /etc/pacman.conf
```
