import os

bind = "0.0.0.0:" + os.getenv("PORT", "10000")  # Render의 PORT 환경 변수 사용
workers = 1  # WebSocket 지원을 위해 반드시 1로 설정
worker_class = "gthread"  # Supabase 등 비동기 라이브러리와 충돌 없는 스레드 모드
threads = 50  # 동시 접속 50명까지 15초 렉(고갈) 방지
timeout = 120
keepalive = 5
preload_app = True
