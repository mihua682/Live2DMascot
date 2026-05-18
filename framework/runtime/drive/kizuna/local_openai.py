import json
import os.path
import time

import requests


class LocalOpenAI:
    """
    本地 OpenAI 兼容 API 客户端
    支持 Ollama、LM Studio、LocalAI 等本地模型服务
    """
    
    KEY_SRC = "role"
    KEY_CONTENT = "content"
    
    # 默认配置 - 可以根据实际情况修改
    DEFAULT_BASE_URL = "http://localhost:11434/v1"  # Ollama 默认地址
    DEFAULT_MODEL = "qwen2.5:7b"  # 默认模型
    
    VALUE_USER = "user"
    VALUE_ASSISTANT = "assistant"

    def __init__(self, base_url=None, model=None, api_key=None):
        """
        初始化本地 OpenAI 客户端
        
        Args:
            base_url: API 基础 URL，例如 http://localhost:11434/v1
            model: 模型名称，例如 qwen2.5:7b, llama3.2:3b 等
            api_key: API Key（本地服务通常不需要）
        """
        self.base_url = base_url or self.DEFAULT_BASE_URL
        self.model = model or self.DEFAULT_MODEL
        self.api_key = api_key
        self.chat_endpoint = f"{self.base_url}/chat/completions"
        
    def chat(self, messages):
        """
        发送聊天请求
        
        Args:
            messages: 消息列表，格式为 [{"role": "user", "content": "你好"}]
            
        Returns:
            AI 回复的文本内容
        """
        try:
            return self.__openai_api(messages)
        except Exception as e:
            error_msg = f"Chat API error: {str(e)}"
            print(error_msg)
            return error_msg

    def __openai_api(self, messages):
        """
        调用 OpenAI 兼容的聊天 API
        
        Args:
            messages: 消息列表
            
        Returns:
            AI 回复的文本
        """
        payload = {
            "model": self.model,
            "messages": messages,
            "temperature": 0.95,
            "top_p": 0.7,
            "stream": False
        }
        
        headers = {
            "Content-Type": "application/json"
        }
        
        # 如果提供了 API Key，添加到请求头
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        response = requests.post(
            self.chat_endpoint, 
            headers=headers, 
            json=payload,
            timeout=60
        )
        
        # 检查响应状态
        response.raise_for_status()
        
        # 解析响应
        result = response.json()
        
        # OpenAI 格式的响应
        if 'choices' in result and len(result['choices']) > 0:
            return result['choices'][0]['message']['content']
        
        # 其他可能的响应格式
        return str(result)
