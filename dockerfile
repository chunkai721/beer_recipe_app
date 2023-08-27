# 使用官方的Python 3.8映像作為基礎映像
FROM python:3.8-slim-buster

# 設置工作目錄
WORKDIR /app

# 設置環境變量
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# 安裝依賴
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 安裝Python依賴
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# 複製應用程序代碼到容器中
COPY . /app/

# 暴露端口
EXPOSE 5000

# 啟動應用程序
CMD ["python", "beer_recipe_app/main.py"]
