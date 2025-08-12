#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script tự động build HTML từ file products.json
Sử dụng: python build.py
"""

import json
import os
from datetime import datetime

def load_products_data():
    """Đọc dữ liệu từ file products.json"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("❌ Không tìm thấy file products.json")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Lỗi định dạng JSON: {e}")
        return None

def generate_product_html(product):
    """Tạo HTML cho một sản phẩm"""
    badge_class = product.get('badge_type', 'hot')
    if badge_class == 'hot':
        badge_html = f'<div class="product-badge">{product["badge"]}</div>'
    else:
        badge_html = f'<div class="product-badge {badge_class}">{product["badge"]}</div>'
    
    # Xử lý giá (nếu không có giá cũ thì chỉ hiển thị giá mới)
    price_html = ""
    if product.get('old_price') and product['old_price'].strip():
        price_html = f'''
                            <span class="old-price">{product['old_price']}</span>
                            <span class="new-price">{product['new_price']}</span>'''
    else:
        price_html = f'''
                            <span class="new-price">{product['new_price']}</span>'''
    
    return f'''
                <!-- Product {product['id']} - {product['name']} -->
                <div class="product-card">
                    <div class="product-image">
                        <img src="images/{product['image']}" alt="{product['name']}">
                        {badge_html}
                    </div>
                    <div class="product-info">
                        <h3>{product['name']}</h3>
                        <p class="product-description">{product['description']}</p>
                        <div class="product-price">{price_html}
                        </div>
                        <a href="{product['affiliate_link']}" class="btn-buy" target="_blank">
                            <i class="fas fa-shopping-cart"></i>
                            Mua Ngay
                        </a>
                    </div>
                </div>'''

def generate_html(data):
    """Tạo file HTML hoàn chỉnh"""
    website_info = data['website_info']
    products = data['products']
    
    # Tạo HTML cho tất cả sản phẩm
    products_html = ""
    for product in products:
        products_html += generate_product_html(product)
    
    # Template HTML hoàn chỉnh
    html_template = f'''<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{website_info['title']}</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="container">
            <h1 class="logo">
                <i class="fas fa-shopping-cart"></i>
                Tiếp Thị Liên Kết
            </h1>
            <nav class="nav">
                <a href="#products">Sản Phẩm</a>
                <a href="#about">Giới Thiệu</a>
                <a href="#contact">Liên Hệ</a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h2>Khám Phá Những Sản Phẩm Tuyệt Vời</h2>
            <p>{website_info['description']}</p>
            <a href="#products" class="btn-primary">Xem Sản Phẩm</a>
        </div>
    </section>

    <!-- Products Section -->
    <section id="products" class="products">
        <div class="container">
            <h2 class="section-title">Sản Phẩm Nổi Bật</h2>
            
            <!-- Product Grid -->
            <div class="product-grid">{products_html}
                
                <!-- Thêm sản phẩm mới tại đây -->
                
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about" class="about">
        <div class="container">
            <h2 class="section-title">Về Chúng Tôi</h2>
            <div class="about-content">
                <div class="about-text">
                    <h3>Tại sao chọn chúng tôi?</h3>
                    <ul>
                        <li><i class="fas fa-check"></i> Sản phẩm chất lượng cao</li>
                        <li><i class="fas fa-check"></i> Giá cả cạnh tranh</li>
                        <li><i class="fas fa-check"></i> Giao hàng nhanh chóng</li>
                        <li><i class="fas fa-check"></i> Hỗ trợ khách hàng 24/7</li>
                    </ul>
                </div>
                <div class="about-stats">
                    <div class="stat">
                        <h4>1000+</h4>
                        <p>Khách hàng hài lòng</p>
                    </div>
                    <div class="stat">
                        <h4>500+</h4>
                        <p>Sản phẩm</p>
                    </div>
                    <div class="stat">
                        <h4>99%</h4>
                        <p>Đánh giá tích cực</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <div class="container">
            <h2 class="section-title">Liên Hệ</h2>
            <div class="contact-info">
                <div class="contact-item">
                    <i class="fas fa-phone"></i>
                    <h4>Điện thoại</h4>
                    <p>{website_info['contact']['phone']}</p>
                </div>
                <div class="contact-item">
                    <i class="fas fa-envelope"></i>
                    <h4>Email</h4>
                    <p>{website_info['contact']['email']}</p>
                </div>
                <div class="contact-item">
                    <i class="fas fa-map-marker-alt"></i>
                    <h4>Địa chỉ</h4>
                    <p>{website_info['contact']['address']}</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Tiếp Thị Liên Kết</h4>
                    <p>Chúng tôi cam kết mang đến những sản phẩm tốt nhất với giá cả hợp lý.</p>
                </div>
                <div class="footer-section">
                    <h4>Liên kết nhanh</h4>
                    <ul>
                        <li><a href="#products">Sản phẩm</a></li>
                        <li><a href="#about">Giới thiệu</a></li>
                        <li><a href="#contact">Liên hệ</a></li>
                    </ul>
                </div>
                <div class="footer-section">
                    <h4>Theo dõi chúng tôi</h4>
                    <div class="social-links">
                        <a href="#"><i class="fab fa-facebook"></i></a>
                        <a href="#"><i class="fab fa-instagram"></i></a>
                        <a href="#"><i class="fab fa-youtube"></i></a>
                        <a href="#"><i class="fab fa-tiktok"></i></a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Tiếp Thị Liên Kết. Tất cả quyền được bảo lưu.</p>
            </div>
        </div>
    </footer>

    <!-- Back to top button -->
    <button id="backToTop" class="back-to-top">
        <i class="fas fa-arrow-up"></i>
    </button>

    <script src="script.js"></script>
    
    <!-- Build info -->
    <!-- Generated automatically from products.json at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} -->
</body>
</html>'''
    
    return html_template

def main():
    """Hàm chính"""
    print("🚀 Bắt đầu build HTML từ products.json...")
    
    # Đọc dữ liệu
    data = load_products_data()
    if not data:
        return
    
    # Kiểm tra thư mục images
    if not os.path.exists('images'):
        print("⚠️  Cảnh báo: Thư mục 'images' không tồn tại")
    
    # Kiểm tra file hình ảnh
    missing_images = []
    for product in data['products']:
        image_path = os.path.join('images', product['image'])
        if not os.path.exists(image_path):
            missing_images.append(product['image'])
    
    if missing_images:
        print("⚠️  Cảnh báo: Các file hình ảnh sau không tồn tại:")
        for img in missing_images:
            print(f"   - images/{img}")
    
    # Tạo HTML
    html_content = generate_html(data)
    
    # Ghi file
    try:
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("✅ Build thành công!")
        print(f"📄 File index.html đã được tạo với {len(data['products'])} sản phẩm")
        print(f"🕒 Thời gian build: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        if missing_images:
            print(f"⚠️  {len(missing_images)} hình ảnh bị thiếu - vui lòng kiểm tra thư mục images/")
        
    except Exception as e:
        print(f"❌ Lỗi khi ghi file: {e}")

if __name__ == "__main__":
    main()
