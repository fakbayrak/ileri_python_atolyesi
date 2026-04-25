
# 1)
# class Ogrenci:
#     def __init__(self,ad,soyad,ders_notu):
#         self.ad=ad
#         self.soyad=soyad
#         self.ders_notu=ders_notu
    
#     def durum_sorgula(self):
#         if self.ders_notu >= 50:
#             return "Başarılı"
#         else:
#             return "Başarısız"
    
# ogrenci1 = Ogrenci("Ahmet", "Yılmaz", 75)
# ogrenci2 = Ogrenci("Ayşe", "Kara", 45)

# print(f"{ogrenci1.ad} {ogrenci1.soyad}: {ogrenci1.durum_sorgula()}")
# print(f"{ogrenci2.ad} {ogrenci2.soyad}: {ogrenci2.durum_sorgula()}")




# ###########################
# 2)
# class Urun:
#     urun_adet = 0
#     def __init__(self):
#         Urun.urun_adet += 1
    
#     @classmethod
#     def toplam_urun_sayisini_getir(cls):
#         return f"Toplam ürün sayısı: {cls.urun_adet}"

# urun1 = Urun()
# urun2 = Urun()
#  print(Urun.toplam_urun_sayisini_getir())






class Robot:
    toplam_robot_sayisi = 0
    def __init__(self,isim):
        self.isim = isim
        Robot.toplam_robot_sayisi += 1

    def selamla(self):
        return f"Merhaba, ben {self.isim}"
    
    @classmethod
    def robot_sayisini_sorgula(self):
        return f"Şu an dünyada {Robot.toplam_robot_sayisi} robot var."
    
robot1 = Robot("Faruk")
robot2 = Robot("Ayşe")
print(robot1.selamla())
print(robot2.selamla())
print(Robot.robot_sayisini_sorgula())










