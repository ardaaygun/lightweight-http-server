import socket
import os
import re
from datetime import datetime

# Sunucu yapılandırma ayarları
HOST = '127.0.0.1'
PORT = 8080


def markdown_to_html(md_text):
    """
    Markdown formatındaki düz metni Regex kullanarak
    dinamik olarak HTML etiketlerine dönüştürür.
    """
    html = md_text
    html = re.sub(r'^# (.*)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', html)
    html = re.sub(r'^- (.*)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    return html


# 1. Soket Kurulumu ve Bağlantı Ayarları
# IPv4 (AF_INET) ve TCP (SOCK_STREAM) protokollerini kullanarak soket oluştur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Portun işletim sistemi tarafından askıda kalmasını (Address already in use) önlemek için REUSEADDR ayarı
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Soketi belirlenen IP adresi ve porta bağla
server_socket.bind((HOST, PORT))

# Maksimum 5 bağlantıyı kuyruğa alarak dinlemeye başla
server_socket.listen(5)

print("===================================================")
print("🚀 CMPE 322 - Dinamik HTTP ve Markdown Sunucusu")
print(f"📡 Adres: http://{HOST}:{PORT}")
print("🛑 Kapatmak için: CTRL+C")
print("===================================================\n")

try:
    while True:
        # 2. İstemci (Client) Bağlantısını Kabul Etme
        client_connection, client_address = server_socket.accept()

        # Gelen byte verisini UTF-8 olarak metne çevir (decode)
        request = client_connection.recv(1024).decode('utf-8')

        # Boş istekleri (örn. tarayıcı pingleri) yoksay
        if not request:
            client_connection.close()
            continue

        # 3. HTTP GET İsteğini Ayrıştırma (Manual Parsing)
        # İsteğin sadece ilk satırını al (Örn: "GET /week1.md HTTP/1.1")
        first_line = request.split('\n')[0]

        # İlk satırı boşluklardan ayırıp istenen dosya yolunu elde et
        parts = first_line.split(' ')
        path = parts[1] if len(parts) > 1 else "/"

        # Tarayıcıların otomatik favicon isteklerini atla
        if "favicon.ico" in path:
            client_connection.close()
            continue

        now = datetime.now().strftime("%H:%M:%S")
        client_ip = client_address[0]

        print(f"[{now}] 🟢 BAĞLANTI   : {client_ip} adresinden bağlandı.")
        print(f"[{now}] 📥 HAM İSTEK  : {first_line}")
        print(f"[{now}] 🔍 PARÇALAMA  : HTTP GET isteği ayrıştırılıyor...")

        # Kök dizin isteğini varsayılan olarak index.html'e yönlendir
        if path == "/":
            path = "/index.html"

        # İşletim sisteminde aramak için baştaki '/' karakterini temizle
        filepath = path.lstrip('/')

        print(f"[{now}] 📂 HEDEF      : '{filepath}' dosyası talep ediliyor.")
        print(f"[{now}] 💾 HARD DİSK  : Dosya sistemi üzerinde aranıyor...")

        # 4. Dosya Kontrolü ve Yanıt (Response) Hazırlama
        if os.path.exists(filepath):
            print(f"[{now}] ✅ BULUNDU    : Dosya mevcut, okuma işlemi başlıyor.")

            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            # Dinamik Markdown Dönüşümü İşlemi
            if filepath.endswith('.md'):
                print(f"[{now}] ⚙️ DÖNÜŞÜM    : Markdown formatı algılandı, HTML'e çevriliyor.")
                parsed_html = markdown_to_html(content)

                # CSS şablonu ile çevrilen metnin birleştirilmesi
                final_content = f"""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>CMPE 322 Notes</title>
                    <style>
                        body {{ font-family: 'Segoe UI', sans-serif; background-color: #1e1e2f; color: #c8c8d4; display: flex; justify-content: center; padding: 40px; }}
                        .container {{ background-color: #2a2a40; padding: 40px; border-radius: 12px; box-shadow: 0 8px 24px rgba(0,0,0,0.6); width: 100%; max-width: 800px; }}
                        h1 {{ color: #00d2ff; border-bottom: 2px solid #44475a; padding-bottom: 10px; }}
                        h2 {{ color: #ff79c6; margin-top: 30px; }}
                        b {{ color: #f1fa8c; }}
                        li {{ margin-bottom: 10px; line-height: 1.6; font-size: 1.1em; }}
                        a {{ color: #8be9fd; text-decoration: none; margin-bottom: 20px; display: inline-block; }}
                        a:hover {{ text-decoration: underline; }}
                    </style>
                </head>
                <body>
                    <div class="container">
                        <a href="/">&larr; Ana Sayfaya Don</a>
                        {parsed_html}
                    </div>
                </body>
                </html>
                """
                content_type = "text/html; charset=UTF-8"

            # Standart HTML dosyası
            elif filepath.endswith('.html'):
                final_content = content
                content_type = "text/html; charset=UTF-8"

            # Diğer dosyalar için düz metin
            else:
                final_content = content
                content_type = "text/plain; charset=UTF-8"

            # Başarılı (200 OK) HTTP Yanıtı Oluşturma
            # HTTP protokolü gereği Header ile Body arasında \r\n\r\n bulunmalıdır.
            response = "HTTP/1.1 200 OK\r\n"
            response += f"Content-Type: {content_type}\r\n\r\n"
            response += final_content

            print(f"[{now}] 📦 PAKETLEME  : HTTP Response hazırlandı.")
            print(f"[{now}] 📤 YANIT      : 200 OK -> İletildi.")

        else:
            # Dosya bulunamadı durumu (404 Not Found)
            print(f"[{now}] ❌ BULUNAMADI : '{filepath}' diskte bulunamadı.")

            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type: text/html; charset=UTF-8\r\n\r\n"
            response += "<html><body style='text-align:center; padding:50px; background-color:#1e1e2f; color:white;'><h1>404 Hata</h1><p>Sayfa bulunamadi!</p><a href='/' style='color:#00d2ff;'>Ana Sayfaya Don</a></body></html>"
            print(f"[{now}] 📤 YANIT      : 404 Not Found -> İletildi.")

        # 5. İletişim ve Kapanış
        # Yanıtı byte formatına çevirip (encode) ağ üzerinden gönder
        client_connection.sendall(response.encode('utf-8'))

        # HTTP protokolü durumsuz (stateless) olduğu için işlemi biten bağlantıyı kapat
        client_connection.close()
        print("-" * 75)

except KeyboardInterrupt:
    # CTRL+C ile terminalden manuel güvenli çıkış
    print("\n[!] Sunucu güvenli bir şekilde kapatılıyor...")
    server_socket.close()