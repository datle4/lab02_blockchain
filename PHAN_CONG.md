# Lab 02 · Bitcoin Script | Kế hoạch cho nhóm 5 người

Đích đến của nhóm là có hai giao dịch chi tiêu thành công trên Bitcoin testnet, một từ địa chỉ P2PKH và một từ địa chỉ P2SH multisig 2-of-2. Với mỗi luồng, nhóm cần chỉ ra output nào đã khóa tiền, giao dịch nào đã dùng output đó và điều kiện nào cho phép chi tiêu.

## Nhận việc

Mỗi người điền tên và MSSV vào hàng của mình. Các đường dẫn trong bảng tính từ `GROUP_ID/Code/`. Bốn module nghiệp vụ nằm trong `bitcoin_lab/`. Mỗi người viết phần nhận xét và cung cấp minh chứng cho phần mình làm.

| Thành viên | File phụ trách | Việc cần bàn giao | Cách kiểm tra |
|---|---|---|---|
| TV1 · … | `bitcoin_lab/transaction.py` | Sinh khóa testnet, suy ra public key, dựng giao dịch chưa ký từ một UTXO. Viết phần cấu trúc giao dịch và phí. | Dùng UTXO mẫu 20.000 sat, phí 500 sat. Giao dịch phải tham chiếu đúng `txid/vout`, trả 19.500 sat về đích và báo lỗi nếu phí âm hoặc tiền còn lại không hợp lệ. |
| TV2 · … | `bitcoin_lab/p2pkh.py` | **Task 1.** Tạo hoặc đối chiếu địa chỉ P2PKH, dựng script khóa, nhận BTC từ faucet, ký và chi tiêu. Viết phần giải thích khóa/mở khóa P2PKH. | Ghi lại TXID nạp, chỉ số output và TXID chi. Đối chiếu input của giao dịch chi với đúng output đã nạp. |
| TV3 · … | `bitcoin_lab/multisig.py` | **Task 2.** Tạo redeem script từ hai public key, suy ra địa chỉ P2SH, nhận BTC, lấy hai chữ ký và ráp giao dịch chi. Viết phần lợi ích và hạn chế của 2-of-2. | Bàn giao giao dịch mẫu cho TV5 kiểm tra. Với đủ hai chữ ký đúng thứ tự, ghi TXID nạp, chỉ số output và TXID chi trên testnet. |
| TV4 · … | `bitcoin_lab/testnet.py` | Chọn nguồn tra cứu testnet, hiện thực tra UTXO, phát giao dịch và tra xác nhận. Hỗ trợ TV2/TV3 chạy hai luồng, ghi mạng, dịch vụ và cách tra giao dịch để nhóm có thể chạy lại. | Trả danh sách rỗng cho địa chỉ chưa nhận tiền, trả TXID khi phát thành công và phân biệt lỗi dịch vụ với giao dịch đang chờ xác nhận. |
| TV5 · … | `tests/test_scripts.py` và báo cáo | **Task 3.** Chuẩn bị bốn ca kiểm thử cục bộ, kiểm tra điều kiện mở khóa, phân tích kết quả và ứng dụng. Tổng hợp phần viết của cả nhóm vào `Report.pdf` rồi đóng gói. | P2PKH chấp nhận đúng khóa, từ chối sai khóa. Multisig 2-of-2 chấp nhận đủ hai chữ ký hợp lệ, từ chối khi thiếu một chữ ký. Đối chiếu kết quả với hai giao dịch thành công trên testnet. |

Đề quy định hai luồng thực hành (mục 4–5), báo cáo phân tích (mục 6) và cấu trúc nộp bài (mục 7). Nhóm tự chọn số lượng file nguồn. Bộ kiểm thử là phần nhóm bổ sung để kiểm tra các điều kiện chi tiêu và lấy minh chứng cho báo cáo.

## Mốc 1 · Chốt giao diện để làm song song

- [ ] Cả nhóm thống nhất cùng một mạng Bitcoin testnet cho ví, faucet, dịch vụ phát giao dịch và explorer. TV1 và TV4 ghi lại mạng, thư viện và dịch vụ thực tế để đưa vào báo cáo.
- [ ] TV1 lấy chữ ký hàm trong khung làm giao diện chung. `UTXO` có bốn trường: `txid`, `vout`, `value_sats`, `script_pubkey_hex`. Số tiền và phí dùng số nguyên satoshi. Giao dịch truyền giữa các module dưới dạng chuỗi hex, public key và script đã tuần tự hóa dùng `bytes`.
- [ ] Khung chọn cách chi một UTXO sang một địa chỉ nhận. Số tiền gửi bằng giá trị UTXO trừ phí nên giao dịch này có một output. TV1 gửi một bộ dữ liệu mẫu cho TV2/TV3/TV5 để các bạn làm phần ký và kiểm thử trong lúc TV4 kết nối testnet.
- [ ] TV2/TV3 kiểm tra địa chỉ và public key giảng viên cung cấp nếu có. Trước khi nạp, xác định người có thể ký cho từng khóa. Nếu dùng khóa nhóm tự tạo theo ví dụ trong đề, mỗi người ký giữ khóa riêng của mình. Chỉ dùng địa chỉ, public key và TXID làm minh chứng công khai.

