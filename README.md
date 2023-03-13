chatgpt-vits-waifu
==================

项目介绍
----

chatgpt-vits-waifu是一个使用chatgpt的API和vits语音合成，实现与AI老婆的语音聊天的项目。  
该项目在cjyaddone大佬的ChatWaifu项目的基础上进行了改进，主要增加了记忆功能和信息聚合功能，大大提升了对话的容量。  
此外，项目还实现了日语对话中文本自动翻译的功能。

环境安装
----

请参考：[https://github.com/cjyaddone/ChatWaifu](https://github.com/cjyaddone/ChatWaifu)

运行
----
1.  在命令行中切换到该项目所在的根目录
2.  输入以下命令即可运行程序：`python ChatWaifu.py`


注意事项
----
0.  为使用chatgpt api，您需要先进行科学上网（VPN）。
1.  在第一次运行ChatWaifu.py之前，请确保您在ChatWaifu.py中填写了您的OpenAI Key、百度翻译平台API、模型地址等信息。
2.  请将vits语音模型放置在./model目录下，并在ChatWaifu.py中填写您的模型地址和对应配置文件地址。

功能介绍
----

**1.记忆功能**

chatgpt-vits-waifu具有记忆功能，它可以在对话过程中实时记录对话，并在下次运行时继续之前的对话。

**2.信息聚合功能**

当聊天内容数量超出openai限制时，chatgpt-vits-waifu会自动总结前文。  
它会根据前文对话信息，生成一段总结性的文本进行替换，从而减少tokens数量，增大对话容量。

**3.日语自动翻译功能**

chatgpt-vits-waifu可以自动将日语对话翻译成中文。方便您使用vits日语模型。

鸣谢
--

*   [ChatWaifu](https://github.com/cjyaddone/ChatWaifu)：该项目以ChatWaifu为基础，感谢cjyaddone大佬的贡献。

如果您有任何疑问或建议，请随时联系我。邮箱：`Likaige_email@163.com`
