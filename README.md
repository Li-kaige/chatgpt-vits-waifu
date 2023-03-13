chatgpt-vits-waifu
==================

项目介绍
----

chatgpt-vits-waifu是一个使用chatgpt的API和vits语音合成，实现与AI老婆的语音聊天的项目。该项目在cjyaddone大佬的ChatWaifu项目的基础上进行了改进，主要增加了记忆功能和信息聚合功能，大大提升了对话的容量。此外，项目还实现了日语对话中文本自动翻译的功能。

环境安装
----

请参考：[https://github.com/cjyaddone/ChatWaifu](https://github.com/cjyaddone/ChatWaifu)

运行
--

在命令行中输入以下命令即可运行程序：

`python ChatWaifu.py`

注意事项
----

1.  第一次运行需要在ChatWaifu.py中填入你的OpenAI Key、百度翻译平台API、模型地址等信息。
2.  vits语音模型请放在./model目录下，并在ChatWaifu.py中填入你的模型地址和对应配置文件地址。

鸣谢
--

*   [ChatWaifu](https://github.com/cjyaddone/ChatWaifu)：该项目为chatgpt-vits-waifu的基础，感谢cjyaddone大佬的贡献。
