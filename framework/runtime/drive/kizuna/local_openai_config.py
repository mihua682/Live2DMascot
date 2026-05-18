# 本地 OpenAI 兼容 API 配置
# 支持 Ollama、LM Studio、LocalAI 等本地模型服务

# API 基础 URL
# Ollama: http://localhost:11434/v1
# LM Studio: http://localhost:1234/v1
# LocalAI: http://localhost:8080/v1
BASE_URL = "http://localhost:8080/v1"

# 模型名称
# Ollama 示例: qwen2.5:7b, llama3.2:3b, mistral:7b
# LM Studio: 使用加载的模型名称
MODEL = "qwen2.5:7b"

# API Key（本地服务通常不需要，留空即可）
API_KEY = ""
