# eFeS Api Dokümantasyonu
Summon Servisi eFeS mikroservisi Rest Api dokümantasyonudur. HTTP isteklerinde bulunabilirsiniz. 

## eFeS Mikroservisi Nedir?
eFeS Summon projesinin dosya sistemi yönetimini sağlayan ölçeklenebilir bir mikroservistir. GlusterFs ve Core mikroservisleri arasında güvenilir bağlantıyı sağlar.

### eFeS mikroservisinin görevleri:

- GlusterFs sistemini yönetmek. Gelen dosyaları aldığı bilgilere göre taşımak, silmek ve eklemek.
- GlusterFs sistemine kaydolmuş dosya birimlerini ve hiyerarşilerini göstermek, filtrelemek.
- İstenilen dosyanın GlusterFs üzerinde kayıtlı olup olmadığını incelemek.

## eFeS Api Nedir?

## Endpointler

### /version
#### GET


### /FileList
#### GET


### /FileList/[:uid:]/
#### GET

### /FileLink
#### GET


### /file/[:file_id:]/
#### GET

### /file/[:uid:]/
#### PUT

### /file/[:uid:]/[:file_id:]/
#### PUT

## Örnek Çıktılar

## Hatalar

## Kapanış
