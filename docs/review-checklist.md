# Checklist review pull request | Pull request review checklist

Dùng checklist này trước khi merge một pull request.

Use this checklist before merging a pull request.

## Nội dung | Content

- [ ] PR có một mục tiêu rõ ràng.
- [ ] Mô tả nêu bối cảnh, thay đổi và ảnh hưởng.
- [ ] Issue liên quan được liên kết nếu có.

- [ ] The PR has one clear goal.
- [ ] The description explains context, changes, and impact.
- [ ] A related issue is linked when available.

## An toàn | Safety

- [ ] Không có secret, token, mật khẩu hoặc dữ liệu cá nhân.
- [ ] Đường dẫn file không thoát khỏi phạm vi repo.
- [ ] Thay đổi phụ thuộc mới có lý do rõ ràng.

- [ ] No secrets, tokens, passwords, or personal data are included.
- [ ] File paths stay inside the repository scope.
- [ ] New dependencies have a clear reason.

## Kiểm tra | Verification

- [ ] Đã chạy kiểm tra liên quan.
- [ ] Kết quả kiểm tra được ghi trong PR.
- [ ] Link nội bộ và file mới đều tồn tại.
- [ ] Không có ký tự gạch dài trong nội dung công khai.

- [ ] Relevant checks were run.
- [ ] Check results are recorded in the PR.
- [ ] Internal links and new files exist.
- [ ] Public content contains no long dash characters.

## Quyết định | Decision

- [ ] Reviewer đã đọc diff, không chỉ đọc mô tả.
- [ ] Finding còn lại có owner và trạng thái rõ ràng.
- [ ] PR đủ điều kiện merge.

- [ ] The reviewer read the diff, not only the description.
- [ ] Remaining findings have a clear owner and state.
- [ ] The PR is ready to merge.
