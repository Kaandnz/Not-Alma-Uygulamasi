import sqlite3

def create_table():
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS notlar (id INTEGER PRIMARY KEY, baslik TEXT, icerik TEXT)')
    conn.commit()
    conn.close()

def notlari_goruntule():
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM notlar')
    notlar = cursor.fetchall()
    for not_ in notlar:
        print(f'ID: {not_[0]}, Başlık: {not_[1]}, İçerik: {not_[2]}')
    conn.close()

def yeni_not_ekle(baslik, icerik):
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO notlar (baslik, icerik) VALUES (?, ?)', (baslik, icerik))
    conn.commit()
    conn.close()

def not_guncelle(id, baslik, icerik):
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE notlar SET baslik = ?, icerik = ? WHERE id = ?', (baslik, icerik, id))
    conn.commit()
    conn.close()

def not_sil(id):
    conn = sqlite3.connect('notlar.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM notlar WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def menu():
    while True:
        secim = input('Lütfen yapmak istediğiniz işlemi seçin: \n1- Notları Görüntüle\n2- Yeni Not Ekle\n3- Not Güncelle\n4- Not Sil\n5- Çıkış\n')
        if secim == '1':
            notlari_goruntule()
        elif secim == '2':
            baslik = input('Lütfen not başlığını girin: ')
            icerik = input('Lütfen not içeriğini girin: ')
            yeni_not_ekle(baslik, icerik)
        elif secim == '3':
            id = input('Lütfen güncellemek istediğiniz notun ID numarasını girin: ')
            baslik = input('Lütfen yeni başlığı girin: ')
            icerik = input('Lütfen yeni içeriği girin: ')
            not_guncelle(id, baslik, icerik)
        elif secim == '4':
            id = input('Lütfen silmek istediğiniz notun ID numarasını girin: ')
            not_sil(id)
        elif secim == '5':
            print('Not alma uygulamasından çıkış yapılıyor...')
            break
        else:
            print('Hatalı bir seçim yaptınız. Lütfen tekrar deneyin.')

if __name__ == '__main__':
    create_table()
    menu()
