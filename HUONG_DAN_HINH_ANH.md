# 🖼️ HƯỚNG DẪN SỬ DỤNG HÌNH ẢNH

## 📁 **Cấu trúc thư mục hiện tại:**
```
TiepThiLienKet/
├── index.html          # File HTML chính
├── style.css           # File CSS
├── script.js           # File JavaScript
├── images/             # THƯ MỤC HÌNH ẢNH (MỚI TẠO)
│   └── README.md       # Hướng dẫn sử dụng
└── HUONG_DAN_HINH_ANH.md # File này
```

## 🎯 **CÁCH THÊM HÌNH ẢNH**

### **Bước 1: Chuẩn bị hình ảnh**
1. **Tải hình ảnh sản phẩm** từ website bán hàng hoặc chụp ảnh
2. **Đổi tên file** theo quy tắc:
   - Không dấu, không khoảng trắng
   - Sử dụng dấu gạch ngang (-)
   - Ví dụ: `iphone-15-pro-max.jpg`, `laptop-gaming-asus.png`

### **Bước 2: Copy hình vào thư mục**
1. Mở thư mục `images/`
2. Copy/paste hình ảnh vào đây
3. Ghi nhớ tên file chính xác

### **Bước 3: Cập nhật HTML**
Trong file `index.html`, thay đổi đường dẫn hình ảnh:

```html
<!-- TRƯỚC (dùng link online) -->
<img src="https://example.com/image.jpg" alt="Sản phẩm">

<!-- SAU (dùng hình trong thư mục images) -->
<img src="images/ten-file-hinh-anh.jpg" alt="Sản phẩm">
```

## 📝 **VÍ DỤ CỤ THỂ**

### **Sản phẩm 1: iPhone 15 Pro Max**
```html
<!-- Trong HTML -->
<img src="images/iphone-15-pro-max.jpg" alt="iPhone 15 Pro Max">

<!-- File cần có trong thư mục images: -->
images/iphone-15-pro-max.jpg
```

### **Sản phẩm 2: Laptop Gaming**
```html
<!-- Trong HTML -->
<img src="images/laptop-gaming.jpg" alt="Laptop Gaming">

<!-- File cần có trong thư mục images: -->
images/laptop-gaming.jpg
```

### **Sản phẩm 3: AirPods Pro**
```html
<!-- Trong HTML -->
<img src="images/airpods-pro.jpg" alt="AirPods Pro">

<!-- File cần có trong thư mục images: -->
images/airpods-pro.jpg
```

### **Sản phẩm 4: Apple Watch**
```html
<!-- Trong HTML -->
<img src="images/apple-watch.jpg" alt="Apple Watch">

<!-- File cần có trong thư mục images: -->
images/apple-watch.jpg
```

## 🔧 **CÁCH SỬA ĐỔI SẢN PHẨM**

### **Thay đổi sản phẩm hiện có:**
1. **Thay hình ảnh:**
   - Xóa hình cũ trong thư mục `images/`
   - Thêm hình mới với cùng tên file
   - HOẶC đổi tên file mới và cập nhật HTML

2. **Cập nhật thông tin:**
   - Mở file `index.html`
   - Tìm sản phẩm cần sửa
   - Thay đổi tên, mô tả, giá, link affiliate

### **Thêm sản phẩm mới:**
1. **Thêm hình ảnh** vào thư mục `images/`
2. **Copy khối product-card** trong HTML:

```html
<!-- SẢN PHẨM MỚI -->
<div class="product-card">
    <div class="product-image">
        <img src="images/ten-hinh-moi.jpg" alt="Tên sản phẩm mới">
        <div class="product-badge">New</div>
    </div>
    <div class="product-info">
        <h3>Tên Sản Phẩm Mới</h3>
        <p class="product-description">Mô tả sản phẩm mới của bạn.</p>
        <div class="product-price">
            <span class="old-price">Giá cũ</span>
            <span class="new-price">Giá mới</span>
        </div>
        <a href="LINK_AFFILIATE_MỚI" class="btn-buy" target="_blank">
            <i class="fas fa-shopping-cart"></i>
            Mua Ngay
        </a>
    </div>
</div>
```

