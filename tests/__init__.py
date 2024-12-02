try:
    from .key import get_key
except:
    def get_key():
        raise NotImplementedError("""
        tests/key.py를 구현해야 합니다.
        
        ```python
        # 예제 코드
        # key.py
        def get_key() -> str:
            return "your_api_key"
        ```
        """)
