# Apple Music Link Parser 后端

基于 FastAPI + Uvicorn 的 Apple Music 链接解析服务。

## 功能特性

- 🎵 自动检测和解析 Apple Music 链接
- 🔍 支持多种分隔符的文本分割  
- 🌐 RESTful API 接口
- 📊 结构化 JSON 响应
- 🚀 高性能异步处理
- ⚙️ 基于 YAML 的集中配置管理
- 🔧 无需修改代码即可调整配置

## 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 启动服务

#### 方法一：使用启动脚本
```bash
chmod +x start.sh
./start.sh
```

#### 方法二：直接启动
```bash
cd python
python backend.py
```

### 服务地址

- API 服务：http://localhost:8000
- API 文档：http://localhost:8000/docs
- 健康检查：http://localhost:8000/health

## API 接口

### POST /api/tasks

处理 Apple Music 链接解析或搜索请求。

#### 请求格式

```json
{
  "input": "这里是包含 Apple Music 链接的文本"
}
```

#### 响应格式

```json
{
  "apple_music_links": ["链接1", "链接2"],
  "link_types": ["album", "song"],
  "needs_search": false,
  "message": "处理结果描述"
}
```

#### 链接类型说明
- `album`: 专辑
- `song`: 歌曲  
- `playlist`: 播放列表
- `artist`: 艺术家
- `music_video`: 音乐视频

#### 示例

**解析 Apple Music 链接:**
```bash
curl -X POST "http://localhost:8000/api/tasks" \
  -H "Content-Type: application/json" \
  -d '{"input": "听听这首歌 https://music.apple.com/us/album/example/123456"}'
```

**搜索模式:**
```bash
curl -X POST "http://localhost:8000/api/tasks" \
  -H "Content-Type: application/json" \
  -d '{"input": "周杰伦的新歌"}'
```

## 支持的 Apple Music 链接格式

- **专辑**：`https://music.apple.com/us/album/album-name/id123456`
- **歌曲**：`https://music.apple.com/us/song/song-name/id123456`
- **播放列表**：`https://music.apple.com/us/playlist/playlist-name/pl.123456`
- **艺术家**：`https://music.apple.com/us/artist/artist-name/id123456`
- **音乐视频**：`https://music.apple.com/us/music-video/video-name/id123456`

### 支持的域名
- `music.apple.com`（标准）
- `beta.music.apple.com`（测试版）
- `classical.music.apple.com`（古典音乐，仅专辑）

## 支持的分隔符

- 空格：` `
- 逗号：`,`
- 句号：`.` 、`。`
- 分号：`;` 、`；`
- 斜杠：`/` 、`\`
- 顿号：`、`

## 开发说明

### 项目结构

```
server/
├── python/
│   └── backend.py          # 主应用文件
├── config/
│   └── config.yaml         # 📋 集中配置文件 (所有配置都在这里)
├── requirements.txt        # Python 依赖
├── start.sh               # 启动脚本
└── README.md              # 项目文档
```

### 配置管理

所有配置都集中在 `config/config.yaml` 文件中，包括：

- **服务器设置**: 主机、端口、重载模式、日志级别
- **CORS 配置**: 跨域访问控制设置
- **Apple Music 配置**: 正则表达式模式、支持的分隔符
- **API 信息**: 标题、版本、描述

修改配置后重启服务即可生效，无需修改代码。

### 核心功能

1. **链接检测**: 使用正则表达式识别 Apple Music 链接
2. **文本分割**: 支持多种分隔符的智能分割
3. **搜索判断**: 自动判断是否需要进行搜索处理
4. **错误处理**: 完善的异常处理和错误响应

### 扩展功能

- [ ] 实现搜索处理逻辑
- [ ] 添加缓存机制
- [ ] 支持批量处理
- [ ] 添加认证机制
