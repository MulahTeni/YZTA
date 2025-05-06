# Sınav Sonucu Analizi ve Çalışma Planı Uygulaması (Gemini API ile) - GRUP 63

Bu proje, öğrencilerin sınav sonuçlarını analiz eden ve onlara çalışma planı sunan bir yapay zeka destekli Gradio uygulamasıdır. Google Gemini API'si kullanılarak, yüklenen görsellerden ve yazılı sorulardan anlam çıkarılmakta ve kişiye özgü tavsiyeler sunulmaktadır. Google Yapay Zeka Teknoloji Akademisi Hackathon için Grup 63 tarafından hazırlanmıştır.

---

## 📂 Proje Dosya Yapısı

```bash
.
├── main.py                 # Ana Python dosyası (Gradio arayüzü ve Gemini API entegrasyonu)
├── requirements.txt       # Gerekli Python kütüphaneleri
└── README.md              # Bu doküman
```

---

## ✨ Özellikler

- Kullanıcıdan sınav sonucu görseli ve soru alarak analiz yapar
- Gemini 2.0 Flash modeli ile çıktı verir
- Tarihçe tutarak sohbet geçmişine dayalı yanıtlar üretir
- Öğrenciye özel bir çalışma planı sunar
- Modern ve eğitime uygun Gradio arayüz tasarımı

---

## 🚀 Kurulum

### 1. Depoyu klonlayın

```bash
git clone https://github.com/kullaniciadi/YZTA.git
cd YZTA
```

### 2. Sanal ortam (isteğe bağlı)

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Gerekli kütüphaneleri yükleyin

```bash
pip install -r requirements.txt
```

---

## 🔑 API Anahtarı Ayarlama

Bu uygulama, Google Gemini API'yi kullanmaktadır. Bu nedenle bir API anahtarına ihtiyacınız var.

1. [Google AI Studio](https://makersuite.google.com/app) sitesinden hesabınızla girin.
2. Bir API anahtarı oluşturun.
3. `main.py` dosyasını açın ve şu satırı bulup anahtarınızı girin:

```python
GEMINI_API_KEY = ""  # Buraya kendi API anahtarınızı yazın
```

Not: Anahtar boş bırakıldıysa uygulama içinde kutudan girmeniz gerekir.

---

## 🚪 Çalıştırma

Projeyi başlatmak için:

```bash
python main.py
```

Arayüz otomatik olarak açılacak ya da terminalde verilen URL'den ulaşabilirsiniz.

---

## 🔹 requirements.txt

```txt
gradio
Pillow
google-generativeai
```

---

## 🌍 Erişimi Paylaşma

Uygulama başladığında `share=True` ayarı sayesinde genel bir link ile başkalarıyla paylaşabilirsiniz.

---

## 🌟 Katkıda Bulun

Pull request'ler ve feature talepleri hoşgörülüdür.

---

## 📄 Lisans

MIT Lisansı

---

