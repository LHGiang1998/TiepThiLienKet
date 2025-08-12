# 📝 HƯỚNG DẪN SỬ DỤNG FILE PRODUCTS.JSON

## 🎯 **TỔNG QUAN**

Bây giờ bạn có thể quản lý tất cả sản phẩm thông qua file `products.json` thay vì phải sửa trực tiếp HTML. Chỉ cần:
1. **Sửa file `products.json`** với thông tin sản phẩm
2. **Chạy lệnh build** để tự động tạo file HTML

## 📁 **CẤU TRÚC FILE PRODUCTS.JSON**

```json
{
  "website_info": {
    "title": "Tiêu đề website",
    "description": "Mô tả website", 
    "contact": {
      "phone": "Số điện thoại",
      "email": "Email liên hệ",
      "address": "Địa chỉ"
    }
  },
  "products": [
    {
      "id": 1,
      "name": "Tên sản phẩm",
      "description": "Mô tả sản phẩm",
      "old_price": "Giá cũ (có thể để trống)",
      "new_price": "Giá mới",
      "image": "ten-file-hinh.jpg",
      "affiliate_link": "Link affiliate",
      "badge": "Hot/Sale/New/Top",
      "badge_type": "hot/sale/new"
    }
  ]
}
```

## ✏️ **CÁCH SỬA ĐỔI SẢN PHẨM**

### **1. Thay đổi sản phẩm hiện có:**
Mở file `products.json` và sửa thông tin:

```json
{
  "id": 1,
  "name": "iPhone 15 Pro Max",
  "description": "iPhone mới nhất với chip A17 Pro, camera 48MP",
  "old_price": "35,000,000đ",
  "new_price": "29,990,000đ", 
  "image": "iphone-15-pro-max.jpg",
  "affiliate_link": "https://s.shopee.vn/iphone15promax",
  "badge": "Hot",
  "badge_type": "hot"
}
```

### **2. Thêm sản phẩm mới:**
Thêm object mới vào mảng `products`:

```json
{
  "id": 5,
  "name": "Laptop Gaming ASUS",
  "description": "Laptop gaming RTX 4060, RAM 16GB, SSD 512GB",
  "old_price": "25,000,000đ",
  "new_price": "19,990,000đ",
  "image": "laptop-asus-gaming.jpg", 
  "affiliate_link": "https://s.shopee.vn/laptop-asus",
  "badge": "Sale",
  "badge_type": "sale"
}
```

### **3. Xóa sản phẩm:**
Xóa object tương ứng khỏi mảng `products`.

## 🎨 **CÁC LOẠI BADGE**

```json
"badge": "Hot",     "badge_type": "hot"     // Màu đỏ
"badge": "Sale",    "badge_type": "sale"    // Màu đỏ nhạt  
"badge": "New",     "badge_type": "new"     // Màu xanh
"badge": "Top",     "badge_type": "hot"     // Màu đỏ (giống Hot)
```

## 🚀 **CÁCH BUILD HTML**

### **Phương pháp 1: Sử dụng Python (Khuyến nghị)**
```bash
python build.py
```

### **Phương pháp 2: Yêu cầu AI build**
Chỉ cần nói: **"Hãy build HTML từ file products.json"**

## 📝 **VÍ DỤ HOÀN CHỈNH**

### **File products.json mẫu:**
```json
{
  "website_info": {
    "title": "Shop Điện Tử - Tiếp Thị Liên Kết",
    "description": "Chuyên cung cấp các sản phẩm điện tử chất lượng cao",
    "contact": {
      "phone": "0901 234 567", 
      "email": "shop@example.com",
      "address": "123 Nguyễn Văn A, Q1, TP.HCM"
    }
  },
  "products": [
    {
      "id": 1,
      "name": "iPhone 15 Pro Max 256GB",
      "description": "iPhone mới nhất với chip A17 Pro, camera 48MP, màn hình 6.7 inch",
      "old_price": "35,000,000đ",
      "new_price": "29,990,000đ",
      "image": "iphone-15-pro-max.jpg",
      "affiliate_link": "https://s.shopee.vn/iphone15promax",
      "badge": "Hot",
      "badge_type": "hot"
    },
    {
      "id": 2, 
      "name": "AirPods Pro Gen 2",
      "description": "Tai nghe không dây chống ồn, âm thanh Hi-Fi, pin 30 giờ",
      "old_price": "",
      "new_price": "5,490,000đ",
      "image": "airpods-pro-gen2.jpg",
      "affiliate_link": "https://s.shopee.vn/airpods-pro",
      "badge": "New", 
      "badge_type": "new"
    }
  ]
}
```

