import os

bind = "0.0.0.0:" + os.getenv("PORT", "10000")  # Render의 PORT 환경 변수 사용
workers = 1  # WebSocket 지원을 위해 반드시 1로 설정
worker_class = "eventlet"  # SocketIO 비동기 처리를 위해 eventlet 사용
timeout = 120
keepalive = 5
preload_app = True
