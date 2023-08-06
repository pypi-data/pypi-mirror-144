# Render CTL tool

![Author](https://img.shields.io/static/v1?label=author&message=1058449090@qq.com&color=blue)
![License](https://img.shields.io/github/license/penny1027/renderctl)
[![python](https://img.shields.io/static/v1?label=Python&message=3.8&color=3776AB)](https://www.python.org)
[![PyPI](https://img.shields.io/pypi/v/renderctl.svg)](https://pypi.org/project/renderctl/)

### 安装python依赖
```txt
添加requirements.txt如下所示：
twine
wheel
安装requirements.txt包以将Twine安装到虚拟环境中
pip install -r requirements.txt
```

### 设置环境变量
```bash
export RENDERCTL_VER=1.0.1
vim $HOME/.pypirc
[pypi]
username = ****
password = ****
```

### Build python
```bash
python setup.py sdist bdist_wheel
```

### Upload pypi
```bash
twine upload dist/*
```

### Install
```bash
pip install renderctl
```

#### Usage
- Render yaml templates

```bash
renderctl yaml --config env.yaml --template templates --render render
```