## Mốc 2 · Chạy đủ hai luồng

Sau khi điền các hàm, đứng tại `GROUP_ID/Code/` và chạy `python3 -m bitcoin_lab.p2pkh` hoặc `python3 -m bitcoin_lab.multisig`. Hai hàm `main()` là nơi TV2 và TV3 nối các bước bên dưới.

| Bước | Task 1 · P2PKH | Task 2 · P2SH multisig 2-of-2 |
|---|---|---|
| Khóa tiền | Lập script khóa cho địa chỉ đích, xin testnet BTC từ faucet và đối chiếu script của output nhận được. | Tạo redeem script theo thứ tự hai public key, suy ra địa chỉ P2SH và nạp testnet BTC vào địa chỉ đó. |
| Chọn tiền để chi | Gọi `list_unspent`, chọn đúng output và ghi số satoshi. | Chọn output nạp vào địa chỉ P2SH vừa tạo và kiểm tra nó khớp với redeem script. |
| Mở khóa | Dùng `build_unsigned_spend` của TV1, sau đó `sign_spend` bằng khóa tương ứng với địa chỉ đã nạp. | Dựng một giao dịch chưa ký. Hai người gọi `sign_input` trên cùng giao dịch và redeem script. Gọi `assemble_signed_spend` với hai chữ ký theo thứ tự public key. |
| Đối chiếu | Phát giao dịch, ghi TXID chi và trạng thái xác nhận. | Kiểm tra ca thiếu chữ ký ở máy cục bộ, sau đó phát giao dịch đủ chữ ký và ghi trạng thái xác nhận. |

Mỗi luồng điền một hàng sau khi chạy. Lưu liên kết explorer để TV5 có thể đối chiếu các giá trị và dẫn nguồn trong báo cáo.

| Luồng | TXID nạp / vout | Giá trị UTXO (sat) | Phí (sat) | Số tiền đích nhận (sat) | TXID chi / link explorer | Số xác nhận lúc kiểm tra |
|---|---|---:|---:|---:|---|---:|
| P2PKH | | | | | | |
| P2SH 2-of-2 | | | | | | |

## Mốc 3 · Task 3 và quy cách nộp

- [ ] **Kiểm thử cục bộ.** Từ `GROUP_ID/Code/`, TV5 chạy `python3 -m unittest discover -s tests -v` sau khi các hàm đã được điền. Dùng khóa và UTXO mẫu, đánh giá script của giao dịch chi với script khóa của output trước. Với ca thiếu chữ ký, dựng giao dịch mẫu chỉ có một chữ ký để kiểm tra đúng điều kiện 2-of-2. Các ca này có thể chạy trước khi faucet cấp tiền.
- [ ] **Phân tích và phản ánh.** TV5 tổng hợp kết quả cùng TV2/TV3, so sánh hai điều kiện chi tiêu, phân tích hệ quả nếu một khóa bị lộ hoặc bị mất, rồi nêu tình huống phù hợp cho mỗi script. Cả nhóm rút ra ưu điểm và giới hạn của Bitcoin Script từ kết quả đã quan sát.
- [ ] **Nội dung báo cáo.** Ghi thông tin thành viên, cấu trúc project, các quyết định thiết kế, luồng hoạt động và tương tác giữa các thành phần. Đưa minh chứng của hai luồng, khó khăn thực tế, cách xử lý, bài học của các thành viên và toàn bộ liên kết, sách đã tham khảo.
- [ ] **Định dạng.** Xuất đúng tên `Report.pdf`, tối đa 15 trang, trình bày trang đơn, cỡ chữ 12 pt, tiếng Việt hoặc tiếng Anh. Dùng mô tả, sơ đồ hoặc minh chứng giao dịch. Đề cấm chèn mã nguồn vào báo cáo.
- [ ] **Đóng gói.** Đổi `GROUP_ID` thành mã nhóm thật. Trong thư mục đó, đặt `Code/` chứa toàn bộ project và `Report.pdf` cùng cấp với `Code/`. File thực thi là tùy chọn. Nén cả thư mục thành `<mã nhóm>.zip`, mở lại ZIP và kiểm tra cả hai đường dẫn. File phân công này nằm ngoài thư mục nộp.
