
Microsoft AirSim

Otonom araçlar için geliştirilmiş bir simülasyon platformudur. Özellikle derin öğrenme algoritmalarını eğitmek için mühim bir araç haline gelmiştir. Otonom araçların görsel olarak algılanması zor sayılabilecek (orman, şehir merkezleri) ortamlarda eğitilmesini ve ekstrem durumlarda test edilmesini sağlar. Kod içeriği C++ ve python ile hazırlanmıştır.

Windows ve Linux üzerinden çalıştırılabilir. Simülasyonun görselliğini sağlayan oyun motoru ve pek çok sistemde olduğu gibi iletişimi sağlamak için mavlink kütüphanesi kullanılır. Nvidia kullanılarak araçların fiziksel ortamdaki etkileşimleri yüksek doğrulukla hesaplanır. Özel sensörler ile hava durumu tespiti yapılır. Hızlı fizik simülasyonları (aynı anda birden fazla fiziksel durum hesaplaması yapan bir algoritma tipi), lazer ışınları sayesinde 3D görüntü almaya yarayan algoritmalar, görüntü segmentasyon algoritmaları (nesne tanıma için kullanılır) ve akıllı öğrenme algoritmalarından yararlanılmıştır.



PX4-Autopilot

Temel amaç drone’lardan sabit kanatlı ve dikey kalkış yapan araçlara kadar pek çok araçta tam otonom uçuş kabiliyeti sağlamaktır. Pek çok donanım ve sensörle çalışabilecek bir yapıdadır. MAVLink üzerinden GCS ve ROS sistemleri ile iletişim kurabilir yapıdadır.

Ubuntu üzerinden çalışan sistemde uORB (haberleşme kütüphanesi), MAVLink, Matrix (matematik kütüphanesi), MAVSDK (otonom görev yazmak için üst düzey bir kütüphanedir), kütüphanaleri kullanılırken simülasyon olarak ise Gazebo, AirSim ve jMAVSim (multikopterler için java simülatörü) kullanılır. Arayüzde QGroundControl ve ROS2 kullanılır.



Mavlink/Mavros

MAVLink Protokolü ile haberleşme sağlayan drone lar için ROS ile iletişim sağlayan C++ tabanlı sistemdir. Yani MAVLink protoklü ile gelen verileri (batarya, durum, hız) ROS’un anlayacağı şekilde çevirir ve yazılan ROS komutlarını da MAVLink paketlerine çevirir. Böylece temel bir ROS-MAVLink çeviri sistemi elde edilmiş olur.

Linux ve ubuntu üzerinden çalışabilen bu sistem gerekli mavlink kütüphanelerinden, konum için hazırlanan gps kütüphanelerinden ve sensörler için olan kütüphanelerden faydalanır. Gazebo ve SITL üzerinden simülasyonlar gerçekleştirir. Haberleşme de içerik üzere MAVLink ve ROS üzerinden sağlanır.

EKF2 Algoritması: sensörler her zaman mükemmel sonuç vermez, (gürültü sebebiyle) bu algoritma olasılık değerlendirmesi yaparak daha sağlam sonuçlar ortaya çıkmasını sağlar. (Extended Kalman Filter)
PID Kontrol Algoritması: Temel bir kontrol algoritmasıdır. Aracın mevcut açısı ile olması istenilen açıyı değerlendirerek motor gücünü ayarlar.




Ardupilot_gazebo

ArduPilot otopilot yazılımı ile gazebo simülasyon ortamı arasındaki iletişimi güçlendirmek için hazırlanan bir eklentidir. C++ ile hazırlanan bu ek daha hızlı ve verimli sistemlerin oluşması için hazırlanmıştır. Sensörlerle desteklenmiş ve JSON (veriyi düzenli saklar ve sistemler arasında taşır) kullanılarak SITL-Gazebo arası daha esnek veri alışverişi sağlamıştır.
Kodlar SITL ve gazebo haberleşme kütüphaneleri eklenerek hazırlanmıştır. Haberleşme MAVLink üzerinden sağlanır.

Sensor Modeling: Gazebo kusursuz veri gönderir ve gerçek hayatta bu denli kusursuz veri üretilmediği için bu veriye gerçek hayatta karşılaşılabilecek zorluklar (gürültü) ekleyen bir algoritma kullanımı gerekir.
Motor Thrust Mapping: ArduPilot’un gönderdiği PWM (Güç sinyalinin ne kadar verileceğini belirler) sinyallerini Gazebo fizik motoruna aktarım için uygun veri tipine dönüştürür.
Bunun yanında sensör verilerinin ve motor komutlarının bir engel oluşmadan aynı anda aktarımı için de asenkron haberleşmeden yararlanılır.



