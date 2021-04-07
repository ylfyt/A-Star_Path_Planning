# A-Star_Path_Planning


##Hal-hal yang perlu diinstall untuk bisa menjalankan program:
- Python 3.9.0
- tkinter
- folium

##Format File Test (.txt)
- Terdapat 2 file yang harus dibuat
- File pertama
  1. Setiap baris harus diakhiri dengan tanda koma "," 
  2. Pada baris pertama merupakan skala dari map yang digunakan untuk mendapatkan koordinat
      - Jika koordinat didapatkan dari api map, maka secara default skalanya adalah 100000
      - Jika koordinat tidak berdasarkan map tertentu, maka skalanya adalah 1
  3. Pada baris kedua merupakan jumlah dari node/simpul pada graph
  4. Jika banyak simpul adalah N, maka N baris selanjutnya adalah koordinat dan nama simpulnya dengan dipisahkan koma ","
  5. Contoh isi file .txt
     - 100000,
     - 3,
     - 9,100,Node1,
     - 9,102,Node2,
     - 7,99,Node3,

- File kedua
  1. File kedua merupakan matriks adjancency dari graph pada file pertama
  2. Nama dari file kedua harus mengikuti nama dari file kedua, dengan ditambakan "_adj". Contoh jika file pertama bernama "01.txt", maka nama file kedua adalah "01_adj.txt".
  3. Harus terdapat matrix adjacency dengan ukuran NxN, dan setiap baris harus diakhiri dengan koma ","
  4. Contoh isi file kedua jika banyak node adalah 4
    - 0,0,0,1,
    - 0,0,1,0,
    - 0,1,0,0,
    - 1,0,0,0,

#Cara run program wajib:
1. Masuk ke folder src
2. ketik "python app.py" pada terminal
3. Program akan berjalan
5. Pilih file eksternal dengan mengeklik tombol "Browse", lalu pilihlah *File Pertama* jangan file kedua.
6. Pilih node awal dan node akhir
7. Tekan tombol "Search"
8. Visualisasi jalur terpendek akan ditampilkan
9. Selesai


#Cara run program bonus:
1. Masuk ke folder src
2. ketik "python map.py" pada terminal
3. Masukkan node awal dan node akhir yang diinginkan pada terminal
4. pada terminal akan ditampilkan urutan pencariann jalur terpendek
5. untuk visualisasi, setelah program berhasil akan terdapat file "map.html" pada folder src
6. Buka file "map.html" tersebut
7. Visualisasi jalur terpendek akan ditampilkan
8. Selesai

