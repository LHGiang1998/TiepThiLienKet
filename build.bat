@echo off
chcp 65001 >nul
echo.
echo ========================================
echo   🚀 BUILD WEBSITE TỪ PRODUCTS.JSON
echo ========================================
echo.

echo 📝 Đang đọc file products.json...
if not exist products.json (
    echo ❌ Không tìm thấy file products.json
    echo    Vui lòng tạo file products.json trước
    pause
    exit /b 1
)

echo 🔨 Đang build HTML...
python build.py

if %errorlevel% equ 0 (
    echo.
    echo ✅ BUILD THÀNH CÔNG!
    echo 📄 File index.html đã được tạo
    echo 🌐 Bạn có thể mở index.html trong trình duyệt
    echo.
    echo Nhấn Enter để mở website...
    pause >nul
    start index.html
) else (
    echo.
    echo ❌ BUILD THẤT BẠI!
    echo    Vui lòng kiểm tra lỗi ở trên
    pause
)
