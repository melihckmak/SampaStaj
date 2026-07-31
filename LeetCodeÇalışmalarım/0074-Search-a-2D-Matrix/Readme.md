# 74. Search a 2D Matrix - Çözüm Notlarım

## Soru Bizden Ne İstiyor?
Bize satırları ve sütunları kendi içinde artarak sıralanmış bir matris veriliyor. İçinde belirli bir sayıyı bulmamız isteniyor. Ancak bunu yaparken bütün sayıları tek tek kontrol etmememiz, işlemi $O(log(m * n))$ İkili Arama hızında çözmemiz gerekiyor.

## Çözüm Mantığım
Soruyu çözerken matrisi katlardan oluşan bir tablo gibi değil de, bütün satırları uç uca eklenmiş dümdüz, uzun ve tek boyutlu bir liste gibi hayal ettim. Liste baştan sona sıralı olduğu için hedef sayıyı bulmak adına **İkili Arama** algoritmasını uyguladım.

Buradaki asıl kilit nokta, düz listedeki hayali indeks numarasını, bilgisayarın matriste bulabileceği gerçek "satır" ve "sütun" koordinatlarına çevirmekti. Bunun için şu matematiksel formülü kullandım:
* Bulunduğum Satır = 'orta nokta // sütun_sayısı'
* Bulunduğum Sütun = 'orta_nokta % sütun_sayısı'

Böylece her adımda arama alanını tam ortadan ikiye bölerek, aradığım sayının sağda mı yoksa solda mı kaldığına baktım ve sınırları ona göre daralttım.

## Performans ve Karmaşıklık
**Zaman Karmaşıklığı:** O(log(m * n)). Arama uzayını her adımda yarıya indirdiğim için hedef sayıya çok hızlı ulaştım. LeetCode testlerinde 0 ms sürede çalıştı.
**Alan Karmaşıklığı:** O(1). Matrisi kopyalamadım veya yeni bir liste oluşturmadım. Sadece 'sol', 'sag' ve 'orta' sınırları tutmak için birkaç küçük değişken kullandığım için ekstra hafıza harcamamış oldum.
