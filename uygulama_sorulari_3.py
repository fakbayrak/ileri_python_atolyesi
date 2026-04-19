# 1) def islem_merkezi(sayi1, sayi2):
#     def toplama():
#         return sayi1 + sayi2
#     def cikarma():
#         return sayi1 - sayi2
#     def bolme():
#         return sayi1 / sayi2
    

#     dict = {
#         "toplam": toplama(),
#         "cikarma": cikarma(),
#         "bolme": bolme()}
    
#     print(dict)

# islem_merkezi(10, 5)


# 2) def logger(seviye):
#     def mesaj_yaz(metin):
#             return f"{seviye} {metin}"
#     return mesaj_yaz 
    
# bilgi_log = logger("INFO")
# hata_log = logger("ERROR")
# print(bilgi_log("Sistem çalışıyor"))
# print(hata_log("Bağlantı hatası"))


# 3) def hesap_makinesi(liste,islem_fonksiyonu):
#     sonuc=[]
#     for i in liste:
#         sonuc.append(islem_fonksiyonu(i))
#     return sonuc

# def kare_al(x):
#     return x**2

# def kup_al(x):
#     return x**3


# print(hesap_makinesi([1,2,3,4,5],kare_al))
# print(hesap_makinesi([1,2,3,4,5],kup_al))
