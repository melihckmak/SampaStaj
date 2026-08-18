3Sum - Çözüm Notlarım
Soru Bizden Ne İstiyor?
Bize verilen bir tam sayı listesi içinden, toplamları tam olarak 0 eden tüm üçlü sayı gruplarını bulmamız isteniyor. En kritik kural ise çözüm listemizde aynı sayı grubundan yani aynı üçlüden birden fazla kopya bulunmaması, her geçerli üçlünün yalnızca bir kez yer alması gerekiyor.

Çözüm Mantığım
Soruyu çözerken algoritmik kısayollara veya karmaşık yöntemlere başvurmak yerine, insan aklına gelen en doğrudan ve temel kaba kuvvet mantığını kurguladım.

Listedeki tüm olası üçlü kombinasyonları eksiksiz yakalayabilmek için iç içe 3 adet döngü açtım. İlk döngü birinci sayıyı sabit tutarken, ikinci döngü onun sağından başlayıp ikinci sayıyı, üçüncü döngü ise en sağdan başlayıp üçüncü sayıyı seçti. Her adımda bu 3 sayının toplamının 0 edip etmediğini kontrol ettim.

Toplamı 0 eden üçlüleri bulduğumda asıl problem kopyaların oluşması oldu. Çünkü eksi bir, bir, sıfır ile sıfır, eksi bir, bir gibi aynı sayılardan oluşan fakat sırası farklı gelen gruplar listeye birden fazla kez eklenebiliyordu. Bu sorunu çözmek için bulduğum her üçlüyü anında küçükten büyüğe sıralayarak standart tek bir kalıba soktum. Ardından bu kalıbın ana sepette daha önce bulunup bulunmadığına baktım, eğer sepette yoksa ana listeye ekledim.

Performans ve Karmaşıklık
Zaman Karmaşıklığı: O N küp. Listeyi tararken iç içe 3 adet döngü kullandığım için eleman sayısı arttıkça bilgisayarın yaptığı işlem sayısı kübik oranda katlandı. Üstelik her bulunan üçlü için yapılan sıralama ve listede var mı kontrolü de ekstra bir yük getirdi. Bu yöntem mantığı kavramak için harika olsa da, büyük test girdilerinde süre sınırına takılacaktır. Bu soru için standart olan İki İşaretçi yaklaşımı kullanılsaydı listeyi önce sıralayıp işlem süresini O N kare seviyesine çekebilirdik.

Alan Karmaşıklığı: O 1. Sorunun bizden dönmemizi istediği sonuç listesi haricinde, sadece döngü sayaçları ve 3 elemanlık geçici paketler kullandığım için hafızada yok denecek kadar az ekstra yer harcamış oldum.
