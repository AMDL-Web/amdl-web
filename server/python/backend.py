import re
import yaml
import uvicorn
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

# 配置加载器
def load_config() -> Dict[str, Any]:
    """
    从配置文件加载所有配置
    """
    config_path = Path(__file__).parent.parent / "config" / "config.yaml"
    
    try:
        with open(config_path, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail=f"配置文件未找到: {config_path}")
    except yaml.YAMLError as e:
        raise HTTPException(status_code=500, detail=f"配置文件解析错误: {str(e)}")

# 加载配置
config = load_config()

# 从配置创建 FastAPI 应用
app = FastAPI(
    title=config["api"]["title"],
    version=config["api"]["version"],
    description=config["api"]["description"]
)

# 从配置添加 CORS 中间件
cors_config = config["cors"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_config["allow_origins"],
    allow_credentials=cors_config["allow_credentials"],
    allow_methods=cors_config["allow_methods"],
    allow_headers=cors_config["allow_headers"],
)

# 从配置文件获取 Apple Music 配置
apple_music_config = config["apple_music"]
APPLE_MUSIC_PATTERNS = list(apple_music_config["patterns"].values())
SEPARATORS = apple_music_config["separators"]

# 请求模型
class TaskRequest(BaseModel):
    input: str

# 响应模型
class TaskResponse(BaseModel):
    apple_music_links: List[str]
    link_types: List[str]  # 链接类型：album, song, playlist, artist, music_video
    needs_search: bool
    message: str

def identify_link_type(link: str) -> str:
    """
    识别 Apple Music 链接的类型
    """
    # 专辑 (包括 classical.music)
    if re.search(APPLE_MUSIC_PATTERNS[0], link):
        return "album"
    # 歌曲
    elif re.search(APPLE_MUSIC_PATTERNS[1], link):
        return "song"
    # 播放列表
    elif re.search(APPLE_MUSIC_PATTERNS[2], link):
        return "playlist"
    # 艺术家
    elif re.search(APPLE_MUSIC_PATTERNS[3], link):
        return "artist"
    # 音乐视频
    elif re.search(APPLE_MUSIC_PATTERNS[4], link):
        return "music_video"
    else:
        return "unknown"

def extract_apple_music_links(text: str) -> List[str]:
    """
    从文本中提取所有符合 Apple Music 格式的链接
    支持专辑、歌曲、播放列表、艺术家、音乐视频等类型
    能够正确分离连续出现的多个链接（无分隔符）
    自动去除重复链接
    """
    all_links = []
    seen_links = set()  # 用于快速查重
    
    # 找到所有 Apple Music 链接的起始位置
    apple_music_starts = []
    for match in re.finditer(r'https://(?:beta\.music|music|classical\.music)\.apple\.com', text):
        apple_music_starts.append(match.start())
    
    # 从每个起始位置开始匹配完整链接
    for start_pos in apple_music_starts:
        remaining_text = text[start_pos:]
        
        # 尝试每个正则表达式模式
        for pattern in APPLE_MUSIC_PATTERNS:
            match = re.match(pattern, remaining_text)
            if match:
                link = match.group(0)
                # 使用 set 进行快速去重
                if link not in seen_links:
                    seen_links.add(link)
                    all_links.append((link, start_pos))
                break  # 找到匹配就停止，避免重复
    
    # 按在文本中出现的位置排序并返回去重后的链接
    all_links.sort(key=lambda x: x[1])
    unique_links = [link for link, pos in all_links]
    
    # 最后再次去重以确保绝对没有重复（使用保序去重）
    final_links = []
    for link in unique_links:
        if link not in final_links:
            final_links.append(link)
    
    return final_links

def split_and_parse_input(input_text: str) -> tuple[List[str], List[str], bool]:
    """
    解析输入文本，拆分并提取 Apple Music 链接
    返回: (apple_music_links, link_types, needs_search)
    """
    # 从配置获取分隔符
    separators = SEPARATORS
    
    # 首先提取所有可能的 Apple Music 链接
    apple_music_links = extract_apple_music_links(input_text)
    
    if apple_music_links:
        # 识别每个链接的类型
        link_types = [identify_link_type(link) for link in apple_music_links]
        
        print(f"检测到 {len(apple_music_links)} 个 Apple Music 链接:")
        for i, (link, link_type) in enumerate(zip(apple_music_links, link_types), 1):
            print(f"  {i}. [{link_type}] {link}")
            
        return apple_music_links, link_types, False
    else:
        # 如果没有检测到 Apple Music 链接，则需要进行搜索
        print(f"未检测到 Apple Music 链接，需要进行搜索处理: {input_text}")
        return [], [], True

@app.post("/api/tasks", response_model=TaskResponse)
async def process_tasks(request: TaskRequest):
    """
    处理任务请求，解析 Apple Music 链接或标记需要搜索
    """
    try:
        input_text = request.input.strip()
        
        if not input_text:
            raise HTTPException(status_code=400, detail="输入内容不能为空")
        
        # 解析输入文本
        apple_music_links, link_types, needs_search = split_and_parse_input(input_text)
        
        if apple_music_links:
            type_counts = {}
            for link_type in link_types:
                type_counts[link_type] = type_counts.get(link_type, 0) + 1
            
            type_summary = ", ".join([f"{count}个{type_name}" for type_name, count in type_counts.items()])
            
            response = TaskResponse(
                apple_music_links=apple_music_links,
                link_types=link_types,
                needs_search=False,
                message=f"成功解析出 {len(apple_music_links)} 个 Apple Music 链接 ({type_summary})"
            )
        else:
            # 其他内容处理逻辑的占位符
            response = TaskResponse(
                apple_music_links=[],
                link_types=[],
                needs_search=True,
                message="未检测到 Apple Music 链接，将进行搜索处理（功能待实现）"
            )
        
        # 打印输出用于测试
        print(f"处理结果: {response.dict()}")
        
        return response
        
    except Exception as e:
        print(f"处理错误: {str(e)}")
        raise HTTPException(status_code=500, detail=f"服务器内部错误: {str(e)}")

@app.get("/")
async def root():
    """
    根路径，返回API信息
    """
    api_config = config["api"]
    return {
        "message": api_config["title"],
        "version": api_config["version"],
        "description": api_config["description"],
        "endpoints": {
            "POST /api/tasks": "处理 Apple Music 链接或搜索请求",
            "GET /health": "健康检查"
        }
    }

@app.get("/health")
async def health_check():
    """
    健康检查端点
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    # 从配置启动服务器
    server_config = config["server"]
    uvicorn.run(
        "backend:app",
        host=server_config["host"],
        port=server_config["port"],
        reload=server_config["reload"],
        log_level=server_config["log_level"]
    )
