# 📊 Instagram Veri Analizi

Bu proje, Instagram gönderilerine ait etkileşim ve erişim verilerinin Python kullanılarak analiz edilmesi ve görselleştirilmesi amacıyla geliştirilmiştir.

Projede gönderilerin ana sayfa, hashtag ve keşfet üzerinden aldığı erişimler; beğeni, yorum, paylaşım, profil ziyaretleri ve takipçi kazanımı gibi etkileşim verileri incelenmektedir. Elde edilen sonuçlar çeşitli grafikler ve veri görselleştirme yöntemleri kullanılarak analiz edilmektedir.

Ayrıca kullanıcı deneyimini geliştirmek amacıyla analiz sonuçlarının tek bir pencere üzerinden görüntülenebildiği, **Önceki** ve **Sonraki** butonlarıyla grafikler arasında geçiş yapılabilen bir arayüz geliştirilmiştir.

---

##  Özellikler

###  Erişim Analizi

- Ana sayfadan gelen erişimlerin incelenmesi
- Hashtaglerden gelen erişimlerin incelenmesi
- Keşfet bölümünden gelen erişimlerin incelenmesi
- Diğer kaynaklardan gelen erişimlerin incelenmesi
- Erişim kaynaklarının toplam dağılımının görselleştirilmesi

###  Etkileşim Analizi

- Beğeni ve gösterim arasındaki ilişkinin incelenmesi
- Profil ziyaretleri ve yorumlar arasındaki ilişkinin incelenmesi
- Paylaşım ve gösterim arasındaki ilişkinin incelenmesi
- Profil ziyaretleri ile takipçi kazanımı arasındaki ilişkinin incelenmesi

###  Metin Analizi

- Gönderi açıklamalarındaki (Caption) kelimelerin analiz edilmesi
- Hashtag kullanımının incelenmesi
- WordCloud ile sık kullanılan kelimelerin görselleştirilmesi

###  Korelasyon Analizi

- Sayısal değişkenler arasındaki korelasyonların hesaplanması
- Korelasyon matrisinin ısı haritası (Heatmap) ile gösterilmesi

###  Takipçi Dönüşüm Analizi

- Profil ziyaretlerinden takipçiye dönüşüm oranının hesaplanması
- Profil ziyaretleri ile takipçi kazanımı arasındaki ilişkinin görselleştirilmesi

###  Grafik Arayüzü

- Tüm analizlerin tek pencere üzerinde görüntülenmesi
- ` Önceki` butonu ile önceki analize geçiş
- `Sonraki ` butonu ile sonraki analize geçiş
- Dokuz farklı analiz sayfası arasında kolayca gezinme

---

##  Kullanılan Teknolojiler

| Teknoloji | Kullanım Alanı |
|---|---|
| Python | Proje geliştirme |
| Pandas | Veri okuma ve veri analizi |
| Matplotlib | Grafik ve veri görselleştirme |
| Seaborn | Korelasyon ve gelişmiş grafikler |
| WordCloud | Metin ve kelime sıklığı analizi |
| Matplotlib Widgets | Grafik arayüzü ve butonlar |

---

##  Proje Yapısı

```text
Instagram-Veri-Analizi/
│
├── 📄 instagram.py
├── 📊 Instagram data.csv
├── 📖 README.md
├── 📦 requirements.txt
└── ⚙️ .gitignore