## 📏 **KHUYẾN NGHỊ VỀ HÌNH ẢNH**

### **Kích thước:**
- **Tỷ lệ khuyến nghị**: 3:2 (ví dụ: 300x200px, 600x400px)
- **Kích thước tối ưu**: 300x200px đến 600x400px
- **Dung lượng**: < 500KB để tải nhanh

### **Định dạng:**
- **JPG**: Cho ảnh có nhiều màu sắc
- **PNG**: Cho ảnh có nền trong suốt
- **WebP**: Định dạng mới, dung lượng nhỏ (khuyến nghị)

### **Chất lượng:**
- Hình ảnh rõ nét, không bị mờ
- Ánh sáng tốt, màu sắc chân thực
- Nền sạch sẽ, tập trung vào sản phẩm

## 🚀 **QUY TRÌNH HOÀN CHỈNH**

### **1. Chuẩn bị:**
- [ ] Tải/chụp hình ảnh sản phẩm
- [ ] Đổi tên file theo quy tắc
- [ ] Tối ưu kích thước nếu cần

### **2. Upload:**
- [ ] Copy hình vào thư mục `images/`
- [ ] Kiểm tra tên file chính xác

### **3. Cập nhật HTML:**
- [ ] Mở file `index.html`
- [ ] Tìm sản phẩm cần sửa
- [ ] Thay đổi `src="images/ten-file.jpg"`
- [ ] Cập nhật `alt="Mô tả sản phẩm"`

### **4. Cập nhật thông tin:**
- [ ] Thay đổi tên sản phẩm
- [ ] Cập nhật mô tả
- [ ] Sửa giá cả
- [ ] Thay link affiliate

### **5. Kiểm tra:**
- [ ] Lưu file HTML (Ctrl + S)
- [ ] Mở trong trình duyệt
- [ ] Kiểm tra hình ảnh hiển thị đúng
- [ ] Test link affiliate hoạt động

## ⚠️ **LƯU Ý QUAN TRỌNG**

### **Đường dẫn file:**
```html
<!-- ĐÚNG -->
<img src="images/iphone-15.jpg" alt="iPhone 15">

<!-- SAI - thiếu thư mục -->
<img src="iphone-15.jpg" alt="iPhone 15">

<!-- SAI - sai tên file -->
<img src="images/iphone15.jpg" alt="iPhone 15">
```

### **Tên file:**
- ✅ `iphone-15-pro-max.jpg`
- ✅ `laptop-gaming-asus.png`
- ❌ `iPhone 15 Pro Max.jpg` (có khoảng trắng)
- ❌ `laptop_gaming_asus.png` (dùng underscore)

### **Alt text:**
- Luôn có mô tả cho hình ảnh
- Giúp SEO và accessibility
- Mô tả ngắn gọn, chính xác

## 🔍 **TROUBLESHOOTING**

### **Hình ảnh không hiển thị:**
1. **Kiểm tra tên file** có chính xác không
2. **Kiểm tra đường dẫn** `images/ten-file.jpg`
3. **Kiểm tra file có tồn tại** trong thư mục images
4. **Refresh trình duyệt** (F5)

### **Hình ảnh bị vỡ:**
1. **Kiểm tra định dạng file** (JPG, PNG, WebP)
2. **Kiểm tra dung lượng** không quá lớn
3. **Thử mở file** trực tiếp để đảm bảo không bị lỗi

---

## 🎯 **TÓM TẮT NHANH**

1. **Thêm hình** → Thư mục `images/`
2. **Đặt tên** → `san-pham-abc.jpg`
3. **Cập nhật HTML** → `src="images/san-pham-abc.jpg"`
4. **Lưu và test** → Ctrl+S, F5

**Bây giờ bạn có thể tự do thêm hình ảnh và quản lý sản phẩm dễ dàng! 🚀**
