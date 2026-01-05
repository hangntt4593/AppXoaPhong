import streamlit as st
from rembg import remove, new_session # <--- Nhớ thêm new_session vào đây
from PIL import Image
import io

st.set_page_config(page_title="App Xóa Phông Pro", page_icon="✂️")
st.title("✂️ Xóa Phông (Model IS-Net)")

# 1. Tải trước bộ não xịn (IS-Net)
# Lần chạy đầu tiên nó sẽ hơi lâu vì phải tải model về
model_name = "isnet-general-use" 
session = new_session(model_name)

uploaded_file = st.file_uploader("Chọn ảnh...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Ảnh gốc")
        st.image(image, use_container_width=True)

    with st.spinner('Đang dùng não xịn để tách...'):
        # 2. Truyền cái session (bộ não) vào hàm remove
        output_image = remove(image, session=session)

    with col2:
        st.header("Kết quả")
        st.image(output_image, use_container_width=True)

    # Phần tải về giữ nguyên như cũ...
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button("Tải ảnh về", byte_im, "xoa_phong_isnet.png", "image/png")

