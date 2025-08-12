# 🛠️ HƯỚNG DẪN CẬP NHẬT SẢN PHẨM

## 📁 **Tình trạng hiện tại:**

### **Thư mục images/ có sẵn:**
```
images/
├── JC3248W535.jpg      # Sản phẩm 1 (đã cập nhật)
├── esp32-board.jpg     # Sản phẩm 2 (đã cập nhật)
├── product-3.jpg       # Sản phẩm 3 (chờ cập nhật)
├── product-4.jpg       # Sản phẩm 4 (chờ cập nhật)
└── README.md
```

### **Trạng thái sản phẩm:**
- ✅ **Sản phẩm 1**: Đã hoàn chỉnh (Màn Hình jc4832w535)
- ✅ **Sản phẩm 2**: Đã cập nhật (ESP32 Development Board)
- ⏳ **Sản phẩm 3**: Cần cập nhật thông tin
- ⏳ **Sản phẩm 4**: Cần cập nhật thông tin

## 🎯 **CÁCH CẬP NHẬT SẢN PHẨM**

### **Để thay đổi sản phẩm 3:**

#### **Bước 1: Thay hình ảnh**
- Thay file `images/product-3.jpg` bằng hình ảnh sản phẩm mới
- Hoặc đổi tên file mới thành `product-3.jpg`

#### **Bước 2: Cập nhật thông tin trong index.html**
Tìm đến dòng 89-108 và thay đổi:

```html
<!-- Product 3 - Sản phẩm 3 -->
<div class="product-card">
    <div class="product-image">
        <img src="images/product-3.jpg" alt="TÊN_SẢN_PHẨM_MỚI">
        <div class="product-badge new">New</div>
    </div>
    <div class="product-info">
        <h3>TÊN_SẢN_PHẨM_MỚI</h3>
        <p class="product-description">MÔ_TẢ_SẢN_PHẨM_MỚI</p>
        <div class="product-price">
            <span class="old-price">GIÁ_CŨ</span>
            <span class="new-price">GIÁ_MỚI</span>
        </div>
        <a href="LINK_AFFILIATE_MỚI" class="btn-buy" target="_blank">
            <i class="fas fa-shopping-cart"></i>
            Mua Ngay
        </a>
    </div>
</div>
```

### **Để thay đổi sản phẩm 4:**

#### **Bước 1: Thay hình ảnh**
- Thay file `images/product-4.jpg` bằng hình ảnh sản phẩm mới

#### **Bước 2: Cập nhật thông tin trong index.html**
Tìm đến dòng 110-129 và thay đổi tương tự.

## 📝 **VÍ DỤ CẬP NHẬT CỤ THỂ**

### **Ví dụ: Thay sản phẩm 3 thành "Tai nghe Bluetooth"**

```html
<!-- Product 3 - Tai nghe Bluetooth -->
<div class="product-card">
    <div class="product-image">
        <img src="images/product-3.jpg" alt="Tai nghe Bluetooth">
        <div class="product-badge new">New</div>
    </div>
    <div class="product-info">
        <h3>Tai Nghe Bluetooth 5.0</h3>
        <p class="product-description">Tai nghe không dây chất lượng cao, pin 20 giờ, chống nước IPX7, âm thanh stereo.</p>
        <div class="product-price">
            <span class="old-price">299,000đ</span>
            <span class="new-price">199,000đ</span>
        </div>
        <a href="https://s.shopee.vn/tai-nghe-bluetooth" class="btn-buy" target="_blank">
            <i class="fas fa-shopping-cart"></i>
            Mua Ngay
        </a>
    </div>
</div>
```

## 🔄 **THÊM SẢN PHẨM MỚI**

### **Bước 1: Thêm hình ảnh**
- Copy hình ảnh mới vào thư mục `images/`
- Đặt tên: `product-5.jpg`, `product-6.jpg`, v.v.

### **Bước 2: Thêm code HTML**
Copy khối code sau và paste vào cuối product-grid (sau sản phẩm 4):

```html
<!-- Product 5 - SẢN PHẨM MỚI -->
<div class="product-card">
    <div class="product-image">
        <img src="images/product-5.jpg" alt="Sản phẩm 5">
        <div class="product-badge">Hot</div>
    </div>
    <div class="product-info">
        <h3>Tên Sản Phẩm 5</h3>
        <p class="product-description">Mô tả sản phẩm 5.</p>
        <div class="product-price">
            <span class="old-price">Giá cũ</span>
            <span class="new-price">Giá mới</span>
        </div>
        <a href="LINK_AFFILIATE" class="btn-buy" target="_blank">
            <i class="fas fa-shopping-cart"></i>
            Mua Ngay
        </a>
    </div>
</div>
```

## 🎨 **CÁC LOẠI BADGE**

```html
<div class="product-badge">Hot</div>      <!-- Màu đỏ -->
<div class="product-badge sale">Sale</div> <!-- Màu đỏ nhạt -->
<div class="product-badge new">New</div>   <!-- Màu xanh -->
```

## 📋 **CHECKLIST CẬP NHẬT**

### **Trước khi cập nhật:**
- [ ] Backup file `index.html` hiện tại
- [ ] Chuẩn bị hình ảnh sản phẩm mới
- [ ] Chuẩn bị link affiliate

### **Khi cập nhật:**
- [ ] Thay hình ảnh trong thư mục `images/`
- [ ] Cập nhật tên sản phẩm
- [ ] Cập nhật mô tả sản phẩm
- [ ] Cập nhật giá cả
- [ ] Cập nhật link affiliate
- [ ] Cập nhật alt text cho hình ảnh

### **Sau khi cập nhật:**
- [ ] Lưu file (Ctrl + S)
- [ ] Mở trong trình duyệt
- [ ] Kiểm tra hình ảnh hiển thị
- [ ] Test link affiliate
- [ ] Kiểm tra responsive trên mobile

## 🚀 **TIPS QUAN TRỌNG**

### **Về hình ảnh:**
- Kích thước khuyến nghị: 300x200px (tỷ lệ 3:2)
- Định dạng: JPG, PNG
- Dung lượng: < 500KB
- Chất lượng: Rõ nét, đẹp mắt

### **Về nội dung:**
- Tên sản phẩm: Ngắn gọn, dễ hiểu
- Mô tả: 1-2 câu, highlight điểm mạnh
- Giá: Rõ ràng, có so sánh
- Link: Luôn test trước khi publish

### **Về SEO:**
- Alt text mô tả chính xác hình ảnh
- Tên file không dấu, không khoảng trắng
- Mô tả sản phẩm có từ khóa

## 📞 **HỖ TRỢ**

Nếu gặp vấn đề:
1. Kiểm tra tên file hình ảnh có chính xác không
2. Kiểm tra đường dẫn `images/ten-file.jpg`
3. Refresh trình duyệt (Ctrl + F5)
4. Kiểm tra Developer Tools (F12) xem có lỗi không

---

**Bây giờ website đã sẵn sàng với hình ảnh thực tế! Bạn chỉ cần cập nhật thông tin sản phẩm 3 và 4 theo hướng dẫn trên. 🎯**
