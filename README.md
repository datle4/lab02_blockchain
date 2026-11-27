# Lab 02 · Bitcoin Script

Bài thực hành môn Blockchain về cách dùng Bitcoin Script để khóa và chi tiêu output giao dịch trên Bitcoin testnet.

| Task | Nội dung |
| --- | --- |
| 1 · P2PKH | Tạo địa chỉ và script khóa, nhận BTC testnet rồi ký giao dịch chi tiêu bằng khóa tương ứng. |
| 2 · P2SH multisig 2-of-2 | Tạo redeem script từ hai public key, nhận BTC testnet rồi chi tiêu bằng hai chữ ký hợp lệ. |
| 3 · Phân tích | So sánh điều kiện chi tiêu, phân tích lợi ích và hạn chế của từng script, ghi lại kết quả thực nghiệm trong báo cáo. |

## Cấu trúc

| Đường dẫn | Mục đích |
| --- | --- |
| [`GROUP_ID/Code/bitcoin_lab/transaction.py`](GROUP_ID/Code/bitcoin_lab/transaction.py) | Quản lý khóa testnet, biểu diễn UTXO và dựng giao dịch chưa ký. |
| [`GROUP_ID/Code/bitcoin_lab/p2pkh.py`](GROUP_ID/Code/bitcoin_lab/p2pkh.py) | Luồng tạo địa chỉ P2PKH và ký giao dịch chi tiêu. |
| [`GROUP_ID/Code/bitcoin_lab/multisig.py`](GROUP_ID/Code/bitcoin_lab/multisig.py) | Luồng tạo địa chỉ P2SH, ký và ghép hai chữ ký. |
| [`GROUP_ID/Code/bitcoin_lab/testnet.py`](GROUP_ID/Code/bitcoin_lab/testnet.py) | Tra UTXO, phát giao dịch và kiểm tra số xác nhận. |
| [`GROUP_ID/Code/tests/test_scripts.py`](GROUP_ID/Code/tests/test_scripts.py) | Các ca kiểm thử cục bộ cho hai điều kiện chi tiêu. |
| [`PHAN_CONG.md`](PHAN_CONG.md) | Phân công 5 thành viên, checklist và bảng ghi kết quả giao dịch. |

## Chạy sau khi triển khai

Repo hiện chứa khung Python. Các hàm và ca kiểm thử đang dùng `raise NotImplementedError`. Sau khi điền các phần tương ứng, chạy từ thư mục gốc của repo.

```bash
cd GROUP_ID/Code
python3 -m unittest discover -s tests -v
python3 -m bitcoin_lab.p2pkh
python3 -m bitcoin_lab.multisig
```

Cả nhóm dùng cùng một mạng Bitcoin testnet cho faucet, ví và dịch vụ tra cứu giao dịch. Ghi lại TXID nạp, chỉ số output, TXID chi và trạng thái xác nhận của mỗi luồng trong bảng kết quả. Giữ private key và thông tin đăng nhập ở máy cá nhân.

## Nộp bài

Đổi `GROUP_ID` thành mã nhóm thật. Đặt `Report.pdf` cùng cấp với thư mục `Code/`, sau đó nén thư mục mang mã nhóm thành `<mã nhóm>.zip`. Báo cáo tối đa 15 trang, cỡ chữ 12 pt.
