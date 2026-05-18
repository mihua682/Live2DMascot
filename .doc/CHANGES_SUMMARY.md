# 本地 OpenAI 支持 - 改造总结

## 📝 改动概览

本次改造为项目添加了本地 OpenAI 兼容 API 的支持，同时保留了原有的百度千帆接口。用户可以根据需要自由切换。

## 🆕 新增文件

### 核心文件
1. **`framework/runtime/drive/kizuna/local_openai.py`**
   - 本地 OpenAI 兼容 API 客户端实现
   - 支持 Ollama、LM Studio、LocalAI 等服务
   - 提供标准的 `chat()` 方法接口

2. **`framework/runtime/drive/kizuna/local_openai_config.py`**
   - 本地 OpenAI 配置文件
   - 包含 BASE_URL、MODEL、API_KEY 配置项

### 示例文件
3. **`framework/runtime/drive/kizuna/local_openai_config.py.ollama.example`**
   - Ollama 配置示例

4. **`framework/runtime/drive/kizuna/local_openai_config.py.lmstudio.example`**
   - LM Studio 配置示例

### 测试文件
5. **`test_local_openai.py`**
   - 本地 OpenAI 连接测试脚本
   - 用于诊断配置问题

6. **`test_all_models.py`**
   - 百度千帆多模型端点测试脚本

7. **`test_qianfan_api.py`**
   - 百度千帆 API 基础测试脚本

### 文档文件
8. **`LOCAL_OPENAI_GUIDE.md`**
   - 详细的使用指南
   - 包含安装、配置、常见问题等

9. **`CHANGES_SUMMARY.md`** (本文件)
   - 改造总结文档

## 🔧 修改文件

### 1. `framework/runtime/drive/kizuna/kizuna_impl.py`

**新增导入：**
```python
from framework.runtime.drive.kizuna.local_openai import LocalOpenAI
from framework.runtime.drive.kizuna import local_openai_config
```

**新增属性：**
```python
self.local_openai: LocalOpenAI | None = None
self.USE_LOCAL_OPENAI = True  # 配置开关
```

**修改 `doInitialize()` 方法：**
- 根据 `USE_LOCAL_OPENAI` 配置初始化不同的 AI 服务
- 支持动态切换本地 OpenAI 和百度千帆

**修改 `doReaction()` 方法：**
- 根据配置调用不同的 AI 服务
- 保持接口一致性

### 2. `framework/runtime/drive/kizuna/qianfan.py`

**优化错误处理：**
- 添加 `expires_in` 默认值，防止 None 类型错误
- 增强错误信息输出，便于调试
- 改进 API 响应解析

**调整 API 端点：**
- 更新为正确的百度千帆模型端点格式

### 3. `framework/runtime/drive/window/gal_dialog_qt.py`

**修复字体问题：**
- 添加字体大小验证，确保大于 0
- 防止 QFont 初始化错误

### 4. `Resources/v3/Haru/Haru.model3.json`

**修复动作配置：**
- 替换空的 TapBody 动作条目
- 使用有效的 motion 文件

### 5. `README.md`

**更新文档：**
- 添加 AI 聊天接口支持说明
- 链接到详细使用指南

## ✨ 主要特性

### 1. 双 API 支持
- ✅ 本地 OpenAI 兼容 API（Ollama/LM Studio/LocalAI）
- ✅ 百度千帆大模型 API
- ✅ 一键切换，无需修改代码逻辑

### 2. 易于配置
- 独立的配置文件
- 提供多个示例文件
- 详细的文档说明

### 3. 完善的测试
- 连接测试脚本
- 诊断工具
- 清晰的错误提示

### 4. 向后兼容
- 保留原有百度千帆功能
- 不影响现有代码结构
- 平滑过渡

## 🎯 使用方法

### 切换到本地 OpenAI

1. 安装本地 AI 服务（如 Ollama）
2. 编辑 `local_openai_config.py` 配置服务地址和模型
3. 在 `kizuna_impl.py` 中设置 `USE_LOCAL_OPENAI = True`
4. 运行 `python test_local_openai.py` 测试连接
5. 启动应用 `python main.py`

### 切换回百度千帆

1. 在 `kizuna_impl.py` 中设置 `USE_LOCAL_OPENAI = False`
2. 确保 `qianfan_token.py` 配置正确
3. 启动应用

## 🔍 技术细节

### API 接口设计

两种 AI 服务都实现了统一的 `chat(messages)` 接口：

```python
def chat(self, messages: list[dict]) -> str:
    """
    Args:
        messages: [{"role": "user", "content": "你好"}]
    Returns:
        AI 回复的文本内容
    """
```

这使得切换 AI 服务时无需修改业务逻辑代码。

### 配置管理

采用模块化配置：
- `qianfan_token.py` - 百度千帆配置
- `local_openai_config.py` - 本地 OpenAI 配置
- 通过 `USE_LOCAL_OPENAI` 开关控制

### 错误处理

- 完善的异常捕获
- 详细的错误日志
- 友好的用户提示

## 📊 对比分析

| 特性 | 本地 OpenAI | 百度千帆 |
|------|------------|----------|
| 成本 | 完全免费 | 有免费额度，超额收费 |
| 隐私 | 数据本地处理 | 数据发送到云端 |
| 网络 | 离线可用 | 需要网络连接 |
| 速度 | 取决于硬件 | 通常较快 |
| 质量 | 取决于模型 | 高质量 |
| 定制性 | 高度可定制 | 有限 |
| 维护 | 需自行维护 | 无需维护 |

## 🚀 后续优化建议

1. **添加更多 AI 服务支持**
   - OpenAI GPT
   - Anthropic Claude
   - 阿里云通义千问

2. **性能优化**
   - 支持流式响应
   - 添加请求缓存
   - 异步调用优化

3. **用户体验**
   - GUI 配置界面
   - 实时切换 AI 服务
   - 模型性能监控

4. **功能增强**
   - 多模型轮询
   -  fallback 机制
   - 对话历史管理

## 📞 问题反馈

如果在使用过程中遇到问题：
1. 查看相关日志输出
2. 运行测试脚本诊断
3. 参考使用指南
4. 检查配置文件

---

**改造完成日期**: 2026-05-17
**版本**: v1.0
