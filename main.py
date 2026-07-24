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


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")

def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
            print("아직 구현되지 않은 기능입니다.")
        else:
            print("올바른 메뉴 번호를 입력해주세요.")

main()