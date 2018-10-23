# Zeus

![](https://img.shields.io/badge/python-2.7-blue.svg)

Automatic detection of security holes

```html
***************************
*  ____  ___  __  _______ *
* /_  / / _ \/ / / / ___/ *
*  / /_/  __/ /_/ (__  )  *
* /___/\___/\__,_/____/   *
***************************
```


## How to work
1. input hostname
2. get the secondary hostname name and ip
3. get the server fingerprint
4. search keyword of fingerprint in holes databases
5. output report(html/xml/email)

## Modules

- Harvest: 信息收集模块，二级域名，子域名以及对应IP等，提供前期的目标 
- WhatWeb: web指纹识别模块，识别目标的指纹信息
- VulSpider: 漏洞爬虫模块，爬虫cve,nvd,cnnvd等各大漏洞资讯站点，持续更新漏洞库
- Fuzzing: 自动攻击模块，利用识别到的指纹与漏洞库进行比对，汇总出存在弱点的目标信息（hostname，ip，服务器应用名称及版本，对应的漏洞编号及poc ）

## User Guide

```git
git clone https://github.com/alvinyeats/Zeus.git
cd Zeus
pip install -r requirements.txt
python Zeus.py -h

```

## todo list
1. hostname collection, doing
2. get ip from hostname
