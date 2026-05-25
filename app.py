import streamlit as st
from openai import OpenAI

# 1. Pengaturan Halaman
st.set_page_config(page_title="HookCraft AI - Viral Hook Generator", page_icon="🚀", layout="centered")

# --- SISTEM KEAMANAN (PASSWORD RAHASIA) ---
# Password telah diubah menjadi sesuai permintaanmu
PASSWORD_RAHASIA = "Sefilius18"

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

def check_password():
    if st.session_state["password_input"] == PASSWORD_RAHASIA:
        st.session_state["authenticated"] = True
    else:
        st.error("❌ Password salah! Silakan cek kembali file PDF dari Lynk.id Anda.")

# Tampilan halaman login jika belum memasukkan password yang benar
if not st.session_state["authenticated"]:
    st.title("🔒 Akses Terkunci - HookCraft AI")
    st.write("Silakan masukkan password akses yang Anda dapatkan setelah melakukan pembelian di Lynk.id.")
    st.text_input("Masukkan Password Akses:", type="password", key="password_input", on_change=check_password)
    st.stop() 
# ----------------------------------

# --- HALAMAN UTAMA APLIKASI (Terbuka jika password benar) ---
st.title("🚀 HookCraft AI")
st.subheader("Bikin 3 Detik Pertama Videomu Viral dalam Sekali Klik!")
st.write("Selamat datang! Gunakan alat ini untuk melejitkan views konten TikTok, Reels, dan Shorts Anda.")
st.markdown("---")

# Input Pengguna
topik = st.text_input("💡 Apa topik atau tema videomu?", placeholder="Contoh: Review skincare lokal, Tips hemat anak kos...")

gaya_bahasa = st.selectbox(
    "🗣️ Pilih Gaya Bahasa (Tone):",
    ["Anak Muda / Kasual", "Kontradiktif (Mematahkan Mitos)", "Memicu Rasa Penasaran (Kepo)", "Edukasi Santai"]
)

jumlah_hook = st.slider("📊 Mau berapa pilihan hook?", min_value=3, max_value=7, value=5)

# Kolom tempat pembeli memasukkan API Key milik mereka sendiri
api_key_input = st.text_input("🔑 Masukkan OpenAI API Key Anda:", type="password", help="Dapatkan API Key gratis di platform.openai.com")

st.markdown("---")

# Proses ketika tombol klik aktif
if st.button("✨ Hasilkan Hook Viral ✨"):
    if not api_key_input:
        st.error("Silakan masukkan OpenAI API Key Anda terlebih dahulu!")
    elif not topik:
        st.warning("Topik konten tidak boleh kosong!")
    else:
        with st.spinner("HookCraft AI sedang meracik hook terbaik... 🤔"):
            try:
                # Menghubungkan ke API OpenAI dinamis milik pembeli
                client = OpenAI(api_key=api_key_input)
                
                system_prompt = (
                    "Kamu adalah seorang psikolog konten dan copywriter viral terbaik di Indonesia untuk TikTok, Shorts, dan Reels. "
                    "Tugasmu adalah membuat pilihan Hook (3 detik pertama video) yang sangat memikat dan memaksa penonton berhenti scrolling. "
                    "Gunakan bahasa kasual Indonesia yang alami, tajam, gaul, dan hindari kata kaku. "
                    "Format output wajib rapi menggunakan penomoran Markdown."
                )
                
                user_prompt = f"Buatkan {jumlah_hook} pilihan hook video pendek dengan topik: '{topik}'. Gunakan gaya bahasa: '{gaya_bahasa}'."
                
                # Memanggil AI gpt-4o-mini yang super cepat
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": user_prompt}
                    ],
                    temperature=0.7
                )
                
                # Menampilkan Hasil
                st.success("🔥 Ini dia Hook Viral untuk Kontenmu:")
                st.markdown(response.choices[0].message.content)
                st.info("💡 Tips: Salin salah satu hook di atas, lalu jadikan sebagai kalimat pertama saat kamu take video!")
                
            except Exception as e:
                st.error(f"Terjadi kesalahan teknis. Pastikan API Key Anda benar dan memiliki saldo aktif. Detail: {e}")
