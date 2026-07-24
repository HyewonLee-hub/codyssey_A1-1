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

        print("입력값을 비워둘 수 없습니다. 다시 입력해주세요.")


def select_category():
    print("\n카테고리 선택:")

    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")

    custom_category_number = len(categories) + 1
    print(f"{custom_category_number}) 직접 입력")

    while True:
        choice = input("선택: ").strip()

        if not choice.isdigit():
            print("올바른 카테고리 번호를 입력해주세요.")
            continue

        category_number = int(choice)

        if 1 <= category_number <= len(categories):
            return categories[category_number - 1]

        if category_number == custom_category_number:
            custom_category = get_required_input("새 카테고리 이름: ")

            if custom_category not in categories:
                categories.append(custom_category)

            return custom_category

        print("올바른 카테고리 번호를 입력해주세요.")


def add_prompt():
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

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

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


def show_prompt_detail():
    print("\n=== 프롬프트 상세 보기 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    while True:
        choice = input("\n상세히 볼 프롬프트 번호: ").strip()

        if choice.isdigit():
            prompt_number = int(choice)

            if 1 <= prompt_number <= len(prompts):
                selected_prompt = prompts[prompt_number - 1]
                break

        print("올바른 프롬프트 번호를 입력해주세요.")

    favorite_mark = "⭐" if selected_prompt["favorite"] else "아니요"

    print("\n────────────────────────────")
    print(f"제목: {selected_prompt['title']}")
    print(f"카테고리: {selected_prompt['category']}")
    print(f"즐겨찾기: {favorite_mark}")
    print("────────────────────────────")
    print("내용:")
    print(selected_prompt["content"])
    print("────────────────────────────")


def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    show_list()

    while True:
        choice = input("\n프롬프트 번호 입력: ").strip()

        if choice.isdigit():
            prompt_number = int(choice)

            if 1 <= prompt_number <= len(prompts):
                selected_prompt = prompts[prompt_number - 1]
                break

        print("올바른 프롬프트 번호를 입력해주세요.")

    selected_prompt["favorite"] = not selected_prompt["favorite"]

    if selected_prompt["favorite"]:
        print(
            f"\n'{selected_prompt['title']}' 프롬프트를 "
            "즐겨찾기에 추가했습니다!"
        )
    else:
        print(
            f"\n'{selected_prompt['title']}' 프롬프트를 "
            "즐겨찾기에서 해제했습니다!"
        )


def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")

    favorite_prompts = []

    for prompt in prompts:
        if prompt["favorite"]:
            favorite_prompts.append(prompt)

    if not favorite_prompts:
        print("즐겨찾기된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(favorite_prompts, start=1):
        print(
            f"{index}. [{prompt['category']}] "
            f"{prompt['title']} ⭐"
        )

    print(f"\n총 {len(favorite_prompts)}개의 즐겨찾기")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_prompt_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("올바른 메뉴 번호를 입력해주세요.")


if __name__ == "__main__":
    main()