import pandas as pd

# 1. Baca file Excel mentah
df = pd.read_excel('data_kotor.xlsx')

# 2. Bersihkan data
df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
df = df.drop_duplicates()
df = df.dropna(subset=['nama_pasien'])

# 3. Buat rekap harian
rekap = df.groupby('tanggal').size().reset_index(name='total_kunjungan')

# 4. Simpan jadi laporan rapi
rekap.to_excel('laporan_bersih.xlsx', index=False)

print("Beres! Laporan rapi sudah dibuat.")
print(rekap)
