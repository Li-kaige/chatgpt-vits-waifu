import openai
import json
import atexit # 用于程序退出时自动保存聊天记录

'''Chatbot1.0'''
class ChatBotV1:
    def __init__(self, api_key, messages):
        self.api_key = api_key
        openai.api_key = self.api_key
        self.messages = messages.copy()
        self.total_tokens = 0

        self.talk()
    def talk(self):
        while True:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                max_tokens=512,
            )
            self.total_tokens = response.usage.total_tokens
            result = ''
            for choice in response.choices:
                result += choice.message.content

            print(f"Bot: {result}")
            self.messages.append({"role": "assistant", "content": result})
            # 打印空行
            print()
            
            user_input = input("User: ")
            if user_input.lower() == 'exit':
                break
            self.messages.append({"role": "user", "content": user_input})

'''Chatbot2.0'''
class ChatBotV2:
    def __init__(self, api_key, save_path, max_tokens=512,auto_save=True,auto_delete=True, model_id=0):
        self.api_key = api_key
        openai.api_key = self.api_key
        self.save_path = save_path
        self.total_tokens = 0
        self.max_tokens = max_tokens # 返回的最大toknes
        self.auto_save = auto_save # 自动保存聊天记录
        self.auto_delete = auto_delete # 自动删除过多的聊天记录
        self.messages = []
        self.settings = {} # 用于保存人物设定
        self.model_id = model_id

        self.load_messages() # 加载聊天记录
        self.settings = self.messages[0] # 读取人物设定

        if  self.auto_save:
            atexit.register(self.save_messages) #程序退出时自动保存聊天记录

        # self.talk() #开始聊天

    def load_messages(self):
        try:
            with open(self.save_path, 'r',encoding='utf-8') as f:
                self.messages = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.messages = []

    def save_messages(self):
        with open(self.save_path, 'w',encoding='utf-8') as f:
            json.dump(self.messages, f, ensure_ascii=False)

    # 裁剪过多的聊天记录
    def trim_messages(self):
        times = 2 # 每次裁剪的次数
        if self.total_tokens > 3500:
            for i in range(times*2):
                self.messages.pop(6)

    # 总结之前的聊天记录
    def summarize_messages(self):
        # self.messages = self.messages[1:]
        # last_words = self.messages.pop(-1)

        self.messages.append({"role": "user", "content": "请帮我总结一下上述对话的内容，实现减少tokens的同时，保证对话的质量。在总结中不要加入这一句话。"})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            max_tokens=self.max_tokens,
        )

        result = response['choices'][0]['message']['content']
        print (f"前情提要: {result}")

        self.messages = []
        self.messages.append(self.settings)

        if self.model_id == 0:
            self.messages.append({"role": "user", "content": "下面我会给你故事的前提提要。"})
            self.messages.append({"role": "assistant", "content": "我明白了，我是伊卡洛斯，一个女性天使。请您输入故事的前提提要。"})
            self.messages.append({"role": "user", "content": result})
            self.messages.append({"role": "assistant", "content": "好的，我已经记住了。让我们继续角色扮演吧。"})
        elif self.model_id == 1:
            self.messages.append({"role": "user", "content": "下面我会给你故事的前提提要。"})
            self.messages.append({"role": "assistant", "content": "わかりました、私は女天使のイカロスです。 話の前提に入ってください。"})
            self.messages.append({"role": "user", "content": result})
            self.messages.append({"role": "assistant", "content": "わかりました、覚えました。 ロールプレイングに移りましょう。"})

        # self.messages.append(last_words)


    def talk(self):
        while True:
            if self.total_tokens > 4000:
                self.summarize_messages() # 总结之前的聊天记录

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.messages,
                max_tokens=self.max_tokens,
            )

            self.total_tokens = response['usage']['total_tokens']
            result = response['choices'][0]['message']['content']
            # 打印机器人的回答和total_tokens
            print(f"Bot: {result}")
            print(f"Total tokens used: {self.total_tokens}")
            print()

            user_input = input("User: ")

            self.messages.append({"role": "assistant", "content": result})
            self.messages.append({"role": "user", "content": user_input})
            
            if self.auto_save:
                self.save_messages() #保存聊天记录    
    
    def send_message(self,input_message):
        if self.total_tokens > 4000:
            self.summarize_messages() # 总结之前的聊天记录

        self.messages.append({"role": "user", "content": input_message})

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            max_tokens=self.max_tokens,
        )

        self.total_tokens = response['usage']['total_tokens']
        result = response['choices'][0]['message']['content']
        # 打印机器人的回答和total_tokens


        self.messages.append({"role": "assistant", "content": result})
        
        if self.auto_save:
            self.save_messages() #保存聊天记录    

        return result
