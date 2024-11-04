# Setting
클론 후, 패키지 설치     
<code>npm i</code>    

dist 폴더 생성    
<code>npm run build</code>


# Commit Convention
- feat : 새로운 기능 추가
- fix : 버그 수정
- docs : 문서 수정
- style : 코드 포맷팅, 세미콜론 누락, 코드 변경이 없는 경우
- refactor : 코드 리펙토링
- test : 테스트 코드, 리펙토링 테스트 코드 추가
- chore : 빌드 업무 수정, 패키지 매니저 수정

# Branch Convention
- feat: 기능 개발
- refactor: 코드 리팩토링
- hotfix: 배포 버전 버그 수정

# PR Convention
## What
This PR adds the login functionality for users. It includes the following changes:
- Implemented a login form with username and password inputs.
- Integrated with the backend API to send authentication requests.
- Handled various error states and showed corresponding messages to users.

## Why
The login feature is a core functionality of the application that allows users to authenticate into the system.

## How to Test
1. Start the application locally.
2. Navigate to the login page and try logging in with a valid account. Ensure the session is established.
3. Try logging in with invalid credentials and check if appropriate error messages are displayed.

## Screenshots
(스크린샷을 첨부할 수 있다면 여기 넣기)

## Additional Information
...

# Directory
public     
 ┣ icons     
 ┣ background.js // jsx 파일과 요청을 주고 받는 파일     
 ┣ manifest.json     
 ┗ vite.svg     
 src     
 ┣ assets     
 ┣ components     
 ┃ ┗ TabList.jsx // 현재 열려있는 탭 목록     
 ┣ App.css     
 ┣ App.jsx // 확장 프로그램 사이드 패널     
 ┣ index.css     
 ┣ main.jsx     
 ┣ popup.jsx     
 ┗ Preview.jsx // 확장 프로그램 팝업 창     
