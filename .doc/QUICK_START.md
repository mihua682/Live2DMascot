# 快速开始 - 使用本地 AI 聊天

## 🚀 5分钟快速配置（使用 Ollama）

### 步骤 1: 安装 Ollama

1. 访问 https://ollama.com/
2. 下载并安装 Windows 版本
3. 安装完成后，Ollama 会自动在后台运行

### 步骤 2: 下载模型

打开命令提示符或 PowerShell，运行：

```bash
# 下载通义千问模型（推荐，中文支持好）
ollama pull qwen2.5:7b

# 或者下载其他模型：
# ollama pull llama3.2:3b    # 轻量级
# ollama pull mistral:7b     # 性能优秀
```

等待下载完成（模型大小约 4-5GB）。

### 步骤 3: 配置项目

编辑文件：`framework/runtime/drive/kizuna/local_openai_config.py`

确保配置如下：

```python
BASE_URL = "http://localhost:11434/v1"
MODEL = "qwen2.5:7b"
API_KEY = ""
```

### 步骤 4: 启用本地 AI

编辑文件：`framework/runtime/drive/kizuna/kizuna_impl.py`

找到第 30 行左右，确保：

```python
self.USE_LOCAL_OPENAI = True  # 设置为 True
```

### 步骤 5: 测试连接

在项目根目录运行：

```bash
python test_local_openai.py
```

如果看到类似输出，说明配置成功：

```
✓ LocalOpenAI 初始化成功
✓ 聊天 API 测试成功
回复:
你好！我是...
```

### 步骤 6: 启动应用

```bash
python main.py
```

现在你可以和 Live2D 角色聊天了！🎉

---

## 💡 常见问题

### Q: 下载模型很慢怎么办？
A: 可以使用国内镜像或选择更小的模型（如 llama3.2:3b）

### Q: 内存不足怎么办？
A: 
- 使用更小的模型（3B 参数）
- 关闭其他占用内存的程序
- 至少需要 8GB RAM

### Q: 响应速度慢？
A:
- 使用较小的模型
- 如果有 GPU，Ollama 会自动使用
- 首次加载会较慢，后续会快一些

### Q: 想换回百度千帆？
A: 在 `kizuna_impl.py` 中设置 `USE_LOCAL_OPENAI = False`

---

## 🎯 其他本地 AI 服务

### LM Studio（图形界面，更易用）

1. 下载：https://lmstudio.ai/
2. 安装并启动
3. 下载并加载一个模型
4. 配置：
   ```python
   BASE_URL = "http://localhost:1234/v1"
   MODEL = "你的模型名称"
   ```

### LocalAI（高级用户）

1. 参考：https://localai.io/
2. 配置：
   ```python
   BASE_URL = "http://localhost:8080/v1"
   MODEL = "模型名称"
   ```

---

## ✨ 优势

✅ **完全免费** - 无需付费
✅ **隐私保护** - 数据不离本地
✅ **离线可用** - 不需要网络
✅ **无限调用** - 想聊多久就多久
✅ **高度定制** - 可选择任意开源模型

---

详细文档请查看：[LOCAL_OPENAI_GUIDE.md](./LOCAL_OPENAI_GUIDE.md)
