# Hướng dẫn đóng góp | Contributing

Cảm ơn anh em đã đóng góp cho GitHub Achievement Lab.

Thank you for contributing to GitHub Achievement Lab.

## Quy tắc | Rules

- Mỗi pull request chỉ giải quyết một mục tiêu.
- Không gửi secret, token, mật khẩu hoặc dữ liệu cá nhân.
- Không thêm phụ thuộc nếu chưa giải thích lý do.
- Mọi thay đổi hành vi cần có cách kiểm tra rõ ràng.
- Không để đường dẫn file thoát khỏi phạm vi repo.
- Viết nội dung công khai bằng tiếng Việt và tiếng Anh khi phù hợp.
- Nội dung công khai không dùng ký tự gạch dài.

- Keep each pull request focused on one goal.
- Never submit secrets, tokens, passwords, or personal data.
- Explain any new dependency before adding it.
- Include clear verification steps for behavior changes.
- Keep file paths inside the repository scope.
- Use Vietnamese and English for public content when appropriate.
- Do not use long dash characters in public content.

## Quy trình | Workflow

1. Mở issue mô tả bối cảnh và kết quả mong muốn.
2. Tạo branch từ `main`, ví dụ `docs/improve-readme`.
3. Thực hiện thay đổi nhỏ, dễ review.
4. Chạy kiểm tra liên quan.
5. Gửi pull request, ghi rõ thay đổi và bằng chứng.
6. Trả lời review trước khi merge.

1. Open an issue with context and expected outcome.
2. Create a branch from `main`, for example `docs/improve-readme`.
3. Make a small, reviewable change.
4. Run the relevant checks.
5. Open a pull request with changes and evidence.
6. Address review comments before merging.

## Mẫu báo cáo kiểm tra | Verification format

Dùng [review checklist](docs/review-checklist.md) trong giai đoạn review, trước khi merge.

Use the [review checklist](docs/review-checklist.md) during review, before merging.

```text
Checks:
- command/tool: <exact command or tool>
- scope: <files, commits, generated files, and artifacts checked>
- base/head: <base SHA>..<head SHA>
- timestamp: <UTC timestamp>
- result: <pass or details>
- artifact: <path or none>

Manual check:
- <what was verified>
```

## Phạm vi | Scope

Repo này là một phòng lab độc lập. Không thay đổi hoặc phụ thuộc vào các dự án khác của DUCPT.

This repository is an independent lab. Do not modify or depend on DUCPT's other projects.
