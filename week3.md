# CMPE 322 - Week 3: Delay and Loss

**Eğitmen:** Engin Hengirmen
**Konu:** Delay, Loss, and Throughput

## Types of Network Delays
Bir paket yola çıktığında düğümlerde (router) farklı gecikmelere maruz kalır. [cite_start]Toplam düğüm gecikmesi formülü şöyledir: $d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$[cite: 837].

- [cite_start]**Processing Delay:** Paketin başlığının incelenmesi ve hata kontrollerinin yapılması için geçen süredir[cite: 774, 775].
- **Queuing Delay:** Paketin bağlantıya aktarılmak üzere kuyrukta beklediği süredir. [cite_start]Trafik yoğunluğuna bağlıdır[cite: 778, 779].
- [cite_start]**Transmission Delay:** Paketin tüm bitlerinin donanımsal olarak linke (kabloya) itilmesi için gereken süredir[cite: 786, 789].
- **Propagation Delay:** Hatta giren bir bitin fiziksel medya üzerinden diğer router'a ulaşması için geçen süredir. [cite_start]Mesafe ile ilgilidir[cite: 792, 797].

## Packet Loss (Paket Kaybı)
- [cite_start]Yönlendiricilerde bulunan tampon belleğin (buffer) kapasitesi sınırlıdır[cite: 497].
- [cite_start]Ağ çok yoğun olduğunda ve kuyruk tamamen dolduğunda, yeni gelen bir paket düşürülür (packet loss) veya mevcut paketlerden biri silinir[cite: 497].