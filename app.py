import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Quan ly diem sinh vien", layout="wide")
st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

# Du lieu 10 sinh vien theo bai Colab
data = {
    "Ho_ten": ["An", "Binh", "Chi", "Dung", "Ha",
               "Lan", "Minh", "Nam", "Phuc", "Trang"],
    "Chuyen_can": [8, 9, 7, 10, 8, 6, 9, 8, 7, 10],
    "Giua_ky": [7, 8, 6, 9, 8, 7, 9, 8, 7, 9],
    "Cuoi_ky": [8, 9, 7, 10, 8, 7, 10, 8, 8, 10]
}

df = pd.DataFrame(data)

# Tinh diem tong ket: 20% chuyen can, 30% giua ky, 50% cuoi ky
df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
)

# Xep loai theo dung nguong trong de bai
def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7:
        return "Kha"
    elif diem >= 5:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)

# 1. Hien thi bang diem
st.subheader("Bang diem sinh vien")
bang_hien_thi = df.rename(columns={
    "Ho_ten": "Ho ten",
    "Chuyen_can": "Chuyen can",
    "Giua_ky": "Giua ky",
    "Cuoi_ky": "Cuoi ky",
    "Tong_ket": "Tong ket",
    "Xep_loai": "Xep loai"
})
st.dataframe(bang_hien_thi, hide_index=True, use_container_width=True)

# 2. Thong ke
st.subheader("Thong ke ket qua hoc tap")
cot1, cot2, cot3, cot4 = st.columns(4)
cot1.metric("Diem trung binh lop", f"{df['Tong_ket'].mean():.2f}")
sv_cao_nhat = df.loc[df["Tong_ket"].idxmax()]
sv_thap_nhat = df.loc[df["Tong_ket"].idxmin()]
cot2.metric("Diem cao nhat", f"{sv_cao_nhat['Tong_ket']:.1f}")
cot3.metric("Diem thap nhat", f"{sv_thap_nhat['Tong_ket']:.1f}")
cot4.metric("So sinh vien dat (>= 5)", int((df["Tong_ket"] >= 5).sum()))
st.write(f"Sinh vien co diem cao nhat: **{sv_cao_nhat['Ho_ten']}** - {sv_cao_nhat['Tong_ket']:.1f}")
st.write(f"Sinh vien co diem thap nhat: **{sv_thap_nhat['Ho_ten']}** - {sv_thap_nhat['Tong_ket']:.1f}")

# 3. Selectbox chon sinh vien
st.subheader("Thong tin chi tiet sinh vien")
ten_sv = st.selectbox("Chon mot sinh vien:", df["Ho_ten"].tolist())
sv = df.loc[df["Ho_ten"] == ten_sv].iloc[0]
st.write(f"**Ho ten:** {sv['Ho_ten']}")
ct1, ct2, ct3, ct4, ct5 = st.columns(5)
ct1.metric("Chuyen can", f"{sv['Chuyen_can']:.1f}")
ct2.metric("Giua ky", f"{sv['Giua_ky']:.1f}")
ct3.metric("Cuoi ky", f"{sv['Cuoi_ky']:.1f}")
ct4.metric("Tong ket", f"{sv['Tong_ket']:.2f}")
ct5.metric("Xep loai", sv["Xep_loai"])

# 4. Bieu do cot bang Matplotlib
st.subheader("Bieu do cot diem tong ket cua 10 sinh vien")
fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Diem tong ket cua 10 sinh vien")
ax.set_xlabel("Ten sinh vien")
ax.set_ylabel("Diem tong ket")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", rotation=45)
fig.tight_layout()
st.pyplot(fig)
plt.close(fig)

# 5. Ho ten va MSSV nguoi tao o cuoi trang
st.markdown("---")
st.caption("Nguoi tao ung dung: Nguyen Ha Anh Duc | MSSV: 068208010628")
