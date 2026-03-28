import streamlit as st
st.set_page_config(page_title='Vuong quoc mo hinh', page_icon=':sparkles')
with st.slider:
    st.title('Vuong quoc mo hinh')
    st.header('Chao mung den voi vuong quoc mo hinh')
    st.image('hinh1.jpg')
    st.write('Chung toi ban mo hinh cao cap ...')
    st.write(':house: Dia chi: ')
    st.write(':phone: Dien thoai: ')
st.title('Vuong quoc mo hinh')
chu_de = ['Dragon Ball', 'Naruto', 'One Piece']
cols = st.columns(len(chu_de))
for i, cd in enumerate(chu_de):
    with cols[i]:
        if st.button(cd):
            chon = cd
            st.image('hinh1.jpg', caption=f'MS: 00{i+1}')
if chon:
    st.header(f'Danh sách mô hình {chon}')
    cols = st.columns(3)
    for i in range(3):
        with cols[i]:
            st.image(f'hinh1.jpg', caption=f'MS: 00{i+1}')

# Đặt hàng
st.header('Đặt hàng')
with st.form('Đơn đặt hàng'):
    loai = st.selectbox('Chủ đề', chu_de)
    ma = st.selectbox('Mã số', ['001', '002', '003'])
    slg = st.slider('Số lượng', 0, 10, 0)
    name = st.text_input('Họ tên:')
    sdt = st.text_input('SDT:')
    add = st.text_input('Địa chỉ:')
    bill = {
        'Mô hình': loai,
        'Mã số': ma,
        'Số lượng': slg,
        'Ho va ten KH': name,
        'SDT': sdt,
        'Dia chi': add}
if st.form_submit_button('Xác nhận'):
    st.header('Bạn đã chọn:')
    for k, v in bill.items():
        st.write(k, v)

# In hoá đơn
if st.checkbox('In hoá đơn'):
    hoa_don = '\n'.join([f"{k}: {v}" for k, v in bill.items()])
    st.download_button('Tải hoá đơn', hoa_don)
