import streamlit as st
# Bỏ new_session đi, dùng lại cái mặc định
from rembg import remove 
from PIL import Image
import io

st.set_page_config(page_title="App Xóa Phông", page_icon="✂️")
st.title("✂️ Xóa Phông (Chế độ Tỉ mỉ)")

uploaded_file = st.file_uploader("Chọn ảnh...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Ảnh gốc")
        st.image(image, use_container_width=True)

    with st.spinner('Đang dò từng milimet...'):
        # Bật chế độ Alpha Matting với thông số mạnh
        output_image = remove(
            image,
            alpha_matting=True,
            # Tăng độ gắt để giữ lại chi tiết (thử từ 200 -> 250)
            alpha_matting_foreground_threshold=250,
            # Giảm độ gắt nền để xóa sạch hơn (thử từ 0 -> 20)
            alpha_matting_background_threshold=5,
            # Co viền lại để tránh bị răng cưa
            alpha_matting_erode_size=5
        )

    with col2:
        st.header("Kết quả")
        st.image(output_image, use_container_width=True)

    # (Phần nút tải về giữ nguyên...)
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button("Tải ảnh về", byte_im, "ket_qua.png", "image/png")