# 1) ham_veriler = ["Ahmet ", " ", "Meryem ", None, "Ali ", " ", " Selin"]
# filtered= list(filter(lambda x:x is not None and not x.isspace(), ham_veriler))
# print(filtered)
# temizlenmis_veriler = list(map(lambda x: x.strip(), filtered))
# print(temizlenmis_veriler)


# 2)ogrenciler = [
# {"ad": "Lale", "notlar": [70, 80, 90]},
# {"ad": "Deniz", "notlar": [40, 50, 30]},
# {"ad": "Arda", "notlar": [90, 95, 100]},
# {"ad": "Zeynep", "notlar": [60, 60, 70]} ]

# for i in range(0, len(ogrenciler)):
#     ogrenciler[i]["ortalama"] = sum(ogrenciler[i]["notlar"])/len(ogrenciler[i]["notlar"])

# print(ogrenciler)

# filtered= list(filter(lambda ogrenci: ogrenci["ortalama"]>=70, ogrenciler))
# print(filtered)

# sorted= sorted(ogrenciler,key=lambda ogrenci: ogrenci["ortalama"],reverse=True)
# print(sorted)


