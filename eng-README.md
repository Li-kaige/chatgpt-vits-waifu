![cover](readme/cyberchat.png)

[中文](README.md "中文") [English](eng-README.md "English") [日本語](jp-README.md "日本語")

<p align="center">
	<img alt="GitHub" src="https://img.shields.io/github/license/cjyaddone/ChatWaifu?color=red">
	<img src="https://img.shields.io/badge/Python-3.7|8|9|10-green" alt="PYTHON" >
  	<a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fcjyaddone%2FChatWaifu?ref=badge_small" alt="FOSSA Status"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fcjyaddone%2FChatWaifu.svg?type=small"/></a>
</p>

#

> ### This is a chatting Waifu program use VITS & ChatGPT!

Effect demonstration on BiliBIli:[《青春猪头少年不会梦见赛博女友》](https://www.bilibili.com/video/BV1rv4y1Q7eT "BiliBili")

**Functioning Now：**
* [x] Talking with ChatGPT
* [x] Convert AI's Response to wav file
* [x] Multi-Character voice generator
* [x] Voice Recognition
* [x] [Connect to Marai Robort](https://github.com/MuBai-He/ChatWaifu-marai)

**Under Construction：**
* [ ] Connect to Live2D

# Catalogue
### This project assumes that you are using chrome explorer
* [1.Install Python venv：](#1.)
	* 1.1 [Enter directory with cd commend](#cd)
	* 1.2 [Create Python Venv:](#99)
	* 1.3 [Enter Python Venv:](#venv)
	* 1.4 [Install required library with Pip:](#pip)
* [2.Import pre-trained models to "model" folder（create a new one if doesn't exist):](#.model)
	* 2.1 [Double click model.exe to import Models](#cd1)
* [3.Run（Talk to your Waifu:](#22)
	* 3.1 [Get ChatGPT Token](#333)
	* 3.2 [Start chatting with CyberWaifu](#444)
* [4.Contributions](#915)
## <span id="1.">1.Install Python Venv：</span>
> **Install Anaconda or Python>=3.7**
> 
> **This example name the venv：chatWaifu**

### <span id="cd">1.1 Enter project directory with cd command</span>
`cd YOUR_PROJECT_RESPORY`
![](readme/5.png)
### <span id="99">1.2 Create Python Venv:</span>

Conda:`conda create --name chatWaifu python=3.10`
![](readme/1.png)
![](readme/2.png)

Python:`python -m venv chatWaifu`
![](readme/6.png)

### <span id="venv">1.3 Activate created venv:</span>
Conda:`conda activate chatWaifu`

![](readme/3.png)

Python:`.\chatWaifu\Scripts\activate.bat`
![](readme/7.png)

### <span id="pip">1.4 Install required library with Pip:</span>
`pip install -r requirements.txt`
![](readme/4.png)

## <span id=".model">2.import pre-trained models to root directory:</span>
Google Drive:https://drive.google.com/file/d/1tMCafhnUoL7FbevVQ44VQi-WznDjt23_/view?usp=sharing

Ali Drive: https://www.aliyundrive.com/s/9JEj1mp1ZRv 提取码: m2y3

### <span id="cd1">2.1Double click model.exe to import Models</span>

## <span id="22">3.RUN（Start chatting with CyberWaifu:</span>
Japanese Ver：`python ChatWaifuJP.py`

Chinese Ver：`python ChatWaifuCN.py`

Japanese voice conversation Ver(use Chinese)：`python ChatWaifuJPVoice.py`

Chinese voice conversation Ver(use Chinese)：`python ChatWaifuCNVoice.py`

Japanese voice conversation Ver(use English)：`python ChatWaifuJPVoiceEN.py`

Japanese voice conversation Ver(use Japanese)：`python ChatWaifuJPVoiceJP.py`


### <span id="333">3.1 Get ChatGPT Token</span>
#### Log in to ChatGPT whith link:https://chat.openai.com
#### Press F12 to enter command center
#### Find Application -> cookie -> __Secure-next-auth.session-token
![](readme/token.png)
#### Copy the value into cmd and press ENTER

### <span id="444">3.2 Start chatting with CyberWaifu</span>

**voice conversation Ver:** Start talking when the console prompts "You:" and then the sentence is recorded and sent to the ChatGPT conversation. 

## <span id="915">4.Contribution：</span>
- [MoeGoe_GUI]https://github.com/CjangCjengh/MoeGoe_GUI
- [Pretrained models]https://github.com/CjangCjengh/TTSModels
- [PyChatGPT]https://github.com/terry3041/pyChatGPT