## 🔧 **TIPS QUAN TRỌNG**

### **Về hình ảnh:**
- File hình phải có trong thư mục `images/`
- Tên file trong JSON phải khớp chính xác với file thực tế
- Ví dụ: `"image": "iphone-15.jpg"` → File `images/iphone-15.jpg` phải tồn tại

### **Về giá cả:**
- Nếu không có giá cũ, để trống: `"old_price": ""`
- Nếu có giá cũ: `"old_price": "500,000đ"`
- Luôn có giá mới: `"new_price": "399,000đ"`

### **Về link affiliate:**
- Luôn sử dụng link đầy đủ: `https://s.shopee.vn/...`
- Test link trước khi publish
- Sử dụng link rút gọn để dễ quản lý

### **Về JSON syntax:**
- Luôn có dấu phẩy `,` giữa các object (trừ object cuối)
- Sử dụng dấu ngoặc kép `"` cho tất cả string
- Kiểm tra syntax bằng JSON validator online

## ⚠️ **LỖI THƯỜNG GẶP**

### **1. Lỗi JSON syntax:**
```json
// SAI - thiếu dấu phẩy
{
  "name": "iPhone"
  "price": "1000đ"
}

// ĐÚNG
{
  "name": "iPhone",
  "price": "1000đ"
}
```

### **2. Lỗi hình ảnh không hiển thị:**
- Kiểm tra tên file trong JSON có khớp với file thực tế
- Kiểm tra file có trong thư mục `images/`
- Kiểm tra không có ký tự đặc biệt trong tên file

### **3. Lỗi link không hoạt động:**
- Kiểm tra link có đầy đủ `https://`
- Test link trong trình duyệt trước

## 🎯 **QUY TRÌNH LÀM VIỆC**

### **Bước 1: Chuẩn bị**
- [ ] Chuẩn bị hình ảnh sản phẩm
- [ ] Copy hình vào thư mục `images/`
- [ ] Chuẩn bị link affiliate

### **Bước 2: Cập nhật dữ liệu**
- [ ] Mở file `products.json`
- [ ] Thêm/sửa thông tin sản phẩm
- [ ] Kiểm tra JSON syntax

### **Bước 3: Build HTML**
- [ ] Chạy `python build.py`
- [ ] Hoặc yêu cầu AI build

### **Bước 4: Kiểm tra**
- [ ] Mở `index.html` trong trình duyệt
- [ ] Kiểm tra hình ảnh hiển thị
- [ ] Test các link affiliate
- [ ] Kiểm tra responsive trên mobile

## 📞 **HỖ TRỢ**

### **Khi gặp lỗi:**
1. **Kiểm tra JSON syntax** bằng jsonlint.com
2. **Kiểm tra file hình ảnh** có tồn tại không
3. **Kiểm tra Python** đã cài đặt chưa
4. **Yêu cầu AI hỗ trợ** nếu cần

### **Lệnh hữu ích:**
```bash
# Kiểm tra Python
python --version

# Chạy build script
python build.py

# Kiểm tra file tồn tại
dir images\
```

---

## 🎉 **TÓM TẮT**

**Từ bây giờ quy trình làm việc của bạn:**
1. **Sửa `products.json`** → Thêm/sửa sản phẩm
2. **Chạy `python build.py`** → Tự động tạo HTML
3. **Mở `index.html`** → Xem kết quả

**Đơn giản, nhanh chóng, không cần sửa HTML thủ công nữa! 🚀**
