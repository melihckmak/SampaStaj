54. Spiral Matrix - Çözüm Notlarım

Soru Bizden Ne İstiyor?
Bize 2 boyutlu bir matris veriliyor. İçindeki tüm elemanları dıştan içe doğru kıvrılan bir Sarmal yörünge izleyerek tek bir düz liste halinde döndürmemiz isteniyor. Yani saat yönünde ilerleyerek matrisi çözmemiz gerekiyor.

Çözüm Mantığım
Bu soruyu çözerken başımdan oldukça öğretici bir deneme-yanılma süreci geçti:

İlk Yaklaşımım ve Düştüğüm Hata: Başlangıçta soruyu satırların tek veya çift olmasına göre çözebileceğimi düşündüm. Mantığım şuydu: "Çift indeksli satırlarda ileri gideyim, tek indeksli satırlarda geri gideyim". Bunun için bolca while döngüsü ve geçici sayaç yazarak sınırları zorladım.
Gerçekle Yüzleşme:Testleri çalıştırdığımda kodumun sarmal değil, bir Yılan hareketi yaptığını fark ettim. Anladım ki sarmal harekette yön, satırın tek veya çift numaralı olmasına bağlı olamazdı. Sarmal hareket köşeleri dönerek merkeze doğru daraldığı için, ilk denediğim o matematiksel kural bu sorunun doğasına tamamen aykırıydı.
Doğru Çözüm: Hatalı mantığımı tamamen çöpe atıp, dünya çapında kabul gören "Sınır Daraltma " tekniğine geçtim. Matrisin etrafına `ust_duvar`, `alt_duvar`, `sol_duvar` ve `sag_duvar` olmak üzere dört adet hayali sınır çizdim.
  * Tek bir ana `while` döngüsü kurdum: Sınırlar birbirine çarpana kadar işlem devam edecekti.
  * Sırasıyla 4 temel hareketi yaptım: Üst kenarı sağa tara, sağ kenarı aşağı tara, alt kenarı sola tara, sol kenarı yukarı tara.
  * Her kenarı tarama işlemim bittiğinde, o kenara ait duvarı bir adım içeri kaydırdım.
  * Matrisin tek satır veya tek sütun olma ihtimaline karşı sayıları iki kere kopyalamamak için, alt ve sol duvarları dönerken aralara ekstra `if` kontrolleri ekledim.

Performans ve Karmaşıklık

Zaman Karmaşıklığı: $\mathcal{O}(m \times n)$. Matrisin içindeki hiçbir sayının üzerinden iki kere geçmedim. Ana döngü sayesinde her eleman sadece ve tam olarak bir kez ziyaret edildiği için süre matrisin boyutuyla doğru orantılıdır.
Alan Karmaşıklığı: $\mathcal{O}(1)$. Sorunun bizden istediği sonuç listesini saymazsak, matrisi kopyalamadım veya ekstra bir matris oluşturmadım. Sadece sınırları takip etmek için 4 adet basit tam sayı değişkeni kullandığımdan ek hafıza harcamamış oldum.
