import gradio as gr
import google.generativeai as genai
from PIL import Image
import os

# API anahtarını doğrudan koda yazıyoruz
GEMINI_API_KEY = ""  # Buraya kendi API anahtarınızı yazın
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

instruction = """
Sen bir eğitim danışmanısın. Öğrencilerin sınav sonuçlarını değerlendiriyorsun. Öğrencinin sınavdan aldığı puanları ve cevaplarını dikkate alarak, hangi konularda eksik olduklarını ve hangi alanlarda daha fazla çalışmaları gerektiği konusunda tavsiyelerde bulunuyorsun. Ayrıca, öğrenciye uygun bir çalışma planı öneriyorsun.
"""
history = ""
hisn = 0

def analyze_image(image, soru, api_key):
    global history
    global hisn
    global GEMINI_API_KEY

    # API anahtarını kontrol et ve yapılandır
    if GEMINI_API_KEY != api_key:
        GEMINI_API_KEY = api_key
        genai.configure(api_key=GEMINI_API_KEY)

    # Görseli numpy dizisine çevir
    pil_image = Image.fromarray(image)
    pil_image = pil_image.convert("RGB")  # Görseli RGB formatına çevir

    # Geçmişi özetle (isteğe bağlı)
    if hisn > 3:
        history = model.generate_content("Yazacağım metni özetle, kısalt ve sadece gereken önemli yerleri al ve metin formatını değiştirme. Metin şu: " + history).text

    # Soruyu ve görseli işleme
    history += f"user: {soru}\n"
    
    if image is None:
        response = model.generate_content(instruction + history)
        history += f"AI: {response.text}\n"
    else:
        try:
            response = model.generate_content([instruction + history, pil_image])
            history += f"AI: {response.text}\n"
        except Exception as e:
            print(f"Hata oluştu: {e}")
            return "Bir hata oluştu, lütfen tekrar deneyin."

    # Durum bilgisi
    hisn += 1
    print(history)
    return response.text.replace("*", "")

# Özel CSS stilleri
theme_css = """
    /* Ana container stil */
    .gradio-container {
        background: #F4F9FF;  /* Açık mavi arka plan */
        border-radius: 15px;
        padding: 40px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.1);
        font-family: 'Arial', sans-serif;
    }
    
    /* Başlık stil */
    .gr-title {
        color: #1E4E8C;  /* Eğitimle ilişkili mavi renk */
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Düğme stil */
    .gr-button {
        background: #FF8C00;  /* Canlı turuncu renk */
        color: white;
        font-weight: bold;
        padding: 14px 30px;
        border-radius: 10px;
        transition: background-color 0.3s ease;
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1);
    }
    
    /* Düğme üzerine geldiğinde renk değişimi */
    .gr-button:hover {
        background: #FF6A00;  /* Daha koyu turuncu */
        transform: scale(1.05);
    }
    
    /* Giriş kutusu ve metin kutusu stil */
    .gr-input {
        background: #FFFFFF;  /* Beyaz arka plan */
        border-radius: 10px;
        border: 1px solid #D1D8E0;
        padding: 15px;
        font-size: 16px;
    }
    
    /* Çalışma planı ve analiz sonucu kutusu */
    .gr-textbox {
        background: #F1F6FF;  /* Açık mavi ton */
        border: 1px solid #C0D5E8;
        padding: 20px;
        border-radius: 10px;
        font-size: 16px;
        height: 400px;  /* Yüksekliği artırdık */
        resize: none;
        overflow-y: auto;  /* Uzun metinler için kaydırma ekledik */
    }

    /* Görsel yükleme kutusu */
    .gr-image {
        background: #E4F3FF;  /* Hafif mavi arka plan */
        border-radius: 10px;
        padding: 20px;
        border: 2px dashed #1E4E8C;
    }

    /* Genel yatay düzenleme */
    .gr-row {
        margin-bottom: 15px;
    }
    
    /* Başlık ve alt başlıklar */
    .gr-markdown h1 {
        color: #1E4E8C;
    }
    
    /* Alt başlık stil */
    .gr-markdown h2 {
        color: #3C5A8B;
    }
"""

# Gradio Arayüzü
with gr.Blocks(css=theme_css, theme=gr.themes.Soft()) as demo:
    gr.Markdown("""
        <h1 class='gr-title'>🎓 Sınav Sonuçları Analiz ve Çalışma Planı</h1>
        <hr>
    """, elem_id='header')
    
    with gr.Row():
        api_key = gr.Textbox(value=GEMINI_API_KEY, label="API Anahtarınız", placeholder="API anahtarınızı buraya yazın", elem_classes="gr-input", interactive=False)
    
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(type="numpy", label="📸 Sınav Sonucunuzu Yükleyin (Görsel)", elem_classes="gr-image")
        with gr.Column():
            result_output = gr.Textbox(label="📋 Analiz Sonucu ve Çalışma Planı", lines=15, interactive=False, elem_classes="gr-textbox")  # lines parametresi artırıldı
        
    with gr.Row():
        soru_input = gr.Textbox(label="💬 Sınav Sonucunuz Hakkında Sormak İstediğiniz Bir Şey", placeholder="Örnek: Bu sınav sonucum hakkında ne düşünüyorsunuz? Çalışma planım nasıl olmalı?", elem_classes="gr-input")
        
    with gr.Row():
        analyze_btn = gr.Button("🔍 Sonuçları Analiz Et ve Çalışma Planı Oluştur", elem_classes="gr-button")
        
    analyze_btn.click(fn=analyze_image, inputs=[image_input, soru_input, api_key], outputs=result_output)

if __name__ == "__main__":
    demo.launch(share=True)
