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

categories = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
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

def get_required_input(message):
    while True:
        value = input(message).strip()

        if value:
            return value

        print("내용을 비워둘 수 없습니다. 다시 입력해주세요.")

def select_category():
    print("\n카테고리 선택:")

    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")

    while True:
        choice = input("선택: ").strip()

        if choice.isdigit():
            category_number = int(choice)

            if 1 <= category_number <= len(categories):
                return categories[category_number - 1]

        print("올바른 카테고리 번호를 입력해주세요.")

def add_promt():
    print("\n=== 프롬프트 추가 ===")

    title = get_required_input("제목: ")
    content = get_required_input("내용: ")
    category = select_category()

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")

def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark}"
        )

    print(f"\n총 {len(prompts)}개의 프롬프트")

def show_by_category():
    print("\n=== 카테고리별 조회 ===")

    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")

    while True:
        choice = input("선택: ").strip()

        if choice.isdigit():
            category_number = int(choice)

            if 1 <= category_number <= len(categories):
                selected_category = categories[category_number - 1]
                break

        print("올바른 카테고리 번호를 입력해주세요.")

    filtered_prompts = []

    for prompt in prompts:
        if prompt["category"] == selected_category:
            filtered_prompts.append(prompt)

    print(f"\n[{select_category}] 카테고리 프롬프트")

    if not filtered_prompts:
        print("해당 카테고리에 등록된 프롬프트가 없습니다.")
        return 

    for index, prompt in enumerate(filtered_prompts, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""
        print(f"{index}. {prompt['title']}{favorite_mark}")

    print(f"\n총 {len(filtered_prompts)}개의 프롬프트")

def search_prompt():
    print("\n=== 프롬프트 검색 ===")

    keyword = get_required_input("검색어: ").lower()
    search_results = []

    for prompt in prompts:
        title = prompt["title"].lower()
        content = prompt["content"].lower()

        if keyword in title or keyword in content:
            search_results.append(prompt)

    print("\n검색 결과:")

    if not search_results:
        print("검색 결과가 없습니다.")
        return 

    for index, prompt in enumerate(search_results, start=1):
        favorite_mark = " ⭐" if prompt["favorite"] else ""

        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']}{favorite_mark}"
        )

    print(f"\n{len(search_results)}개의 프롬프트를 찾았습니다.")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_promt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        elif choice in ["5", "6", "7"]:
            print("아직 구현되지 않은 기능입니다.")
        else:
            print("올바른 메뉴 번호를 입력해주세요.")

main()