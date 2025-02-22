print("Stres Testi ve İlgi Analizi Makinesi")
print("==================================")

# Kullanıcıdan giriş al
print("Başlamak için Enter'a bas...")
enter = input()

if enter == "":
    print("Başlıyor...")
    print()

    # Soru 1: Stres seviyesi
    print("1. Son zamanlarda kendini ne kadar stresli hissediyorsun? (1-5 arası, 1=en az, 5=en çok)")
    stres = int(input())

    # Soru 2: İlgi alanları (Yazılım)
    print("2. Bilgisayar programlama veya yazılım geliştirmeyi ne kadar seviyorsun? (1-5 arası, 1=en az, 5=en çok)")
    yazilim = int(input())

    # Soru 3: İlgi alanları (Sanat)
    print("3. Resim, müzik veya başka bir sanat dalını ne kadar seviyorsun? (1-5 arası, 1=en az, 5=en çok)")
    sanat = int(input())

    # Soru 4: İlgi alanları (Spor)
    print("4. Spor yapmayı veya fiziksel aktiviteleri ne kadar seviyorsun? (1-5 arası, 1=en az, 5=en çok)")
    spor = int(input())

    # Soru 5: İlgi alanları (Bilim)
    print("5. Bilim, doğa veya teknolojiyi ne kadar merak ediyorsun? (1-5 arası, 1=en az, 5=en çok)")
    bilim = int(input())

    # En yüksek ilgiyi bul
    en_yuksek_ilgi = max(yazilim, sanat, spor, bilim)
    ilgi_alani = ""

    if en_yuksek_ilgi == yazilim:
        ilgi_alani = "Yazılım ve programlama"
    elif en_yuksek_ilgi == sanat:
        ilgi_alani = "Sanat (resim, müzik, vb.)"
    elif en_yuksek_ilgi == spor:
        ilgi_alani = "Spor ve fiziksel aktiviteler"
    else:
        ilgi_alani = "Bilim ve teknoloji"

    # Stres analizi
    if stres >= 4:
        stres_durum = "Son zamanlarda oldukça stresli görünüyor olabilirsin. Kendine biraz zaman ayırmayı ve gevşemeyi deneyebilirsin."
    elif stres >= 2:
        stres_durum = "Orta düzeyde stres hissediyorsun. Dengeli bir şekilde ilerlemeye devam edebilirsin, ama bazen mola vermeyi unutma."
    else:
        stres_durum = "Harika! Çok stresli değilsin, bu enerjiyle hedeflerine ulaşabilirsin!"

    # Motivasyon ve öneri
    print("\nStres Testi ve İlgi Analizi Sonuçları")
    print("==================================")
    print(f"Stres Durumun: {stres_durum}")
    print("Öneri: "+ ilgi_alani +" daha fazla zaman ayırarak hem eğlenebilir hem de stresini azaltabilirsin.")
    print("Sen harika birisin! Kendine güven ve hedeflerine emin adımlarla ilerle.")

else:
    print("Başlamak için Enter'a basmalısın, lütfen tekrar dene.")