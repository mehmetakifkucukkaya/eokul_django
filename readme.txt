Proje Tanımı: 
    Proje bir e-okul klonudur. E-okul içerisinde olması gereken işlevleri belirli bir ölçüde kendisinde barındırır.

Projede şu ana kadar yapılanlar:
    - Proje dosyası oluşturuldu. Settings.py dosyasına postgre veri tabanı bağlantısı için gerekli konfigürasyonlar yapıldı, eokul_app INSTALLED_APPS kısmına eklendi, urls.py dosyasına eokul_app.urls eklendi. 
    - eokul_app isminde bir app dosyası oluşturuldu. 
    - eokul_app için kullanılacak modeller eokul_app/models kısmında tanımlandı. Modeller ve ilişkileri burada yazıldı.
    - Yazılan modeller için validation kuralları yazıldı. 
    - eokul_app için kullanılacak viewler eokul_app/views kısmında tanımlandı. student_login ve admin_login için viewler yazıldı. 
    - Projenin ana html iskeleti için ./templates klasörü oluşturuldu ve bir index.html dosyası yazıldı. Tüm projede kullanılacak ana css ve jss'ler bu dosyaya import edildi.
    - Proje için kullanılacak gerekli js ve css dosyaları için static klasörü oluşturuldu. 
    - Projenin login sayfası yazıldı. 


Projede şu andan itibaren yapılıcaklar:
    - student/dashboard urli için bir view yazılacak. View bir html template* dönecek. View sadece student giriş yapıldığında aktif olacak diğer türlü tekrar login page'e dönüş yapılacak.
        * student/dashboard için yazılacak html template'inde solda bir menü içerisinde bir link listesi olacak(dersler, profil, haftalık ders programı vb.), sağda ise menüde tıklanana göre bir block content dönecek.
    - admin/dashboard urli için bir view yazılacak. View bir html template* dönecek. View sadece admin giriş yapıldığında aktif olacak diğer türlü tekrar login page'e dönüş yapılacak.
        * admin/dashboard için giriş yapan kişinin öğretmen ya da müdür olmasına göre farklı bir dashboard template'i dönecek (if else kullanılabilir.) öğretmen için öğrencileri listeleme, notlar ekleme, dersleri görüntüleyebilme  ve öğrenciye özel ders ekleyebilme özellikleri olucak. müdür için öğretmen ve öğrenci ekleyebilme, ders ekleyebilme, haftalık ders programını güncelleyebilme özellikleri olucak.
    - student ve lesson modeli ile ilişkili bir students_lesson modeli yazılacak. (bir öğrencinin birden fazla dersi olabilir. aynı dersi birden fazla öğrenci alabilir.)
    - müdür,öğretmen ve öğrenci için çalışacak fonksiyonlar için özel bir decorator yazılacak. Bu decorator fonksiyonlara yetki vericek bu şekilde o fonksiyon sadece yetkisi olan için çalışacak diğer türlü bir hata mesajı döndürecek.

        
