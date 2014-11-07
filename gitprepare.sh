#!/bin/bash
export LANG=C
export LC_MESSAGES=C

REMOTE_BRANCH="systemd-rhel/master"
BRANCH="master"
NEW_TAG=
SCRATCH=

while [ "$1" != "${1##[-+]}" ]; do
        case $1 in
        '')
                echo echo $"$0: Usage: gitpreprepare [--branch BRANCH] [--srpm]"
                exit 1;;
        --branch)
                REMOTE_BRANCH="systemd-rhel/$2"
                BRANCH=$2
                shift 2
        ;;
        --branch=?*)
                REMOTE_BRANCH="systemd-rhel/${1#--branch=}"
                BRANCH=${1#--branch=}
                shift
        ;;
        --srpm)
                SCRATCH="true"
                shift
        ;;
        *)
                echo $"$0: Usage: gitpreprepare [--branch BRANCH] [--srpm]"
                exit 1;;
    esac
done

git remote | grep -qx systemd-rhel ||  git remote add systemd-rhel http://10.3.11.34/msekleta/systemd-rhel.git

git fetch systemd-rhel

OLD_VERSION=$(grep '^Version' systemd.spec | awk '{print $2}')
OLD_RELEASE=$(grep '^Release' systemd.spec | awk '{print $2}' | sed -e 's/%{?dist}.*//')
OLD_POST=$(grep '^Release' systemd.spec | awk '{print $2}' | sed -e 's/.*%{?dist}//')
OLD_TAG="v${OLD_VERSION}-${OLD_RELEASE}"

NEW_POST=

if [ -n "$SCRATCH" ] ; then
        NEW_TAG=$OLD_TAG
        NEW_POST=".0.${BRANCH}"
else
        NEW_TAG=$(git describe --tags --exact-match ${REMOTE_BRANCH})
        echo $NEW_TAG
        if ! echo $NEW_TAG | grep -x "v[0-9]\+-[0-9]\+" ; then
                echo "Branch ${REMOTE_BRANCH} is not properly tagged"
                exit 2
        fi
fi

clear
echo $NEW_TAG

NEW_VERSION=$(echo ${NEW_TAG} | sed -e 's/v\([0-9]\+\)-.*/\1/')
NEW_RELEASE=$(echo ${NEW_TAG} | sed -e 's/v[0-9]\+-\(.*\)/\1/')

BUGLIST=""
CHANGELOG=""

MSG_HEAD=$(echo "* $(date +"%a %b %d %Y") $(git config user.name) <$(git config user.email)> - ${NEW_VERSION}-${NEW_RELEASE}${NEW_POST}")


for COMMIT in $(git rev-list --reverse ${REMOTE_BRANCH} ${OLD_TAG}..${NEW_TAG}); do
        RESOLVES=$(git show ${COMMIT} | grep '^\s*\(Resolves\)\|\(Related\):\s*#' | awk '{print $2}')
        if [ -n "${RESOLVES}" ]; then
                CHANGELOG="${CHANGELOG}- $(git log --format=%s -n 1 ${COMMIT} ) (${RESOLVES})\n"
                echo ${BUGLIST} | grep -q ${RESOLVES} && continue
                [ -n "${BUGLIST}" ] && BUGLIST="${BUGLIST},"
                BUGLIST="${BUGLIST}${RESOLVES}"
        fi
done

git rm -f [0-9][0-9][0-9][0-9]*.patch
git format-patch -M -N --no-signature v208..${REMOTE_BRANCH}

for i in [0-9][0-9][0-9][0-9]*.patch; do
        [ -f "$i" ] || continue
        git add "$i"
done

IFS="
"
while read -r line; do
        case "$line" in
        Patch[0-9][0-9][0-9][0-9]*)
                ;;
        *RHEL-specific*)
                printf "%s\n" "$line"
                for i in [0-9][0-9][0-9][0-9]*.patch; do
                    printf "Patch%s: %s\n" "${i%%-*}" "$i"
                done
                ;;
        %changelog*)
                printf "%s\n" "${line}"
                printf "%s\n" "${MSG_HEAD}"
                echo -e  "${CHANGELOG}"
                ;;
        Version:*)
                printf "Version:        %s\n" "${NEW_VERSION}"
                ;;
        Release:*)
                printf "Release:        %s\n" "${NEW_RELEASE}%{?dist}${NEW_POST}"
                ;;
        *)
                printf "%s\n" "${line}"
                ;;
        esac
done < systemd.spec >systemd.spec.new

mv systemd.spec.new systemd.spec

if [ -n "$SCRATCH" ]; then
        echo
        rhpkg srpm | awk '{print $2;}'
else
        git add systemd.spec
        git commit -m "systemd-${NEW_VERSION}-${NEW_RELEASE}

Resolves: ${BUGLIST}
"
fi
