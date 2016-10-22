# Tugas eliminasi 1

## Tugas
Temukan dan betulkan *bug* teknis yang terdapat pada pesan-pesan terjemahan yang terdapat pada repo-repo GitHub. 

## Tujuan

Tugas ini bertujuan untuk membantu peserta mendapatkan pemahaman tingkat lanjut mengenai
*markup* teks dan format-format berkas terjemahan, serta alat-alat pengecek kualitas
bersumber terbuka yang tersedia untuk format berkas tersebut.

JANGAN menerjemahkan pesan-pesan, karena hal tersebut bukan tujuan dari tugas ini.

## Peringatan

Selama fase eliminasi berlangsung, para peserta tidak diperkenankan untuk
berinteraksi dengan repo GitHub yang telah dipilih oleh peserta lain untuk
tugas ini sampai peserta tersebut telah berhasil menyelesaikan tugasnya. 

Peserta Besut Kode Universitas tidak boleh memilih repo-repo berikut,
dan tidak diperkenankan untuk berinteraksi dengan repo-repo di bawah: 

- https://github.com/phpmyadmin/localized_docs/
- https://github.com/phpmyadmin/phpmyadmin/
- https://gitlab.com/noosfero/noosfero (salinan di https://github.com/noosfero/noosfero)
- https://github.com/godotengine/godot
- https://github.com/exaile/exaile
- https://github.com/hangoutsbot/hangoutsbot-locales

## Langkah-langkah

### Terima undangan

Anda akan menerima surel dari GitHub yang berisi undangan untuk bergabung dalam
organisasi BesutKode GitHub.

Anda harus menyetujui undangan tersebut.

Setelah Anda menyetujui undangan tersebut, Anda akan memiliki akses "Tulis" (*write*)
ke repositori berikut:

https://github.com/BesutKode/uni-task-1

Repositori ini adalah repositori privat, *namun* akan diubah menjadi repositori
publik pada 30 Oktober 2016.

Segala hal yang Anda lakukan akan selamanya bersifat publik.

DILARANG menyambungkan pranala pada suatu masalah (*issue*)
ataupun *Pull Request* dari repo lain. 

Ada saluran "gitter" untuk repositori ini, yang hanya bisa diakses oleh
peserta Besut Kode Universitas yang berhasil. 

https://gitter.im/BesutKode/uni-task-1

Saluran gitter ini publik tidak.

Gunakan saluran ini untuk bertanya atau meminta klarifikasi mengenai tugas ini. 

Disarankan untuk berlaku secara profesional dan berlaku layaknya
"mahasiswa yang bertanya" pada saluran ini. 

### Temukan 20 *bug* dalam proyek terjemahan

*Bug* yang terdapat pada pesan-pesan terjemahan termasuk masalah-masalah

-  semantik, seperti struktur tata bahasa yang hilang,
   contoh: tidak adanya titik pada akhir kalimat, dan lain sebagainya.

-  syntax errors, seperti pada variant bahasa dari bahasa sumber yang tidak semestinya di translate namun sudah terlanjur di translate.

