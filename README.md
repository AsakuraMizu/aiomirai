# Async Mirai SDK for Python

[![License](https://img.shields.io/github/license/water-lift/aiomirai.svg)](LICENSE)
[![PyPI](https://img.shields.io/pypi/v/aiomirai.svg)](https://pypi.python.org/pypi/aiomirai)

Async Mirai SDK for Python is a Python SDK with async I/O for [Mirai](https://github.com/mamoe/mirai)'s [Mirai API HTTP](https://github.com/mamoe/mirai-api-http) plugin.

Inspired by [CQHTTP Python Async SDK](https://github.com/cqmoe/python-aiocqhttp) and [Mirai Framework for Python](https://github.com/NatriumLab/python-mirai).

## Installation

```bash
pip install aiomirai
```

## Documentation

See at [https://aiomirai.solariar.tech](https://aiomirai.solariar.tech)

## 鸣谢

> 这些项目也很棒, 去他们的项目页看看, 点个 `Star` 以鼓励他们的开发工作, 毕竟没有他们也没有 `aiomirai`.

特别感谢 [`mamoe`](https://github.com/mamoe) 给我们带来这些精彩的项目:
 - [`mirai`](https://github.com/mamoe/mirai): 即 `mirai-core`, 一个高性能, 高可扩展性的 QQ 协议库, 同时也是个很棒的机器人开发框架!
 - [`mirai-console`](https://github.com/mamoe/mirai-console): 一个基于 `mirai` 开发的插件式可扩展开发平台, 我们的大多数开发工作基本上都在该项目上完成, 不得不称赞其带来的开发敏捷性.
 - [`mirai-api-http`](https://github.com/mamoe/mirai-api-http): 为该项目提供 `http` 接口的 `mirai-console` 插件, 万物之源

特别感谢 [`NatriumLab`](https://github.com/NatriumLab) 给我们带来这些精彩的项目:
  - [`python-mirai`](https://github.com/NatriumLab/python-mirai)：一个以 OICQ(QQ) 协议驱动的高性能机器人开发框架 Mirai 的 Python 接口，本项目的灵感来源，参考了部分内容~~比如这个鸣谢~~

特别感谢 [`CQMOE`](https://github.com/cqmoe) 给我们带来这些精彩的项目:
  - [`python-aiocqhttp`](https://github.com/cqmoe/python-aiocqhttp/)：酷Q 的 CQHTTP 插件 的 Python SDK 异步版本，本项目的主要代码及逻辑都在一定程度上参考了该项目

特别感谢 [`Koishi.js`](https://github.com/koishijs) 给我们带来这些精彩的项目：
  - [`koishijs.github.io`](https://github.com/koishijs/koishijs.github.io)：本项目文档的部分内容使用了该项目中的 vue 组件

And finally...

```
Long Live Mirai
                 `-://+++//:-.                              
               -+o+o++oo+o+++////:-.`                       
           ``-o+/:+o:+++//++s+++/////:`                     
         `--/++//+os://+/::+o+::/:/--::.                    
         :://o/:-:o+:/`./-:+-.//:/://`:/:-.`                
        -+/+:o/--:/--:.`.:-.-+o/+o++:- +-`:/:-              
       ./::o:o+/+::.ohy:````-ss+/os+:`.-:` .--              
    ```.-/`+:++:/o/+++:.``````.`-o/:. -` ...```             
      `- -:/-`///+o+:````...-.`.:+/.``                      
     .-. ``:. ...::::--....``.-----..:.                     
     .:-.-    `....`----.-...-.---:.`--.`                   
  `..--::.    -.```...-:  `.--`-..-`-`-`..`                 
  ..:--...   `.--     `.-```.-  `..`. .....`                
   ....``-  `-...-      :-  `.`  `..`  -`-..`               
   `.:``./...`.```..``..//  `..   ..-.```.-```              
 `-:-:...-...``.`.````..//` ````  ../:    .`.``             
 ......     +:.```.   . //` `.`.  .://    ````.`            
  ....``  `.shy+.`.  `.`-/: `-`.. `+/-    -````.            
   .```.````/os/../  `---//` :``-  //.   `-`.```.`          
   .`````````..`..-` -+oo+/- .``.. :/.  ```..````-:`        
   .``.```````-.-`:  .-::-// .`.`-`./.    -:-.```-/.`       
   `.`.``````./-`/+`   `  -/``.:--.`/-  ./+..-```:/``-      
    `-.`````.` ``:++:   ` -/. `.`.. /:  .- `  ..-/-``.-.`   
     `.....`  ``  `-/`    ./-  .:- `:/`    .   --.```.....` 
              `            `   ` `  ``                      
          ``.`   ````  ``                 ``                
          /++/` `+++:  -.     ``   ```    `.                
          /+-+/ :/-+: `+/  -:...`.-.`.--  -:`               
          /+..+/+-.+: `+/  -:    .-..`-:` -:`               
          -/` -/- `/- `/:  --    .-....-` .-`               
```