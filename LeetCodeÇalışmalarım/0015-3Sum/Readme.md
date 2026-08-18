# 15. 3Sum - Çözüm Notlarım

---

## Soru Bizden Ne İstiyor?

Bize verilen bir tam sayı listesi içinden, toplamları tam olarak 0 eden tüm üçlü sayı gruplarını bulmamız isteniyor. En kritik kural ise çözüm listemizde aynı sayı grubundan yani aynı üçlüden birden fazla kopya bulunmaması, her geçerli üçlünün yalnızca bir kez yer alması gerekiyor.

## Çözüm Mantığım

---

Soruyu çözerken algoritmik kısayollara veya karmaşık yöntemlere başvurmak yerine, insan aklına gelen en doğrudan ve temel kaba kuvvet mantığını kurguladım.

Listedeki tüm olası üçlü kombinasyonları eksiksiz yakalayabilmek adına iç içe 3 adet döngü açtım:

* Birinci döngü ilk sayıyı sabit tuttu.
* İkinci döngü ilkinin hemen sağından başlayıp ikinci sayıyı seçti.
* Üçüncü döngü ise ikincinin sağından başlayarak son sayıyı seçti.

Her adımda bu 3 sayının toplamının 0 edip etmediğine baktım. Toplamı 0 eden üçlüleri bulduğumda asıl problem kopyaların oluşması oldu. Çünkü sayılar aynı olsa bile farklı sıralarla geldiklerinde listeye birden fazla kez eklenebiliyorlardı.

Bu sorunu çözmek için şu adımları uyguladım:

* Bulduğum her 3 sayıyı anında küçükten büyüğe sıralayarak tek bir standart kalıba soktum.
* Hazırladığım bu paketin ana sonuç listesinde daha önce olup olmadığını kontrol ettim.
* Eğer listede yoksa yeni bir çözüm olarak ana listeye ekledim.

## Performans ve Karmaşıklık

---

**Zaman Karmaşıklığı:** O(N^3). Listeyi tararken iç içe 3 adet döngü kullandığım için eleman sayısı arttıkça bilgisayarın yaptığı işlem sayısı kübik oranda katlandı. Üstelik her bulunan üçlü için yapılan sıralama ve listede arama işlemleri de süreye ek yük getirdi. Bu yöntem mantığı kavramak için harika olsa da büyük veri setlerinde süre sınırına takılacaktır. **Alan Karmaşıklığı:** O(1). Sorunun bizden dönmemizi istediği ana sonuç listesi haricinde matrisi kopyalamadım veya büyük veri yapıları açmadım. Sadece döngü indislerini ve 3 elemanlık geçici paketleri kullandığım için ekstra hafıza harcamamış oldum.