DroneKit_Python

Eski ve temel düzey bir repo olmasına karşın öğretici olduğu için yeni başlayanlar tarafından tercih edilir. Tamamen python ile yazılmıştır ve Drone lar için otonom sistem uygulamalarının yazılmasını, görevlendirme yapılmasını ve yki uygulamalarının yazılmasını (basit şekilde) sağlar.

Linux, MacOS ve Windows üzerinden çalıştırılabilir. Pymavlink, monotonic (zamanlama ve timeout hesaplamaları için kullanılır.) kullanılır. SITL simülasyonu ve MAVLink protokolü de bu sistemde yararlanılan diğer önemli araçlardır.



Eflatun-IHA

Otonom uçuş yapabilen, belirli görevleri (hedef tespiti, kilitlenme vb.) yerine getirebilen yki ile haberleşebilen bir İHA projesidir. Ağırlıklı olarak C++ kullanılsa da arayüz tasarlamak gibi bazı işlemlerde de python kullanılmıştır.

Ubuntu ve Linux’da çalışabilir. ROS tabanlı olduğu için bu sistemlerde çalışması daha makuldür. Numpy, mavlink, OpenCv (şerit izleme, rakip takibi vb. İşlemler için) gibi kütüphaneler kullanılır. Simülasyon ortamı gazebo ile sağlanmış olup ROS ile iletişim sağlanır. Derin öğrenme, SITL ve ROS’un fazlaca kullanıldığı bu sistemler aynı zamanda otonom görev yönetimi, hata yönetimi ve çeşitli görüntü işleme algoritmalarından destek alırlar.



rotors_simulator

Mikro hava araçları için yüksek gerçekçilik oranına sahip bir simülasyon ortamı hazırlamak amacıyla geliştirilmiştir. Aracın fiziksel özellikleri, motor durumu ve sensör verileri en gerçekçi şekilde modellenerek test aşaması için imkan sağlanır. 
Ubuntu ve Linux üzerinden çalışabilecek sistem Eigen (vektör hesaplayıcı), MAV comm, Gazebo Plugins (pervanelerin ürettiği kuvvetleri simüle eden araç) kütüphanelerinden yararlanır. Gazebo ortamında yapılan simülasyon ROS kullanır. Geometrik kontrol (drone un manevraları sırasındaki kontroller), gazebo physics engine (Diferansiyel denklem çözer) ve durum kontrol algoritmaları kullanılarak hazırlanır.



Toy_Siha (github.com/burakcetin19/TOY_SIHA_2026)

Otonom uçuş yapabilen, çeşitli görevleri yerine getirmekle yükümlü bir İHA projesidir. C++ ve Python ağırlıklı yazılım dili kullanılır.

Ubuntu ve Linux üzerinden çalışan bu sistem, OpenCv, pymavlink ve yolo (yapay zeka tabanlı nesne tespiti) algoritmalarından yararlanır. Gazebo ile simüle edilen proje haberleşmede ROS ve MAVROS ile haberleşme sağlar. Derin öğrenme algoritmaları, kalman filtresi (olasılık üzerine bir teknoloji), otonom karar verme, PID ve kilitlenme algoritmaları kullanır.



Fritim

Otonom bir sistemin çevredeki nesneleri ayırt etmesini sağlamak, sisteme görev vererek görevlerin de otonom şekilde tamamlanmasını sağlamak amaçlanır. Sensörlerdeki ham veri işlenip karar verilir ve bu karar motora iletilir. Python ve C++ kullanılarak hazırlanmıştır.

Ubuntu ve Linux üzerinden çalışır, MAVROS, OpenCv ve YOLO kütüphaneleri kullanılır. Simülasyonlar gazebo üzerinden gerçekleştirilir. Computer Vision, (kameradan gelen kareleri anlık olarak işleyen ve alamlandıran teknoloji, bilgisayarlı görü) ROS, hedef takip algoritmaları, PID, projenin aşamalarını gösteren (kalkış, iniş, uçuş vb.) gösteren algoritmalardan faydalanılmıştır.


