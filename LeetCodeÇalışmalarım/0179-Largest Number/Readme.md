179.Largest Number - Çözüm Notlarım

Soru Bizden Ne İstiyor?
Bize bir tam sayı listesi veriliyor. Bu sayıları yan yana dizerek oluşturulabilecek en büyük sayıyı bulmamız ve sonucu metin olarak döndürmemiz isteniyor.

Çözüm Mantığım
Bu soruyu çözerken başımdan oldukça öğretici bir deneme-yanılma süreci geçti:

İlk Yaklaşımım ve Düştüğüm Hata: Başlangıçta sayıları normal bir şekilde büyükten küçüğe sıralayıp dümdüz uç uca yapıştırmanın işi çözeceğini düşündüm. Matematiksel büyüklüğün metin birleştirmede de aynı şekilde kusursuz çalışacağını varsaydım.

Gerçekle Yüzleşme: Testleri çalıştırdığımda 3 ve 30 gibi sayılarda mantığımın çöktüğünü fark ettim. Büyük olanı başa koyunca 303 çıkıyordu, oysa küçük duran 3 başa gelirse 330 oluyordu. Anladım ki dümdüz sıralama yapmak, sayıların metin olarak birleştiklerinde yaratacağı bu devasa kombinasyon farkını tamamen görmezden geliyordu.

Doğru Çözüm: Hatalı mantığımı çöpe atıp sayıların tekil büyüklüğüne değil, yan yana geldiklerindeki uyumuna odaklandım.
Öncelikle bütün matematiksel sayıları kelime gibi yapıştırabilmek için metne çevirdim.
İç içe iki döngü kurarak her sayıyı kendisinin sağında kalan diğer sayılarla tek tek kapıştırdım.
İki sayıyı önce birinci artı ikinci, sonra da ikinci artı birinci olacak şekilde uç uca ekleyip test ettim.
Eğer sağdaki sayının başa gelmesi daha büyük bir sonuç üretiyorsa, bu iki sayının listedeki yerini birbiriyle takas ettim.
Bu sayede büyük kombinasyon üreten sayılar listenin başına kaydı. Son adımda join yapıştırıcısıyla hepsini aralıksız birleştirdim. Sadece sıfırlardan oluşan bir liste ihtimaline karşı da ilk harfi kontrol edip gerekirse tek bir sıfır döndürdüm.

Performans ve Karmaşıklık

Zaman Karmaşıklığı: O N kare. Listeyi kendi kurallarıma göre sıralamak için iç içe iki adet döngü kullandım. Bu yüzden her elemanı diğerleriyle teker teker kıyaslamak zorunda kaldım ve işlem süresi veri sayısının karesi oranında artmış oldu.

Alan Karmaşıklığı: O N. Bize verilen orijinal sayı listesi üzerinde çalışmak yerine, elemanları metne çevirip oluşturduğum yeni listeyi kullandım. Bu nedenle listedeki veri miktarı kadar ekstra hafıza alanı tüketmiş oldum.
