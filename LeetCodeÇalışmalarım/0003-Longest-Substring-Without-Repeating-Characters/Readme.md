# 74. Search a 2D Matrix - Çözüm Notlarım

## Soru Bizden Ne İstiyor?
Bize verilen bir kelimenin içinde, hiçbir harfin tekrar etmediği yan yana duran en uzun parçayı bulmamız ve bunun uzunluğunu döndürmemiz isteniyor.

## Çözüm Mantığım
Soruyu çözerken boş bir liste oluşturup harfleri sırayla içine atmaya başladım. İlk başta şöyle bir mantık kurdum: Eğer listeye ekleyeceğim harf zaten içeride varsa, listeyi tamamen sıfırlayıp yola öyle devam edeyim. Ancak "1R1T7" gibi test kelimelerinde bu mantığın patladığını gördüm. Çünkü listeyi tamamen boşalttığımda, arada kalan sağlam harfleri haksız yere çöpe atmış oluyordum. Bu sorunu çözmek için listeyi tamamen sıfırlamak yerine, tekrar eden harfin listedeki yerini .index() ile bulup, listeyi sadece o harften sonrasını alacak şekilde dilimlemem gerektiğini fark ettim ve kodumu buna göre düzelttim.

Ayrıca bu süreçte kendi denemelerimi yaparken, elimdeki parçalanmış harf listesini ekranda dümdüz bir kelime gibi birleşik görmek istediğimde "".join(liste) komutunun ne kadar pratik bir araç olduğunu öğrendim.

Fakat asıl aydınlanmayı algoritmanın çalışma şeklinde yaşadım. Ben kendi çözümümde tekrar eden harfi bulmak için liste içinde .index() ile arama yapacak bir kurgu hazırlamıştım. Meğer bu yöntem, bilgisayarın her seferinde listeyi baştan sona tek tek taramasına sebep oluyormuş. Soruyu bu şekilde çözdükten sonra analiz ekranında gördüm ki; karşılaştığım harflerin konumunu bir tabloya kaydetmek çok daha mantıklıymış. Böylece "Bu harf daha önce nerede karşıma çıkmıştı?" sorusunun cevabını liste içinde aramakla uğraşmadan, tablodan anında çekip alabiliyormuşuz. Bu kodumda kurguyu tablo ile yapmamış olsam da, listeler yerine sözlük kullanmanın gereksiz adımları atlayarak performansı nasıl uçurduğunu çok net bir şekilde öğrenmiş oldum.

## Performans ve Karmaşıklık
**Zaman Karmaşıklığı:** O(log(m * n)). Kendi kurduğum düzende liste içinde .index() ile arama yapıp listeyi dilimlediğim için bilgisayarı oldukça yormuşum. LeetCode istatistiklerinde çalışma zamanım 284 ms olarak ölçüldü ve tabloda diğer kullanıcıların oldukça gerisinde kaldığımı gördüm. Öğrendiğim Hash Tablosu mantığını kullansaydım arama süresini $O(1)$'e düşürerek genel hızı $O(N)$ seviyesine çıkarabilirmişim. 
**Alan (Bellek) Karmaşıklığı:** O(1). Sistem kodumun 20.26 MB hafıza kullandığını ölçtü. Kod Stili Analizi: LeetCode sistemi kodumun yapısını "Mükemmel", okunabilirliğini ise "İyi" olarak değerlendirdi. Sadece ufak bir tavsiye olarak; daha iyi bir global okunabilirlik için Türkçe değişken isimleri yerine İngilizce isimlendirmeler kullanmamın daha iyi olacağını not aldım.
