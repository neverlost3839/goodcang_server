FROM python:3.12-slim

WORKDIR /app

# 使用清华镜像源
RUN pip install uv -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制依赖文件
COPY pyproject.toml ./

# 安装依赖 - 使用国内镜像
RUN uv sync --frozen || uv sync -i https://pypi.tuna.tsinghua.edu.cn/simple

# 复制应用代码
COPY . .

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
