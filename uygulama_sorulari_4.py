# 1)
# import time
# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)  
#         end_time = time.time()
#         duration = end_time - start_time
#         print(f"{func.__name__} fonksiyonu {duration:.4f} saniyede çalıştı.")
#         return result
#     return wrapper

# @timer_decorator
# def ornek_islem(saniye):
#     """Belirtilen saniye kadar bekleyen basit bir işlem."""
#     time.sleep(saniye)
#     return "İşlem Tamamlandı!"

# ornek_islem(1.5)



current_user = {"role": "user"}
def auth_decorator(gereken_rol):
    def decorator(func):
        def wrapper(*args, **kwargs):
            
            if current_user.get("role") == gereken_rol:
                
                return func(*args, **kwargs)
            else:
                
                return "Erişim Reddedildi: Yetersiz Yetki"
        
        return wrapper
    
    return decorator

@auth_decorator("admin")
def hassas_verileri_getir():
    return "Çok gizli devlet sırları: 123456"

print("--- 1. Deneme (Rol: user) ---")
print(hassas_verileri_getir())

print("\n--- 2. Deneme (Rol: admin) ---")
current_user["role"] = "admin"
print(hassas_verileri_getir())



