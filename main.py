# -*- coding: utf-8 -*-
"""AKA_Tubes_Pengurutan tim liga inggris.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/16DBwP24A-FmBE3Zxd4HHnLnRElow3Fl9

**Pengurutan Tim Liga Inggris Berdasarkan Jumlah Gelar juara premier league dengan pendekatan itteratif dan rekursif**
"""

import time
import random
import matplotlib.pyplot as plt

from prettytable import PrettyTable
from enum import auto, Enum

n_list = []
recursive_time_list = []
iterative_time_list = []

class JenisSort(Enum):
  """
  Membuat enum untuk menentukan jenis algoritma sorting yang akan digunakan
  sehingga program dapat menentukan jenis algoritma sorting yang akan digunakan
  @param ITERATIF: algoritma sorting dengan pendekatan iteratif
  @param REKURSIF: algoritma sorting dengan pendekatan rekursif
  """

  ITERATIF = auto()
  REKURSIF = auto()

def create_graph():
  """
  Membuat fungsi untuk membuat grafik dari data yang diberikan
  dengan menggunakan library matplotlib untuk visualisasi data
  performa algoritma sorting dari merge dan bubble sort
  """

  plt.figure(figsize=(8, 6))
  plt.plot(n_list, recursive_time_list, label='Rekursif', marker='o', linestyle='-')
  plt.plot(n_list, iterative_time_list, label='Iteratif', marker='o', linestyle='-')
  plt.title('Grafik Performa Antara Rekursif dan Iteratif')
  plt.xlabel('Input (n)')
  plt.ylabel('Waktu Eksekusi (seconds)')
  plt.legend()
  plt.grid(True)
  plt.show()

def create_table():
  """
  Prosedur untuk membuat tabel dari data yang diberikan
  dengan menggunakan library prettytable untuk visualisasi data
  Waktu eksekusi dari algoritma sorting dari merge dan bubble sort
  """

  # Inisialisasi table dari fungsi construct pada library PrettyTable
  table = PrettyTable()

  # Mengisi header dari table sehingga lebih informatif
  table.field_names = ["n", "Waktu Rekursif (s)", "Waktu Iteratif (s)"]

  # mencari jumlah list terkecil dari list input, rekursif, dan iteratif
  # sehingga proses mencetak table tidak terjadi bug atau error
  min_len = min(len(n_list), len(recursive_time_list), len(iterative_time_list))

  # Melakukan perulangan dari 0 hingga n, dimana n adalah jumlah minimal
  # yang sudah ditentukan
  for i in range(min_len):
    # menambahkan baris dari nilai yang berada pada indeks ke i, dimana
    # nilai dari i didapat dari nilai perulangan yang dilakukan
    table.add_row([n_list[i], recursive_time_list[i], iterative_time_list[i]])

  # Mencetak table yang sudah dibuat
  print(table)

def bubble_sort(teams):
  """
  Membuat fungsi sorting dengan pendekatan iteratif menggunakan metode bubble sort
  @param teams: list team yang akan diurutkan
  @return: list team yang telah diurutkan
  """

  # N = jumlah data dari list yang diberikan
  # dimana data N akan menjadi batas iterasi luar
  n = len(teams)

  # Melakukan pengecekan apakah nilai N bernilai 0 atau kosong
  # jika data teams kosong, maka kembalikan nilai list kosong
  if n == 0:
    return teams

  # Pada iterasi luar, kita akan melakukan perulangan
  # sebanyak N kali yaitu jumlah elemen pada list team
  for x in range(n):
    # Pada iterasi dalam, kita akan melakukan perulangan
    # dari 0 hingga n - x - 1, dengan kata lain pada iterasi
    # pertama berjalan sebanyak n - 1 kali karena x bernilai 0
    for y in range(0, n-x-1):
      # Pada tahap ini, kita akan melakukan operasi dasar yaitu
      # perbandingan, dimana ketika nilai pada indeks ke y kurang dari
      # nilai pada indeks ke y + 1 maka program akan melakukan aksi yang
      # sudah diberikan karena syarat berhasil terpenuhi atau bernilai benar
      if teams[y][1] < teams[y+1][1]:
        # Ketika syarat pada kondisi terpenuhi, selanjutnya kita akan melakukan
        # operasi dasar penukaran nilai, dimana nilai pada indeks ke y dan nilai
        # indeks ke y + 1 akan ditukar sehingga menghasilkan list yang terurut
        # membesar dengan perumpamaan i > j && j > k && ... && x > n
        teams[y], teams[y+1] = teams[y+1], teams[y]

  # Setelah proses pengurutan selesai, selanjutnya kita akan
  # mengembalikan list data yang sudah terurut membesar
  return teams

