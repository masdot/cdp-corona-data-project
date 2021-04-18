# Credits for the most of this script: https://github.com/jgehrcke/covid-19-germany-gae/blob/master/tools/auto-update.sh (Licensed under MIT License)
#!/usr/bin/env bash
set -o errexit
set -o errtrace

# GITHUB_ACTIONS may be unbound
#set -o nounset
#set -o pipefail

# Change this in local dev branch to not create a branch, and to not make any
# commits.
GIT_COMMIT_CHANGES="yes"

echo "running auto-update.sh in dir: $(pwd)"

RNDSTR=$(python -c 'import uuid; print(uuid.uuid4().hex.upper()[0:4])')
UPDATE_ID="$(date +"%m-%d-%H%M" --utc)-${RNDSTR}"
BRANCH_NAME="data-update/${UPDATE_ID}"

echo "generated branch name: ${RNDSTR}"

if [[ $GIT_COMMIT_CHANGES == "yes" ]]; then
    git branch "${BRANCH_NAME}" || true
    git checkout "${BRANCH_NAME}"
fi


if [[ $GITHUB_ACTIONS == "true" ]]; then
    git config --local user.email "action@github.com"
    git config --local user.name "GitHub Action"
fi

python scripts/data-parser/build-rki-csv.py
if [[ $GIT_COMMIT_CHANGES == "yes" ]]; then
    git add /data/rki/rki-cdr-melde.csv || true
    git add /data/rki/rki-cdr-ref.csv || true
    git commit -m "data: csvs updated ${UPDATE_ID}" || true 
fi

python scripts/plotter/cd-by-age-groups.py
if [[ $GIT_COMMIT_CHANGES == "yes" ]]; then
    git add plots/rki/age_group-cases-deaths.png || true
    git commit -m "data: age-groups plot update ${UPDATE_ID}" || true 
fi

python scripts/plotter/timeseries-cd-r-m.py 
if [[ $GIT_COMMIT_CHANGES == "yes" ]]; then
    git add plots/rki/timeseries-cd-r-m.de.png || true
    git add plots/rki/timeseries-cd-r-m.en.png || true
    git commit -m "data: timeseries plot updated ${UPDATE_ID}" || true 
fi

python scripts/plotter/timeseries-cd-r-m-rw14.py
if [[ $GIT_COMMIT_CHANGES == "yes" ]]; then
    git add plots/rki/timeseries-cd-r-m-rw14.de.png || true
    git add plots/rki/timeseries-cd-r-m-rw14.en.png  || true
    git commit -m "data: csvs updated ${UPDATE_ID}" || true 
fi

python scripts/plotter/timeseries-c-d-r-m-rw14.py.py
if [[ $GIT_COMMIT_CHANGES == "yes" ]]; then
    git add plots/rki/timeseries-c-d-r-m-rw14.de.png || true
    git add plots/rki/timeseries-c-d-r-m-rw14.en.png || true
    git commit -m "data: csvs updated ${UPDATE_ID}" || true 
fi

if [[ $GITHUB_ACTIONS == "true" ]]; then
    git push --set-upstream origin "${BRANCH_NAME}"
else
    # git push
    # When run locally skip the rest
    exit
fi


if [[ $GITHUB_ACTIONS == "true" ]]; then
    # `hub` CLI is available through actions/checkout@v2 -- nice!
    # https://github.com/github/hub#github-actions
    # https://hub.github.com/hub-pull-request.1.html
    PR_URL="$(hub pull-request \
        --base main \
        --head "${BRANCH_NAME}" \
        --message "Automatic data update ${UPDATE_ID}" \
        --reviewer masdot)"

    # Split string on slashes and get last item, for extracting PR ID
    # credits: https://stackoverflow.com/a/3162500/145400
    PR_ID=${PR_URL##*/}
    echo "::set-output name=pr_url::${PR_URL}"
    echo "::set-output name=pr_id::${PR_ID}"
fi
