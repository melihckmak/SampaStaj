İncelediğim bu makale, robotların kameralardan gelen görüntüleri kullanarak nasıl hareket edeceğini anlatıyor. Eskiden bu sistemlerde robotlar her an için 
sadece tek bir adım sonrasını tahmin ediyordu. Bu eski modellerin en büyük sorunu, önlerine iki farklı doğru yol çıktığında kararsız kalıp engellere çarpmasıydı.
Ayrıca her salise yeni bir karar aldıkları için robotun motorları sürekli titriyor ve robot hafif bir darbe aldığında hemen kilitlenip donuyordu.
Makaledeki araştırmacılar bu sorunları çözmek için difüzyon teknolojisini robot hareketlerine uyarlayarak Diffusion Policy algoritmasını geliştirdiler.
Bu yeni sistem yapacağı hareketi doğrudan hesaplamak yerine, rastgele bir gürültüyü kamera görüntüsüne bakarak adım adım temizliyor ve net bir rotaya dönüştürüyor.
Sadece tek bir anı değil, önündeki 16 adımlık tüm yolu tek seferde pürüzsüz bir paket halinde çıkardığı için motorlardaki titremeleri tamamen bitiriyor.
2023 yılında yayımlanan bu çalışmanın test sonuçlarına baktığımda çok büyük bir fark görüyorum. Sistem 15 farklı görevde denendi ve kendinden önceki en iyi modellere
göre başarı oranını ortalama %47 artırdı. Hatta eski modellerin %40'ı bile geçemediği çok zorlu taşıma ve hassas alet asma görevlerinde başarıyı %80 ile %100
seviyelerine çıkardı. Kısacası bu yeni model, robotların kararsız kalmadan ve titremeden tıpkı bir insan gibi akıcı hareket etmesini sağlıyor.
