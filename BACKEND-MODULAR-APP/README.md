# Backend Modular API

## Identitas
- Institusi: STIKOM PGRI Banyuwangi
- Mata Kuliah: Dasar Pemrograman Backend (KK112105)
- Praktikum: Pertemuan 5
- Topik: REST API Design dan Response Standardization
- Versi API: v1

## Deskripsi
REST API untuk mengelola kategori dan produk. Setiap produk memiliki
`category_id` yang mengacu pada kategori yang tersedia.

## Base URL
`http://127.0.0.1:5000/api/v1`

## Endpoint Categories
| Method | URI | Fungsi |
|---|---|---|
| GET | `/categories` | Daftar kategori |
| GET | `/categories/{id}` | Detail kategori |
| POST | `/categories` | Membuat kategori |
| PUT | `/categories/{id}` | Memperbarui kategori |
| DELETE | `/categories/{id}` | Menghapus kategori |
| GET | `/categories/{id}/products` | Produk dalam kategori |

## Endpoint Products
| Method | URI | Fungsi |
|---|---|---|
| GET | `/products` | Daftar produk |
| GET | `/products?category_id=1` | Filter berdasarkan kategori |
| GET | `/products/{id}` | Detail produk |
| POST | `/products` | Membuat produk |
| PUT | `/products/{id}` | Memperbarui produk |
| DELETE | `/products/{id}` | Menghapus produk |

## Contoh JSON produk
```json
{
  "name": "Mouse Wireless",
  "price": 250000,
  "stock": 10,
  "category_id": 2
}
```

## Standarisasi respons
- `success`: permintaan berhasil, menggunakan `data`.
- `fail`: kesalahan input atau permintaan, menggunakan `errors`.
- `error`: kesalahan internal server, menggunakan `message`.

## Validasi produk
- `name` wajib berupa teks yang tidak kosong.
- `price` harus berupa angka lebih besar dari 0.
- `stock` harus berupa bilangan bulat minimal 0.
- `category_id` harus mengacu pada kategori yang tersedia.
- Request yang mengirim body harus memakai `Content-Type: application/json`.

## Arsitektur
Client -> Blueprint Route -> Service -> Repository

Helper respons berada di `app/utils/response_helper.py` dan digunakan
untuk menyeragamkan respons endpoint.

## Cara menjalankan
1. Buat virtual environment: `python -m venv venv`
2. Aktifkan di PowerShell: `.\venv\Scripts\Activate.ps1`
3. Instal dependensi: `python -m pip install -r requirements.txt`
4. Jalankan: `python run.py`
5. Uji API melalui Postman atau PowerShell.

## Penyimpanan
Data contoh disimpan di memori Python, bukan database permanen.
Data kembali ke contoh awal ketika server dimulai ulang.
