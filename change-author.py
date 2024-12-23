#!/usr/bin/env python3
import subprocess
import os
import re

# 定义要匹配的提交信息模式
commit_pattern = r"GitHub Actions \d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"

# 创建环境变量设置命令
new_env = {
    'GIT_AUTHOR_NAME': 'github-actions[bot]',
    'GIT_AUTHOR_EMAIL': '41898282+github-actions[bot]@users.noreply.github.com',
    'GIT_COMMITTER_NAME': 'github-actions[bot]',
    'GIT_COMMITTER_EMAIL': '41898282+github-actions[bot]@users.noreply.github.com'
}

# 使用 git filter-branch
cmd = '''
git filter-branch -f --env-filter '
COMMIT_MSG=$(git log --format=%B -n 1 $GIT_COMMIT)
if [[ $COMMIT_MSG =~ "GitHub Actions Crawler ALL IN ONE at" ]]; then
    export GIT_AUTHOR_NAME="github-actions[bot]"
    export GIT_AUTHOR_EMAIL="41898282+github-actions[bot]@users.noreply.github.com"
    export GIT_COMMITTER_NAME="github-actions[bot]"
    export GIT_COMMITTER_EMAIL="41898282+github-actions[bot]@users.noreply.github.com"
else
    export GIT_AUTHOR_NAME="$GIT_AUTHOR_NAME"
    export GIT_AUTHOR_EMAIL="$GIT_AUTHOR_EMAIL"
    export GIT_COMMITTER_NAME="$GIT_COMMITTER_NAME"
    export GIT_COMMITTER_EMAIL="$GIT_COMMITTER_EMAIL"
fi
' --tag-name-filter cat -- --all
'''

subprocess.run(cmd, shell=True)