prompts = [
    {
        "title": "AI 생산성 서비스 광고 문구 생성",
        "content": (
            "AI 생산성 서비스의 핵심 기능을 소개하는 광고 문구를 작성해주세요. "
            "사용자의 흩어진 업무 정보를 하나의 흐름으로 정리해준다는 메시지를 강조하고, "
            "간결한 제목과 설명 문구를 함께 제안해주세요."
        ),
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "AI 서비스 브랜드 엔드카드 이미지",
        "content": (
            "밝은 회색 책상 위에 실버 노트북과 스마트폰이 놓인 "
            "프리미엄 AI 생산성 서비스 광고 이미지를 생성해주세요. "
            "파란색, 네이비, 흰색을 중심으로 미니멀하고 현실적인 스타일로 표현해주세요."
        ),
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "15초 AI 서비스 광고 영상 구성",
        "content": (
            "60초 분량의 AI 생산성 서비스 광고를 15초 영상으로 줄여주세요. "
            "문제 상황, 핵심 기능, 사용 효과, 브랜드 메시지가 빠르게 전달되도록 "
            "장면별 구성과 내레이션을 작성해주세요."
        ),
        "category": "영상 생성",
        "favorite": False
    }
]


print("기본 프롬프트가 등록되었습니다.")
print(f"등록된 프롬프트 수: {len(prompts)}개")

for index, prompt in enumerate(prompts, start=1):
    print(f"{index}. [{prompt['category']}] {prompt['title']}")