# def usAlma(taban):
#     def inner(us):
#         return taban**us
#     return inner
# sonuc=usAlma(2)(3)
# fn=usAlma(5)  Birinci parametre dış fonksiyona verilir ve ikinci parametre iç fonksiyona verilir.
# sonuc=fn(4)
# print(sonuc)


# def yetki_sorgulama(sayfa):
#     def inner(rol):
#         if rol=="Admin":
#             return f"{rol} rolü {sayfa} sayfasına erişim izni var."
#         else:
#             return f"{rol} rolü {sayfa} sayfasına erişim izni yok."
#     return inner

# yetki= yetki_sorgulama("Ürün Güncelleme")
# print(yetki("Admin"))
# print(yetki("Kullanıcı"))


