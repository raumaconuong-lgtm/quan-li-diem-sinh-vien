import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("QUAN LY DIEM SINH VIEN")

data = {
    "Ho_ten": ["An", "Binh", "Chi", "Dung", "Ha",
               "Lan", "Minh", "Nam", "Phuc", "Trang"],
    "Chuyen_can": [8, 7, 9, 6, 8, 9, 7, 8, 6, 10],
    "Giua_ky": [7, 8, 9, 6, 7, 8, 7, 9, 6, 9],
    "Cuoi_ky": [8, 7, 9, 7, 8, 9, 8, 8, 7, 10]
}

df = pd.DataFrame(data)
df.insert(0, "STT", range(1, 11))

df["Tong_ket"] = (
    df["Chuyen_can"] * 0.2
    + df["Giua_ky"] * 0.3
    + df["Cuoi_ky"] * 0.5
)

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

st.subheader("Bang diem sinh vien")
st.dataframe(df, hide_index=True)

st.subheader("Thong ke")
st.write("Diem trung binh:", round(df["Tong_ket"].mean(), 2))

cao = df.loc[df["Tong_ket"].idxmax()]
thap = df.loc[df["Tong_ket"].idxmin()]

st.write("Sinh vien cao nhat:", cao["Ho_ten"], "-", cao["Tong_ket"])
st.write("Sinh vien thap nhat:", thap["Ho_ten"], "-", thap["Tong_ket"])
st.write("So sinh vien dat:", int((df["Tong_ket"] >= 5).sum()))

st.subheader("Bieu do diem tong ket")
st.bar_chart(df.set_index("Ho_ten")["Tong_ket"])
