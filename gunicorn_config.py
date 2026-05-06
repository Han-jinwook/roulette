import os

bind = "0.0.0.0:" + os.getenv("PORT", "10000")  # Render의 PORT 환경 변수 사용
workers = 1  # WebSocket 지원을 위해 반드시 1로 설정
worker_class = "gthread"  # SocketIO long-polling 지원 필수
threads = 8  # 동시 게스트·동기 I/O(Supabase) 경합 시 스레드 고갈 완화 (기존 4 → 8)
timeout = 120
keepalive = 5
preload_app = True
