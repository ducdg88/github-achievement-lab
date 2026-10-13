# Checklist review pull request | Pull request review checklist

Dùng checklist này trong giai đoạn review, trước khi merge.

Use this checklist during review, before merging.

`CONTRIBUTING.md` là nguồn chuẩn của repo cho quy tắc chung. Checklist này là nguồn chuẩn cho bằng chứng review và quyết định merge.

`CONTRIBUTING.md` is the repository source of truth for general rules. This checklist is the source of truth for review evidence and the merge decision.

## Nội dung | Content

- [ ] PR có một mục tiêu rõ ràng.
- [ ] Mô tả nêu bối cảnh, thay đổi và ảnh hưởng.
- [ ] Issue liên quan được liên kết nếu có.

- [ ] The PR has one clear goal.
- [ ] The description explains context, changes, and impact.
- [ ] A related issue is linked when available.

## An toàn | Safety

Đối chiếu từng quy tắc trong `CONTRIBUTING.md`, không dùng một checkbox tổng hợp:

Check each rule in `CONTRIBUTING.md`; do not use one aggregate checkbox:

- [ ] Secret, token, mật khẩu và dữ liệu cá nhân: đạt hoặc ghi finding.
- [ ] Phụ thuộc mới: đạt hoặc ghi lý do và finding.
- [ ] Thay đổi hành vi: có cách kiểm tra rõ ràng hoặc ghi `N/A`.
- [ ] Phạm vi đường dẫn: đạt hoặc ghi finding.
- [ ] Nội dung tiếng Việt và tiếng Anh khi phù hợp: đạt hoặc ghi finding.
- [ ] Ký tự gạch dài trong nội dung công khai: đạt hoặc ghi finding.

- [ ] Secrets, tokens, passwords, and personal data: pass or record a finding.
- [ ] New dependencies: pass or record the reason and finding.
- [ ] Behavior changes have a clear verification method or are marked `N/A`.
- [ ] Path scope: pass or record a finding.
- [ ] Vietnamese and English public content when appropriate: pass or record a finding.
- [ ] Long dash characters in public content: pass or record a finding.

## Kiểm tra | Verification

- [ ] Đã chạy các kiểm tra liên quan.
- [ ] Với mỗi kiểm tra, PR ghi rõ lệnh hoặc công cụ, input set, phạm vi, output và đường dẫn artifact, hoặc ghi rõ không có artifact.
- [ ] Bằng chứng ghi rõ `base SHA`, `head SHA` và thời điểm UTC; phải chạy lại sau commit mới nhất.
- [ ] Link nội bộ và file mới đều tồn tại.
- [ ] Secret scan dùng công cụ đã nêu, bao phủ toàn bộ commit thuộc PR, file sinh ra và artifact, không chỉ cây file cuối hoặc net diff.
- [ ] Long-dash scan bao phủ cây file hiện tại, lịch sử commit, file sinh ra, artifact và nội dung PR nếu có.

- [ ] Relevant checks were run.
- [ ] For every check, the PR records the command or tool, input set, scope, output, and artifact path, or explicitly states that no artifact exists.
- [ ] Evidence records the `base SHA`, `head SHA`, and UTC timestamp; checks are rerun after the latest commit.
- [ ] Internal links and new files exist.
- [ ] The named scanner covers every commit in the PR, generated files, and artifacts, not only the final tree or net diff.
- [ ] The long-dash scan covers the current tree, commit history, generated files, artifacts, and PR text when applicable.

## Quyết định | Decision

- [ ] Reviewer đã đọc diff, không chỉ đọc mô tả.
- [ ] Đã ghi trạng thái cổng GitHub: required checks, approvals và ruleset/branch protection; mục nào chưa bật phải ghi `N/A, chưa cấu hình`, không được gọi là đã enforce.
- [ ] Tất cả check bắt buộc đều đạt, hoặc có ghi rõ check không áp dụng.
- [ ] Đã có đủ approval theo yêu cầu của repo, nếu repo yêu cầu.
- [ ] Bằng chứng được chạy lại với commit head mới nhất và branch không còn conflict.
- [ ] Không còn finding blocking chưa xử lý.
- [ ] Finding không blocking còn lại có owner và trạng thái rõ ràng.
- [ ] PR đủ điều kiện merge chỉ sau khi các cổng áp dụng đã được xác minh.

- [ ] The reviewer read the diff, not only the description.
- [ ] The GitHub gate state is recorded: required checks, approvals, and ruleset or branch protection; any disabled gate is marked `N/A, not configured`, not claimed as enforced.
- [ ] All required checks pass, or inapplicable checks are explicitly documented.
- [ ] Required approvals are present when the repository requires them.
- [ ] Evidence was rerun against the latest head commit and the branch has no conflicts.
- [ ] No unresolved blocking finding remains.
- [ ] Remaining non-blocking findings have a clear owner and state.
- [ ] The PR is ready to merge only after applicable gates are verified.
