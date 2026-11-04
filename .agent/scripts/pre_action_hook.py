#!/usr/bin/env python3
import sys
import json

def main():
    payload = {}
    try:
        raw_input = sys.stdin.read()
        if raw_input.strip():
            payload = json.loads(raw_input)
    except Exception:
        pass

    # Nếu là PreToolUse (có trường "toolCall")
    if "toolCall" in payload:
        response = {
            "decision": "allow"
        }
    else:
        # PreInvocation (chạy ngay sau khi nhận prompt từ người dùng)
        instruction = (
            "[BẮT BUỘC - Evidence-Based Engineering]\n"
            "Sau khi nhận prompt, AI Agent PHẢI ĐỌC và TUÂN THỦ TUYỆT ĐỐI kỹ năng 'evidence-based-engineering' "
            "(/Users/hathuy/Documents/github/skills/evidence-based-engineering/SKILL.md) trước khi giải quyết vấn đề kỹ thuật "
            "hoặc viết/chỉnh sửa code.\n"
            "- TUYỆT ĐỐI KHÔNG suy diễn (infer), không suy đoán (guess), không kỳ vọng (assume).\n"
            "- Mọi quyết định kỹ thuật phải có căn cứ kiểm chứng từ repo code/test, tài liệu chính thức, mã nguồn thư viện, hoặc thực nghiệm.\n"
            "- Nếu chưa có căn cứ rõ ràng: tra cứu hoặc nói rõ 'chưa có căn cứ', không phỏng đoán."
        )
        response = {
            "injectSteps": [
                {
                    "ephemeralMessage": instruction
                }
            ],
            "terminationBehavior": ""
        }

    sys.stdout.write(json.dumps(response))
    sys.stdout.flush()

if __name__ == "__main__":
    main()
