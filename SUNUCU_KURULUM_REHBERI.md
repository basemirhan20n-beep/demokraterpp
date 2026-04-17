# SUNUCU KURULUM REHBERİ

## Giriş
Bu belge, Discord/Telegram tarzı sunucu ve alt kanal yönetim sistemi için kurulum ve kullanım kılavuzunu içermektedir. 

## Kurulum Adımları

### 1. Gereksinimler
- Node.js (v14 veya üstü)
- npm (Node Package Manager)

### 2. Projeyi İndirin
Aşağıdaki komutları kullanarak projeyi indirin:
```bash
git clone https://github.com/owner/demokraterpp.git
cd demokraterpp
```

### 3. Bağımlılıkları Yükleyin
Proje dizininde, gerekli bağımlılıkları yüklemek için:
```bash
npm install
```

### 4. Ayarları Yapılandırın
`config.json` dosyasını düzenleyin ve gerekli ayarları yapılandırın:
```json
{
  "token": "YOUR_BOT_TOKEN",
  "prefix": "!"
}
```

### 5. Botu Başlatın
Botu başlatmak için:
```bash
node index.js
```

## Kullanım

### Komutlar
- `!create [channel_name]`: Yeni bir kanal oluşturur.
- `!delete [channel_name]`: Mevcut bir kanalı siler.
- `!list`: Mevcut kanalları listeler.

### Örnek Kullanım
Bir kanal oluşturmak için:
```bash
!create oyun-kanali
```

## Sonuç
Bu rehber, sunucunuzda Discord/Telegram tarzı bir yapılandırma oluşturmanıza yardımcı olacaktır. Herhangi bir sorun veya yardım gerektiğinde iletişime geçmekten çekinmeyin.