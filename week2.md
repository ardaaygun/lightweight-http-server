# CMPE 322 - Week 2: The Network Core

**Eğitmen:** Engin Hengirmen
**Konu:** Packet Switching vs. Circuit Switching

## The Network Core
- [cite_start]Ağ çekirdeği, uç sistemleri birbirine bağlayan paket anahtarlayıcılar ve bağlantıların oluşturduğu ağdır (mesh)[cite: 430].
- [cite_start]**Store-and-Forward:** Çoğu yönlendirici (router) bir paketin ilk bitini iletmeden önce paketin tamamını almak zorundadır[cite: 454, 455].
- [cite_start]Aktarım hızı $R$, paket boyutu $L$ ise iletim süresi $L/R$ saniyedir[cite: 451].

## Packet Switching (Paket Anahtarlama)
- [cite_start]Yönlendirme işlemi önceden rezerve edilmiş kaynaklar olmadan, anlık talep üzerine yapılır[cite: 583].
- [cite_start]Eğer varış bağlantısı başka paketlerle meşgulse, gelen paket tampon bellekte (buffer) beklemek zorundadır ve bu duruma kuyruk gecikmesi (queuing delay) denir[cite: 494].
- [cite_start]Devre anahtarlamaya kıyasla daha fazla kullanıcının ağı paylaşmasına olanak tanır[cite: 640].

## Circuit Switching (Devre Anahtarlama)
- [cite_start]İletişim süresince uçtan uca ağ kaynakları (tampon bellek, iletim hızı) garanti altına alınır ve rezerve edilir[cite: 558].
- [cite_start]Geleneksel telefon ağlarında yaygın olarak kullanılır[cite: 566].
- [cite_start]FDM (Frekans) ve TDM (Zaman) bölmeli çoğullama teknikleri kullanılır[cite: 589].
- [cite_start]Kullanılmayan boş sürelerde rezerve edilen kaynaklar ziyan olduğu için paket anahtarlamaya göre daha verimsiz bulunabilir[cite: 623].