def merge_sort(teams):
  """
  Membuat fungsi sorting dengan pendekatan rekursif menggunakan metode merge sort
  @param teams: list team yang akan diurutkan
  @return: list team yang telah diurutkan
  """

  # Menghitung panjang nilai dari teams agar menghindari
  # perulangan kode dan lebih mudah untuk digunakan
  length = len(teams)

  # Melakukan pengecekan apakah nilai length bernilai 0 atau kosong
  # jika data teams kosong, maka kembalikan nilai list kosong
  if length <= 1:
    return teams

  # Mencari indeks tengah dari list yang diberikan
  # dengan perumpamaan panjang list dibagi 2
  mid = length // 2

  # Menentukan list berdasarkan nilai tengah yang kita bagi
  # menjadi 2 bagian yaitu bagian kiri dan bagian kanan
  left_half = teams[:mid]
  right_half = teams[mid:]

  # Menjalankan pendekatan rekursif,
  # sehingga data dari setiap bagian menjadi urut membesar
  merge_sort(left_half)
  merge_sort(right_half)

  # Deklarasi variable i, j, dan k
  # dimana semua variable di berikan nilai 0
  i = j = k = 0

  # Melakukan iterasi dimana akan terus berjalan hingga
  # kondisi nilai i dan j kurang dari panjang nilai left dan right
  while i < len(left_half) and j < len(right_half):
    if left_half[i][1] > right_half[j][1]:
      teams[k] = left_half[i]
      i += 1
    else:
      teams[k] = right_half[j]
      j += 1
    k += 1

  while i < len(left_half):
    teams[k] = left_half[i]
    i += 1
    k += 1

  while j < len(right_half):
    teams[k] = right_half[j]
    j += 1
    k += 1

  return teams

def calculate_time(sort_type, teams):
  """
  Membuat fungsi untuk menghitung waktu eksekusi dari algoritma sorting
  @param sort_type: jenis algoritma sorting yang akan digunakan
  @param teams: list team yang akan diurutkan
  """

  start_time = time.time()

  if sort_type == JenisSort.ITERATIF:
    bubble_sort(teams)
    end_time = time.time()
    iterative_time_list.append(round(end_time - start_time, 6))
  elif sort_type == JenisSort.REKURSIF:
    merge_sort(teams)
    end_time = time.time()
    recursive_time_list.append(round(end_time - start_time, 6))
  else:
    print("Jenis algoritma sorting tidak valid")

def generate_random_teams(n):
  """
  Membuat fungsi untuk membuat list team secara acak
  @param n: jumlah team yang akan dibuat
  @return teams: list team yang telah dibuat
  """

  teams = []

  for i in range(0, n):
    name = f"Team {i+1}"
    points = random.randint(0, 30)
    teams.append((name, points))

  return teams

while True:
  try:
    n = int(input("Masukan nilai n (masukan '-1' untuk keluar): "))

    if n == -1:
      print("Program berhenti, sampai jumpa!")
      break
    elif n < 0:
      print("Nilai yang diberikan harus bernilai positif, silahkan coba lagi")
      continue

    n_list.append(n)
    teams = generate_random_teams(n)

    calculate_time(JenisSort.ITERATIF, teams)
    calculate_time(JenisSort.REKURSIF, teams)

    create_table()
    create_graph()
  except ValueError as e:
    print("Something went wrong", e)