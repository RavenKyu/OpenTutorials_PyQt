import QtQuick 2.5

// 사각형의 root 요소(Element)
Rectangle {
    // 요소의 이름은 root
    id: root

    // 속성 정의
    width: 120; height: 240

    // 색 속성
    color: "#4A4A4A"

    // 하위 요소들 선언
    Image {
        id: triangle

        // 부모(root) 값 참조
        x: (parent.width - width)/2; y: 40

        source: 'assets/triangle_red.png'
    }

    // 다른 요소 선언
    Text {
        // 이름없이 사용가능

        // id값을 이용한 참조 가능
        y: triangle.y + triangle.height + 20
        width: root.width

        color: 'white'
        horizontalAlignment: Text.AlignHCenter
        text: 'Triangle'
    }

    Text {
        id: thisLabel

        x: 24; y: 16
        height: 2 * width

        // 사용자 속성 값 선언
        property int times: 24

        // 외부에서 접근 가능하게 별명 선언
        property alias anotherTimes: thisLabel.times

        // 텍스트 속성 설정, 값은 문자열과 사용자 속성 값
        text: "Greetings " + times

        // 폰트그룹 속성 정의
        font.family: "Ubuntu"
        font.pixelSize: 24

        // 키 네비게이션 설정
        KeyNavigation.tab: otherLabel

        // 길이가 달라질경우 signal 발생
        onHeightChanged: console.log('height:', height)

        // 키 이벤트는 focus 상태있때만
        focus: true

        // 포커스 상태에 따른 색 변화
        color: focus?"red":"black"
    }

    Text {
        id: label

        x: 24; y: 24

        // 스페이스바를 카운터할 속성
        property int spacePresses: 0

        text: "Space pressed: " + spacePresses + " times"

        // 글이 바뀌면 콘솔에 로그를 남긴다
        onTextChanged: console.log("text changed to:", text)

        // 포커스가 있어야 동작
        focus: true

        // 스페이스바를 누르면 함수 실행
        Keys.onSpacePressed: {
            increment()
        }

        // ESC키를 누르면 라벨 지우기
        Keys.onEscapePressed: {
            label.text = ''
        }

        // 자바 스크립트 함수
        function increment() {
            spacePresses = spacePresses + 1
        }
    }
}