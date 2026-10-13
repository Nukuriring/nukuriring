#!/bin/bash
# 클라우드 세션 시작 훅: 검색·중복·연결 스크립트가 쓰는 패키지를 설치하고, 기준 브랜치 상태를 알려 준다.
# 출력은 세션 맥락에 들어간다. PC(로컬) 세션에서는 아무것도 하지 않는다.
set -uo pipefail
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi
cd "${CLAUDE_PROJECT_DIR:-.}"
python3 -c "import kiwipiepy, numpy, sklearn" 2>/dev/null || pip install -q kiwipiepy numpy scikit-learn >/dev/null 2>&1 || echo "알림: kiwipiepy·numpy·scikit-learn 설치에 실패했다. search.py는 글자 2그램으로 동작한다."
BASE=claude/great-einstein-58fp2d
git fetch -q origin 2>/dev/null || true
CUR=$(git branch --show-current 2>/dev/null)
echo "[보관함 상태] 현재 브랜치: ${CUR:-?} / 기준 브랜치: $BASE"
if git rev-parse -q --verify "origin/$BASE" >/dev/null; then
  BEHIND=$(git rev-list --count HEAD..origin/$BASE 2>/dev/null || echo ?)
  AHEAD=$(git rev-list --count origin/$BASE..HEAD 2>/dev/null || echo ?)
  echo "  기준 브랜치보다 뒤처진 커밋 $BEHIND개, 앞선 커밋 $AHEAD개."
  [ "$BEHIND" != "0" ] && echo "  작업 전에 기준 브랜치를 받아야 한다(CLAUDE.md '기준 브랜치' 절)."
  for b in $(git branch -r --format='%(refname:short)' | grep 'origin/claude/' | grep -v "origin/$BASE"); do
    n=$(git rev-list --count origin/$BASE..$b 2>/dev/null || echo 0)
    [ "$n" != "0" ] && echo "  주의: $b 가 기준 브랜치에 없는 커밋 ${n}개를 가지고 있다. 작업 전에 영진 님께 알린다."
  done
fi
exit 0
