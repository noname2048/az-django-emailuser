# az-django-emailuser
닉네임이 아닌 이메일을 기준으로 구분하는 유저

## Prerequisite
- `poetry` 설치 필요
- `postgresql` 연결

로컬환경(local.py)
- `poetry add <package_name> --dev`
- `poetry install`

스테이징환경, 테스트환경(staging.py, test.py)
- not use

운영환경(product.py)
- `poetry add <package_name>`
- `poetry install --no-dev`

## 3rd party apps
- `pypi`django-debug-toolbar `import`debug_toolbar
  - sql 시간 관리
