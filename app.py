import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Judul dashboard
st.header("Kampus Jaya")
st.subheader("by Bayun Kurniawan")

# Membaca data dengan delimiter ';'
jaya_df = pd.read_csv("data.csv", delimiter=';')
jaya_df.columns = jaya_df.columns.str.strip()  # Bersihkan spasi

# Tampilkan total mahasiswa
st.subheader("Total Mahasiswa")
st.metric("Jumlah", len(jaya_df))

# Debug (opsional): tampilkan nama kolom
# st.write("Kolom tersedia:", jaya_df.columns.tolist())

# Hitung jumlah per status
if 'Status' in jaya_df.columns:
    status_counts = jaya_df['Status'].value_counts().reset_index()
    status_counts.columns = ['Status', 'Jumlah']

    # Tampilkan grafik
    st.subheader("Jumlah Mahasiswa per Status")
    fig = plt.figure(figsize=(8, 4))
    sns.barplot(x='Status', y='Jumlah', data=status_counts)
    st.pyplot(fig)
else:
    st.error("Kolom 'Status' tidak ditemukan! Periksa file CSV.")
    
scholarship_counts = jaya_df['Scholarship_holder'].value_counts().reset_index()
scholarship_counts.columns = ['Scholarship_holder', 'Jumlah']
scholarship_counts['Status'] = scholarship_counts['Scholarship_holder'].map({
    1: 'Mendapat Beasiswa',
    0: 'Tidak Mendapat Beasiswa'
})

st.subheader("Jumlah Mahasiswa Berdasarkan Beasiswa")
fig = plt.figure(figsize=(6, 4))
sns.barplot(x='Status', y='Jumlah', data=scholarship_counts)
st.pyplot(fig)

bins = [15, 20, 25, 30, 35, 40, 100]
labels = ['16-20', '21-25', '26-30', '31-35', '36-40', '41+']
jaya_df['Kelompok_Umur'] = pd.cut(jaya_df['Age_at_enrollment'], bins=bins, labels=labels)

umur_counts = jaya_df['Kelompok_Umur'].value_counts().sort_index().reset_index()
umur_counts.columns = ['Usia', 'Jumlah']

st.subheader("Jumlah Mahasiswa Berdasarkan Umur")

fig = plt.figure(figsize=(8, 4))
sns.barplot(x='Usia', y='Jumlah', data=umur_counts)
plt.xticks(rotation=45)
st.pyplot(fig)
