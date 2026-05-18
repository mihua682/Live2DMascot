# 本地 OpenAI 兼容 API 使用指南

本项目现已支持本地 OpenAI 兼容的 AI 服务，包括 Ollama、LM Studio、LocalAI 等。

## 🚀 快速开始

### 1. 选择并安装本地 AI 服务

#### 选项 A: Ollama（推荐）
- **官网**: https://ollama.com/
- **特点**: 简单易用，支持多种开源模型
- **安装**:
  ```bash
  # Windows
  # 从官网下载安装程序
  
  # 下载模型
  ollama pull qwen2.5:7b
  ```

#### 选项 B: LM Studio
- **官网**: https://lmstudio.ai/
- **特点**: 图形界面，易于管理模型
- **安装**: 从官网下载并安装

#### 选项 C: LocalAI
- **官网**: https://localai.io/
- **特点**: 功能强大，支持更多自定义选项

### 2. 配置项目

编辑 `framework/runtime/drive/kizuna/local_openai_config.py`:

```python
# Ollama 配置示例
BASE_URL = "http://localhost:11434/v1"
MODEL = "qwen2.5:7b"  # 或 llama3.2:3b, mistral:7b 等
API_KEY = ""  # 留空

# LM Studio 配置示例
BASE_URL = "http://localhost:1234/v1"
MODEL = "你的模型名称"
API_KEY = ""

# LocalAI 配置示例
BASE_URL = "http://localhost:8080/v1"
MODEL = "模型名称"
API_KEY = ""
```

### 3. 启用本地 AI

编辑 `framework/runtime/drive/kizuna/kizuna_impl.py`:

```python
# 设置为 True 使用本地 OpenAI
self.USE_LOCAL_OPENAI = True

# 设置为 False 使用百度千帆
self.USE_LOCAL_OPENAI = False
```

### 4. 测试连接

运行测试脚本：
```bash
python test_local_openai.py
```

如果看到成功消息，说明配置正确！

### 5. 启动应用

```bash
python main.py
```

## 📋 支持的模型

### Ollama 推荐模型
- **qwen2.5:7b** - 通义千问，中文支持好
- **llama3.2:3b** - Meta Llama，轻量级
- **mistral:7b** - Mistral AI，性能优秀
- **gemma2:9b** - Google Gemma，高质量

查看可用模型：https://ollama.com/library

### LM Studio
可以从 HuggingFace 下载各种 GGUF 格式的模型

## 🔧 常见问题

### Q: 连接失败怎么办？
A: 
1. 确认本地 AI 服务已启动
2. 检查 BASE_URL 是否正确
3. 确认端口未被防火墙阻止
4. 运行 `test_local_openai.py` 诊断问题

### Q: 响应很慢怎么办？
A:
1. 使用更小的模型（如 3B 参数）
2. 确保有足够的 RAM（至少 8GB）
3. 如果有 GPU，启用 GPU 加速

### Q: 如何切换回百度千帆？
A:
在 `kizuna_impl.py` 中设置：
```python
self.USE_LOCAL_OPENAI = False
```

### Q: 需要 API Key 吗？
A:
本地服务通常不需要 API Key，保持为空即可。

## 💡 优势

✅ **完全免费** - 无需付费 API
✅ **隐私保护** - 数据在本地处理
✅ **离线可用** - 不需要网络连接
✅ **高度可定制** - 可选择任意开源模型
✅ **无调用限制** - 想聊多久就聊多久

## ⚠️ 注意事项

- 本地模型需要一定的硬件资源（建议 8GB+ RAM）
- 首次运行可能需要下载模型文件
- 响应速度取决于模型大小和硬件性能
- 某些小模型的对话质量可能不如大型云端模型

## 📞 需要帮助？

如果遇到问题，请检查：
1. 本地 AI 服务日志
2. 项目控制台输出
3. 运行测试脚本的诊断信息

祝您使用愉快！🎉
