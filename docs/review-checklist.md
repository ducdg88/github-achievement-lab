# Checklist review pull request | Pull request review checklist

Dùng checklist này trong giai đoạn review, trước khi merge.

Use this checklist during review, before merging.

`CONTRIBUTING.md` là nguồn chuẩn của repo cho các quy tắc về secret, dữ liệu, phụ thuộc, đường dẫn và nội dung công khai.

`CONTRIBUTING.md` is the repository source of truth for secrets, data, dependencies, paths, and public content.

## Nội dung | Content

- [ ] PR có một mục tiêu rõ ràng.
- [ ] Mô tả nêu bối cảnh, thay đổi và ảnh hưởng.
- [ ] Issue liên quan được liên kết nếu có.

- [ ] The PR has one clear goal.
- [ ] The description explains context, changes, and impact.
- [ ] A related issue is linked when available.

## An toàn | Safety

- [ ] Đã đối chiếu và đáp ứng toàn bộ mục `Quy tắc | Rules` trong `CONTRIBUTING.md`.
- [ ] The full `Rules` section in `CONTRIBUTING.md` has been checked and satisfied.

## Kiểm tra | Verification

- [ ] Đã chạy các kiểm tra liên quan.
- [ ] Với mỗi kiểm tra, PR ghi rõ lệnh hoặc công cụ, phạm vi, output và đường dẫn artifact, hoặc ghi rõ không có artifact.
- [ ] Link nội bộ và file mới đều tồn tại.
- [ ] Secret scan bao phủ toàn bộ commit thuộc PR, file sinh ra và artifact, không chỉ cây file cuối hoặc net diff.
- [ ] Không có ký tự gạch dài trong nội dung công khai.

- [ ] Relevant checks were run.
- [ ] For every check, the PR records the command or tool, scope, output, and artifact path, or explicitly states that no artifact exists.
- [ ] Internal links and new files exist.
- [ ] The secret scan covers every commit in the PR, generated files, and artifacts, not only the final tree or net diff.
- [ ] Public content contains no long dash characters.

## Quyết định | Decision

- [ ] Reviewer đã đọc diff, không chỉ đọc mô tả.
- [ ] Tất cả check bắt buộc đều đạt, hoặc có ghi rõ check không áp dụng.
- [ ] Đã có đủ approval theo yêu cầu của repo.
- [ ] Branch đã cập nhật, không còn conflict.
- [ ] Không còn finding blocking chưa xử lý.
- [ ] Finding không blocking còn lại có owner và trạng thái rõ ràng.
- [ ] PR đủ điều kiện merge.

- [ ] The reviewer read the diff, not only the description.
- [ ] All required checks pass, or inapplicable checks are explicitly documented.
- [ ] Required approvals are present for the repository.
- [ ] The branch is up to date and has no conflicts.
- [ ] No unresolved blocking finding remains.
- [ ] Remaining non-blocking findings have a clear owner and state.
- [ ] The PR is ready to merge.
