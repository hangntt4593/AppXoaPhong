import streamlit as st
from rembg import remove
from PIL import Image
import io

# Cấu hình trang web
st.set_page_config(page_title="App Xóa Phông", page_icon="✂️")
st.title("✂️ Ứng dụng Xóa Phông")

# Nút tải ảnh
uploaded_file = st.file_uploader("Chọn ảnh cần xóa phông...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Hiển thị ảnh gốc
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Ảnh gốc")
        st.image(image, use_container_width=True)

    # Xử lý xóa phông
    with st.spinner('Đang tách nền...'):
        output_image = remove(image)

    with col2:
        st.header("Kết quả")
        st.image(output_image, use_container_width=True)

    # Xử lý để tải về
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="Tải ảnh về",
        data=byte_im,
        file_name="anh_xoa_phong.png",
        mime="image/png"
    )