Telah ada alat-alat bersumber terbuka untuk menemukan dan bahkan
membetulkan masalah-masalah ini secara otomatis.
Contoh alat bersumber terbuka untuk hal ini adalah
[`translate-toolkit`](https://en.wikipedia.org/wiki/Translate_Toolkit),
yang mana telah disertakan pada distribusi Linux pada umumnya. 

Pada wiki repo telah ada halaman "*Existing tools*" (perangkat yang telah tersedia).
Halaman tersebut berisi alat-alat yang mungkin berguna. 

Disarankan agar Anda mencari *bug*-*bug* terjemahan pada proyek-proyek yang menggunakan
layanan [Weblate](https://en.wikipedia.org/wiki/Weblate).
Weblate mengizinkan siapapun untuk memberikan kontribusi terjemahan yang kemudian
akan di-[lazy-commit](https://docs.weblate.org/en/latest/admin/continuous.html#lazy-commit)-kan pada reponya. 

Apabila proyek weblate disambungkan pada sebuah repo GitHub,
perubahan-perubahan yang dibuat pada layanan weblate akan muncul pada 
profil GitHub kontributor yang membuat perubahan tersebut di weblate,
**HANYA** apabila alamat surel yang digunakan oleh kontributor di 
GitHub dan di weblate sama.

Beberapa layanan weblate memungkinkan otentikasi (pembuktian) menggunakan 
akun GitHub, apabila Anda menggunakan alamat surel (*e-mail*) yang sama 
antara weblate dan GitHub. 

Pada wiki ada halaman "Weblate" yang berisi informasi mengenai layanan-layanan 
weblate. Dua layanan weblate terbesar yang di dalamnya terdapat beragam
proyek yang tersambung dengan repo GitHub adalah: 

- https://hosted.weblate.org/
- https://l10n.opensuse.org/

Peserta diperkenankan untuk memilih repo GitHub non-Weblate. 

Namun diperingatkan bahwa adalah hal yang biasa bagi proyek-proyek
untuk menolak menerima *Pull Request* untuk berkas-berkas terjemahan. 

Contohnya, [Proyek SugarLabs](https://github.com/sugarlabs) menggunakan 
layanan [Pootle](https://en.wikipedia.org/wiki/Pootle) pada 
[translate.sugarlabs.org](https://translate.sugarlabs.org/) untuk mengelola 
terjemahan, dan mereka akan menolak perubahan berkas yang terjadi di luar
layanan Pootle mereka sendiri. 

### Daftarkan proyek Anda

Hanya satu peserta yang diperkenankan untuk bekerja pada satu repo GitHub
pada satu waktu. Hal ini diberlakukan untuk menghindari berbagai perubahan
yang mungkin bentrok. 

Setiap peserta akan membuat sebuah halaman pada wiki repo BesutKode mengenai
repo yang telah mereka pilih dan *bug*-*bug* yang mereka temukan. 

Saat Anda telah menemukan sebuah proyek yang di dalamnya terdapat *bug* teknis,
pertama-tama cari di wiki untuk memeriksa apakah telah ada peserta lain yang
memilih repo tersebut. 

Apabila tidak ada yang memilih repo yang Anda inginkan, buat sebuah halaman
di wiki dan beri nama dengan nama pengguna GitHub Anda, dan cantumkan hal-hal berikut ini: 

1. Pranala (*link*) ke repo GitHub
2. Pranala ke halaman proyek terjemahan (contoh: layanan weblate)
3. Deskripsi teknis *bug* yang telah anda temukan
4. Perintah (*command*) yang Anda gunakan untuk menemukan *bug* tersebut
5. Keluaran (*output*) yang dihasilkan oleh perintah tersebut
6. Informasi lainnya yang terkait dengan hal ini.

Tulisan dalam bahasa Indonesia diperbolehkan dan diterima. 

### Perbaiki 20 *bug* atau lebih 

Proyek sumber terbuka yang menggunakan Weblate lebih menyukai terjemahan
yang disediakan menggunakan Weblate, karena hal ini mengurangi jumlah
pekerjaan untuk kontributor yang melakukan *commit* karena Weblate
secara otomatis memasukkan perubahannya. 

Namun, tugas ini membutuhkan Anda untuk melakukan modifikasi pada
sekelompok pesan-pesan dalam jumlah besar yang memiliki masalah teknis. 
Seluruh perbaikan teknis idealnya dimasukkan dalam Pull Request pada
proyek GitHub-nya, untuk dikaji bersama-sama.

Perhatikan pula bahwa pada umumnya proyek-proyek akan menolak *pull request* 
berkas-berkas berisi terjemahan.

Contohnya, openSUSE menunjukkan bahwa mereka lebih menyukai proses penerjemahan melalui weblate.

Selain itu, beberapa proyek dia menerima penerjemahan yang menggunakan
identitas penerjemah. Contohnya, [SugarLabs projects](https://github.com/sugarlabs)
menggunakan layanan [Pootle](https://en.wikipedia.org/wiki/Pootle) di 
[translate.sugarlabs.org](https://translate.sugarlabs.org/) untuk mengatur
hasil terjemahan mereka. Mereka akan menolak perubahan pada berkas terjemahan
itu yang bukan berasal dari layanan Pootle. Selanjutnya, terjemahan dari
layanan Pootle itu akan diterima oleh para pengelola secara *ad hoc*.

Dalam tugas ini, tidak dipermasalahkan apakah Anda menggunakan *pull request*
atau menggunakan layanan penerjemahan web, selama perubahan itu tampil di 
profil GitHub Anda (yaitu, suntingan di layanan Pootle akan dianggap tidak memenuhi syarat).

Apabila Anda tidak menemukan dan memperbaiki 20 pesan bermasalah dalam
repositori terdaftar pertama Anda, Anda dapat memilih repositori lain
di halaman wiki Anda, dan mengulanginya hingga Anda berhasil memperbaiki 20 pesan.

#### Contoh

[Contoh tugas](https://wikimedia-id.github.io/besutkode/university-sample-task-1-en.html) 
ini memiliki latar belakang tentang proyek penerjemahan phpMyAdmin.

Peserta yang menyelesaikan contoh tugas ini dapat dilihat di 
[`id.po`](https://github.com/phpmyadmin/localized_docs/commits/master/po/id.po).

Contoh-contoh perbaikan perbaikan kecil juga dapat dilihat di sana, seperti: 

- https://github.com/phpmyadmin/localized_docs/commit/9cc7914fe0ddc8caa90ca5da32150442de2561e4#diff-ef37f181f82218fc93bce3f96e620e4d
- https://github.com/phpmyadmin/localized_docs/commit/877c28f9f859a4806b1556764be697d0aab0501c#diff-ef37f181f82218fc93bce3f96e620e4d

Sebagai contoh, *Pull Request* yang harus berhasil Anda lakukan dalam tugas ini adalah 
[https://github.com/phpmyadmin/localized_docs/pull/2](https://github.com/phpmyadmin/localized_docs/pull/2).

### Temukan satu lagi *bug*

Buat atau perbaiki sebuah program bersumber terbuka, dalam bahasa 
pemrograman apapun, untuk mengenali sedikitnya satu *bug* 
penerjemahan dalam repositori tersebut.

Masalah yang terdeteksi itu harus tidak dapat ditemukan oleh peralatan yang ada.

Apabila Anda mengubah sebuah program yang sudah ada, Anda tidak diwajibkan
untuk mengirimkan perbaikan yang Anda buat kepada pengelola program tersebut.
Ini dapat menjadi sebuah proses pekerjaan.

Apabila program Anda hanya berupa skrip kecil, Anda dapat mengirimkannya 
sebagai *pull request* ke dalam subdirektori repositori BesutKode yang
dinamai menurut nama pengguna GitHub Anda.

Tambahkan penjelasan ringkas mengenai alat baru Anda ke halaman wiki Anda.

## Penilaian 

Setelah Anda rasa Anda telah selesai, buat sebuah issue pada repo BesutKode
dan tugaskan (*assign*) kepada @jayvdb.

Judul dari *issue* Anda harus merujuk pada nama pengguna GitHub Anda, 
dan isi *issue* Anda harus merujuk pada halaman wiki repo Anda. 

Peringatan: JANGAN SEKALIPUN menyertakan pranala (*link*) ke sebuah
*issue* atau *pull request* dari repositori lain. 

Secara baku, tugas akan dinilai dengan meninjau *pull request* yang 
sudah digabungkan ke berkas terjemahan pada profil GitHub Anda. 

Sebagai contohnya, pencarian kueri GitHub berikut ini digunakan: 

> author:<username> is:pr is:merged created:>2016-10-19

Penilaian akan menghitung seluruh pesan yang dimodifikasi,
dan secara manual akan memeriksa apakah sintaks sebelumnya memiliki kesalahan,
dan telah dibetulkan melalui kiriman (*commit*) yang Anda lakukan,
tanpa membuat kesalahan sintaks yang baru. 

Jika, dan hanya jika, pesan sintaks yang sebelumnya salah, terjemahan 
pesannya dapat Anda perbaiki apabila anda *mengetahui* bahasa pesannya. 

Selain itu, jenis kesalahan yang diperbaiki melalui *pull request* bisa 
diangkat seluruhnya dari repo, kecuali *pull request* secara eksplisit 
menyatakan mengapa sejumlah kejadian '*error*' tidak diperbaiki. 

## Tag StackOverflow terkait

- [translate-toolkit](http://stackoverflow.com/questions/tagged/translate-toolkit) 
- [weblate](http://stackoverflow.com/questions/tagged/weblate)
- [gettext](http://stackoverflow.com/questions/tagged/gettext)
- [reStructuredText](http://stackoverflow.com/questions/tagged/reStructuredText)
