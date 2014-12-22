#!/bin/bash
export LANG=C
export LC_MESSAGES=C

# Evaluate shvar-style booleans
is_true() {
    case "$1" in
        [tT] | [yY] | [yY][eE][sS] | [tT][rR][uU][eE])
        return 0
        ;;
    esac
    return 1
}

is_false() {
    case "$1" in
        [fF] | [nN] | [nN][oO] | [fF][aA][lL][sS][eE])
        return 0
        ;;
    esac
    return 1
}

function brew-download-scratch {
    local task_id="$1"
    local login="$2"

    mkdir -p scratch
    pushd scratch

    [ -z "$task_id" -o -z "$login" ] && return 1

    local url="http://download.lab.bos.redhat.com/brewroot/scratch/${login}/task_${task_id}/"

    wget -r -nd -l 1 --accept-regex '.*rpm$' "$url"
    rm index.html

    popd
}

REMOTE_BRANCH="systemd-rhel/master"
REMOTE="systemd-rhel"
REMOTE_URL="http://10.3.11.34/msekleta/systemd-rhel.git"

BRANCH="master"
NEW_TAG=""
CREATE_SRPM="false"
SCRATCH_BUILD="false"
FORCE="false"
N_SCRATCH=0
CHCK_KRB="false"
CLEAN="false"
LOGIN=$(whoami)
ARCHES=""
Z_STREAM="false"
DISTGIT=$(git rev-parse --abbrev-ref HEAD)

[ -e gitprepare.config ] && . ./gitprepare.config

while [ "$1" != "${1##[-+]}" ]; do
        case $1 in
        --branch)
                REMOTE_BRANCH="${REMOTE}/$2"
                BRANCH=$2
                CREATE_SRPM="true"
                shift 2
        ;;
        --branch=?*)
                REMOTE_BRANCH="${REMOTE}/${1#--branch=}"
                BRANCH=${1#--branch=}
                CREATE_SRPM="true"
                shift
        ;;
        --z-stream)
                REMOTE_BRANCH="${REMOTE}/${DISTGIT}"
                BRANCH=${DISTGIT}
                Z_STREAM="true"
                shift
        ;;
        --arches)
                ARCHES=$2
                shift 2
        ;;
        --arches=?*)
                ARCHES=${1#--arches=}
                shift
        ;;
        --srpm)
                CREATE_SRPM="true"
                shift
        ;;
        --scratch)
                CREATE_SRPM="true"
                SCRATCH_BUILD="true"
                shift
        ;;
        --force)
                FORCE="true"
                shift
        ;;
        --clean)
                CLEAN="true"
                shift
        ;;
        -n)
                CREATE_SRPM="true"
                N_SCRATCH=$2
                shift 2
        ;;
        *)
                echo $"$0: Usage: gitpreprepare [--branch BRANCH] [--srpm] [--scratch] [-n N] [--force]"
                echo ""
                echo "--branch"
                echo -e "\t download patches from different branch"
                echo "--srpm"
                echo -e "\t only create srpm"
                echo "--scratch"
                echo -e "\t do a scratch build"
                echo "-n N"
                echo -e "\t append N to the end of NVR"
                echo "--force"
                echo -e "\t do not check if repository is clean"
                echo "--arches"
                echo -e "\t specify arches for scratch build"
                echo "--clean"
                echo -e "\t call git reset --hard after everything is done"
                echo "--z-stream"
                echo -e "\t create a z-stream update"
                exit 1;;
    esac
done

git remote | grep -qx ${REMOTE} ||  git remote add ${REMOTE} ${REMOTE_URL}

git fetch ${REMOTE}

if is_true "${SCRATCH_BUILD}" && is_true "${CHK_KRB}" ; then
        #this is most definitelly wrong
        klist | grep -q 'krbtgt/REDHAT\.COM@REDHAT\.COM' || kinit
        klist | grep -q 'krbtgt/REDHAT\.COM@REDHAT\.COM' || kinit
        klist | grep -q 'krbtgt/REDHAT\.COM@REDHAT\.COM' || exit 1
fi

if [ -n "$(git status --porcelain -z)" ] && is_false "${FORCE}" ; then
        echo "Your repo is not clean, exiting"
        exit 1
fi

if git status 2>&1 | grep -q "Your branch is ahead" && is_false "${FORCE}" ; then
        echo "Your repo is ahead, exiting"
        exit 1
fi

OLD_VERSION=$(grep '^Version' systemd.spec | awk '{print $2}')
OLD_RELEASE=$(grep '^Release' systemd.spec | awk '{print $2}' | sed -e 's/%{?dist}.*//')
OLD_POST=$(grep '^Release' systemd.spec | awk '{print $2}' | sed -e 's/.*%{?dist}//')
if is_true "$Z_STREAM" && [ -n "${OLD_POST}" ] ; then
        OLD_TAG="v${OLD_VERSION}-${OLD_RELEASE}${OLD_POST}"
else
        OLD_TAG="v${OLD_VERSION}-${OLD_RELEASE}"
fi

NEW_POST=

if is_true "$CREATE_SRPM" ; then
        NEW_TAG=$OLD_TAG
        NEW_POST=".0.${BRANCH}.${N_SCRATCH}"
else
        NEW_TAG=$(git describe --tags --exact-match ${REMOTE_BRANCH})
        echo $NEW_TAG
        if ! echo $NEW_TAG | grep -qx "v[0-9]\+-[0-9]\+\(\.[0-9]\+\)\?" || [ "${NEW_TAG}" = "${OLD_TAG}" ]; then
                echo "Branch ${REMOTE_BRANCH} is not properly tagged"
                exit 2
        fi
fi

NEW_VERSION=$(echo ${NEW_TAG} | sed -e 's/v\([0-9]\+\)-.*/\1/')
NEW_RELEASE=$(echo ${NEW_TAG} | sed -e 's/v[0-9]\+-\([0-9]*\)\(.*\)/\1/')
is_true "${Z_STREAM}" && NEW_POST=$(echo ${NEW_TAG} | sed -e 's/v[0-9]\+-[0-9]*\(.*\)/\1/')

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
                echo -e "${CHANGELOG}"
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

if is_true "${CREATE_SRPM}" ; then
        echo
        SRPM=$(rhpkg srpm | awk '{print $2;}')
        echo $SRPM

        if is_true "${SCRATCH_BUILD}" ; then
                [ -n "${ARCHES}" ] && ARCHES="--arches=${ARCHES}"
                BUILD_ID=$(rhpkg --dist $(git rev-parse --abbrev-ref HEAD) scratch-build ${ARCHES} --srpm ${SRPM} | tee scratch.log |  grep "Created task"  | sed -e 's/[^0-9]//g')
                #sometimes rhpkg is not able to watch the build so lets wait manually
                while $(brew taskinfo ${BUILD_ID} | grep -q "State: open"); do sleep 10; done
                brew-download-scratch ${BUILD_ID} ${LOGIN}
        fi

        is_true ${CLEAN} && git reset --hard

else
        git add systemd.spec
        git commit -m "systemd-${NEW_VERSION}-${NEW_RELEASE}${NEW_POST}

Resolves: ${BUGLIST}
"
fi
