ArduPilot uçuş modları hakkında kısa bir araştırma 
Stabilize: Genelde test uçuşları için kullanılır, bu modda araç kendi dengesini sağlar. Rüzgar ve küçük sapmalar otomatik olarak düzeltilir.Drone dengeyi korur.
Altitutde Hold: Drone'un sabit bir yükseklikte kalmasını sağlayan moddur.
Loiter ve Position Hold: GPS destekli olan bu modlar pozisyon ve yüksekliğin sabitlenebilidiği için dış etkenlere karşı drone konumu bozulmaz. 
Auto: önceden olanlanmış görev listesini (waypoint) takip eden otonom uçuş modu
Guided: Otonom uçuşta esneklik sağlayan ve anlık komut alabilen bir moddur. Drone bu modda iken Python dronekit veya gcs üzerinden hareket komutları alabilir. Bu mod gerçek zamanlı kontrol gerektiren durumlar için idealdir.
RTL:Drone'un kalkış noktalarına otomatik geri dönüşünü sağlar.

Python kodları hazırlanırken yapay zekadan oldukça fazla yararlanıldı ama yapay zekanın verdiği tüm kodlar ayrıca teker teker incelendi ve içerikleri öğrenildi, aşağıda akış üzerinden açıklamalar yapılarak bazı kodlar verildi

1) pymavlink kullanılacağı için kütüphane import edildi.
2) (udp:127.0.0.1.14550) -pymavlinkteki bağlantı adresi
3) mavutil.mavlink.MAV_CMD_NAV_WAYPOINT-drone erişimi var mı
4) def set_mode(mode_name):
    mode_id = master.mode_mapping()[mode_name] -mode isimleri sayısal id ye çevirilir
5)master.target_system -drone sistem id
6)mavutil.mavlink.MAV_MODE_FLAG_CUSTOM_MODE_ENABLED -özel uçuş modu
7) master.target_component -parça id
8) mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM -motorları açıp kapatma komutu
9) def takeoff(altitude) -drone u havalandır
10) master.mav.mission_item_send -belirlenen noktaya gitmesi için
11) mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT -konumun neye göre alındığını belirler deniden yükseklik olarak değil kalkılan yere göre yükseklik alındı
12) mavutil.mavlink.MAV_CMD_NAV_WAYPOINT -waypoint e git
13) msg = master.recv_match(type='GLOBAL_POSITION_INT', blocking=True) -drone dan gelen konum mesajını okur
14) lat, lon, alt = get_position() - konum bilgisini 3 değişkene ayırır
15) lat = msg.lat / 1e7 -gps formatını düzenler















<img width="1854" height="1034" alt="Screenshot from 2026-05-13 18-36-25" src="https://github.com/user-attachments/assets/b7b71b52-d940-4b63-ba7e-b09eb648c03e" />
verilen ekran görüntüsü ilk yapılan çalışmaya aittir, rüzgar durumu ve batarya gözlenebilmektedir

<img width="1854" height="1034" alt="Screenshot from 2026-05-13 19-13-03" src="https://github.com/user-attachments/assets/199c8763-bb36-4f1d-be37-98fe547d87e6" />


bu ekte ise terminal üzerinden yükseklik verisi akışı görülmektedir. Console da irtifan 15 olduktan sonra otomatik iniş moduna geçildiği ve başarılı şekilde inerek motorların kapatıldığı görülür


<img width="1854" height="1042" alt="Screenshot from 2026-05-16 12-32-25" src="https://github.com/user-attachments/assets/be0bbd24-48f3-41ee-a120-a1a1e57b12fb" />

waypoint görevinin yer aldığı bu ekte irtifa alnıması ilk waypoint olarak belirlenmiş olup 2. waypoint olarak silindirin üzerine gelerek bu işlemi tamamlamıştır 


<img width="1854" height="1042" alt="Screenshot from 2026-05-16 12-32-36" src="https://github.com/user-attachments/assets/0bfb49a2-2293-48db-abbf-e1b1280dc2fb" />


3. waypoint olan küp şeklinin üzerinde olduğu andan bir ek


<img width="1854" height="1042" alt="Screenshot from 2026-05-16 12-32-57" src="https://github.com/user-attachments/assets/782acfb2-e2a2-43ca-b493-c6b729c5cfdb" />



4. waypoint, küre şeklinin üzerinde olduğu andan bir ek


<img width="1854" height="1042" alt="Screenshot from 2026-05-16 12-33-05" src="https://github.com/user-attachments/assets/e5b0985a-c09d-4e8e-b4bd-44b23a176803" />


ardından 5. waypoint olarak kalkış yaptığı yere gelir ve inişe geçer









Karşılaşılan ve oyalayan tek hata "link 1 down" hatası oldu tam olarak neden olduğunu anlamasam da iki ihtimal olduğunu düşünüyorum, ya host da ayru olarak kurulan ardupşlot sebebiyle bir port sıkıntısı meydana geldi (docker içinde çalıştığımız için pek olası değil, docker kendi simülasyonunu kullanıyor ve ayrı olarak ardupilot açmamıştım) ya da gazebo başlatıldığında direkt simülasyon başlatılmadan ardupilot çalıştırıldı. bunun harici hata ile karşılaşılmadı. sistemde en uzun oyalanılan yerlerden biri bu hata diğeri de python kodlarının anlaşılması kısmı oldu.
